"""
Log into Transunit, walk All Menus, visit each reachable page, and write one folder per page under pages/.

Run:
    pip install selenium
    python discover_pages.py

Optional env: TRANSUNIT_URL, TRANSUNIT_USER, TRANSUNIT_PASS
"""
from __future__ import annotations

import json
import os
import re
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"

BASE_URL = os.getenv("TRANSUNIT_URL", "https://transunit.traumasoft.com").rstrip("/")
USERNAME = os.getenv("TRANSUNIT_USER", "rbane")
PASSWORD = os.getenv("TRANSUNIT_PASS", "Jmi@2026")
SITE_HOST = urlparse(BASE_URL).netloc


@dataclass
class MenuLink:
    section: str
    label: str
    url: str
    external: bool = False


@dataclass
class PageCapture:
    folder: str
    section: str
    label: str
    url: str
    title: str = ""
    headings: list[str] = field(default_factory=list)
    buttons: list[str] = field(default_factory=list)
    inputs: list[dict] = field(default_factory=list)
    links_on_page: list[dict] = field(default_factory=list)
    table_count: int = 0
    form_count: int = 0
    visited: bool = False
    note: str = ""


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^\w\-]+", "-", value)
    return value.strip("-") or "page"


def label_from_url(url: str) -> str:
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    route = query.get("a", [""])[0]
    if route:
        return route.replace(":", " / ").replace("_", " ").replace("/", " / ")
    path = parsed.path.strip("/") or "home"
    return path.replace("_", " ").replace("/", " / ")


def folder_name(section: str, label: str, url: str) -> str:
    parsed = urlparse(url)
    route = parse_qs(parsed.query).get("a", [""])[0]
    if route:
        base = slugify(route.replace(":", "-").replace("/", "-"))
    else:
        base = slugify(parsed.path or "home")
    if not base:
        base = "page"
    section_slug = slugify(section) if section else ""
    if section_slug and not base.startswith(section_slug):
        return f"{section_slug}-{base}"[:80]
    return base[:80]


def login(driver: webdriver.Chrome, wait: WebDriverWait) -> None:
    driver.get(BASE_URL)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="login-username"]')))
    driver.find_element(By.CSS_SELECTOR, '[data-testid="login-username"]').send_keys(USERNAME)
    driver.find_element(By.CSS_SELECTOR, '[data-testid="login-password"]').send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, '[data-testid="login-submit"]').click()
    wait.until(lambda d: d.current_url.rstrip("/") != BASE_URL.rstrip("/"))
    time.sleep(3)


def open_all_menus(driver: webdriver.Chrome, wait: WebDriverWait) -> None:
    btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="All Menus"]')))
    btn.click()
    time.sleep(0.8)


def collect_menu_links(driver: webdriver.Chrome, wait: WebDriverWait) -> list[MenuLink]:
    open_all_menus(driver, wait)
    sections: list[tuple[str, str | None]] = []
    seen_sections: set[str] = set()
    for item in driver.find_elements(By.CSS_SELECTOR, ".ts_menu_list_item"):
        if not item.text.strip() or not item.is_displayed():
            continue
        name = item.text.strip().split("\n")[0]
        if name in seen_sections:
            continue
        seen_sections.add(name)
        sections.append((name, item.get_attribute("aria-owns")))

    found: list[MenuLink] = []
    seen_urls: set[str] = set()

    for section, owns in sections:
        open_all_menus(driver, wait)
        candidates = driver.find_elements(
            By.XPATH,
            f"//div[contains(@class,'ts_menu_list_item')][normalize-space()='{section}']",
        )
        target = next((t for t in candidates if t.is_displayed()), None)
        if not target:
            continue
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            target,
        )
        time.sleep(0.3)
        try:
            ActionChains(driver).move_to_element(target).perform()
        except Exception:
            driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));", target)
        time.sleep(1)

        section_links: list[MenuLink] = []
        if owns:
            for anchor in driver.find_elements(By.CSS_SELECTOR, f"#{owns} a[href]"):
                href = (anchor.get_attribute("href") or "").strip()
                if not href or href.startswith("javascript:"):
                    continue
                text = (anchor.text or anchor.get_attribute("title") or "").strip()
                label = text or label_from_url(href)
                external = SITE_HOST not in urlparse(href).netloc
                link = MenuLink(section=section, label=label, url=href, external=external)
                section_links.append(link)
        else:
            for anchor in driver.find_elements(
                By.XPATH,
                f"//div[contains(@class,'ts_menu_list_item')][normalize-space()='{section}']//a[@href]",
            ):
                href = (anchor.get_attribute("href") or "").strip()
                if not href:
                    continue
                text = (anchor.text or "").strip()
                label = text or label_from_url(href)
                external = SITE_HOST not in urlparse(href).netloc
                section_links.append(MenuLink(section=section, label=label, url=href, external=external))

        if not section_links:
            placeholder = f"{BASE_URL}/#menu-{slugify(section)}"
            if placeholder not in seen_urls:
                found.append(
                    MenuLink(
                        section=section,
                        label="(no direct links in menu flyout for this user)",
                        url=placeholder,
                        external=False,
                    )
                )
                seen_urls.add(placeholder)
            continue

        for link in section_links:
            if link.url in seen_urls:
                continue
            seen_urls.add(link.url)
            found.append(link)

    return found


def collect_quick_nav_links(driver: webdriver.Chrome) -> list[MenuLink]:
    """Top navigation exposes many routes even when All Menus flyouts fail to open."""
    links: list[MenuLink] = []
    seen: set[str] = set()
    for anchor in driver.find_elements(By.CSS_SELECTOR, "a[href*='main.php']"):
        href = (anchor.get_attribute("href") or "").strip()
        if not href or href.startswith("javascript:"):
            continue
        if href.endswith("#") or href.endswith("/#"):
            href = href.rstrip("#")
        if not href or "logout" in href.lower() or href in seen:
            continue
        if SITE_HOST not in urlparse(href).netloc:
            continue
        seen.add(href)
        text = " ".join((anchor.text or "").split())
        route = parse_qs(urlparse(href).query).get("a", [""])[0]
        section = route.split(":")[0].replace("_", " ").title() if route else "Navigation"
        links.append(
            MenuLink(
                section=section,
                label=text or label_from_url(href),
                url=href,
                external=False,
            )
        )
    return links


def merge_menu_links(*groups: list[MenuLink]) -> list[MenuLink]:
    merged: list[MenuLink] = []
    seen: set[str] = set()
    for group in groups:
        for link in group:
            if link.url in seen:
                continue
            seen.add(link.url)
            merged.append(link)
    return merged


def visible_texts(driver: webdriver.Chrome, selector: str, limit: int = 40) -> list[str]:
    texts: list[str] = []
    for el in driver.find_elements(By.CSS_SELECTOR, selector):
        if not el.is_displayed():
            continue
        text = " ".join((el.text or "").split())
        if text and text not in texts:
            texts.append(text)
        if len(texts) >= limit:
            break
    return texts


def collect_inputs(driver: webdriver.Chrome) -> list[dict]:
    inputs: list[dict] = []
    for el in driver.find_elements(By.CSS_SELECTOR, "input, select, textarea"):
        if not el.is_displayed():
            continue
        entry = {
            "tag": el.tag_name,
            "type": el.get_attribute("type") or "",
            "name": el.get_attribute("name") or "",
            "id": el.get_attribute("id") or "",
            "placeholder": el.get_attribute("placeholder") or "",
            "label": el.get_attribute("aria-label") or "",
        }
        key = (entry["tag"], entry["id"], entry["name"], entry["placeholder"])
        if not any((entry["id"], entry["name"], entry["placeholder"], entry["label"])):
            continue
        if entry not in inputs:
            inputs.append(entry)
        if len(inputs) >= 50:
            break
    return inputs


def collect_page_links(driver: webdriver.Chrome) -> list[dict]:
    links: list[dict] = []
    seen: set[str] = set()
    for anchor in driver.find_elements(By.CSS_SELECTOR, "a[href]"):
        href = (anchor.get_attribute("href") or "").strip()
        if not href or href.startswith("javascript:") or href in seen:
            continue
        if SITE_HOST not in urlparse(href).netloc:
            continue
        if "logout" in href.lower():
            continue
        text = " ".join((anchor.text or "").split())
        links.append({"text": text or label_from_url(href), "url": href})
        seen.add(href)
        if len(links) >= 80:
            break
    return links


def capture_live_page(
    driver: webdriver.Chrome,
    wait: WebDriverWait,
    capture: PageCapture,
) -> PageCapture:
    if capture.url.startswith(f"{BASE_URL}/#menu-"):
        capture.note = "Menu section only — no navigable URL exposed in All Menus for this account."
        return capture

    if SITE_HOST not in urlparse(capture.url).netloc:
        capture.note = "External link (not scraped; opening would leave Transunit)."
        return capture

    if "logout" in capture.url.lower():
        capture.note = "Logout link skipped to keep the session."
        return capture

    driver.get(capture.url)
    time.sleep(3)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
    except Exception:
        pass

    capture.visited = True
    capture.url = driver.current_url
    capture.title = driver.title or ""
    capture.headings = visible_texts(driver, "h1, h2, h3")
    capture.buttons = visible_texts(driver, "button, [role='button']")
    capture.inputs = collect_inputs(driver)
    capture.links_on_page = collect_page_links(driver)
    capture.table_count = len(driver.find_elements(By.CSS_SELECTOR, "table"))
    capture.form_count = len(driver.find_elements(By.CSS_SELECTOR, "form"))
    return capture


def write_page_folder(capture: PageCapture, screenshot_path: Path | None) -> None:
    folder = PAGES_DIR / capture.folder
    folder.mkdir(parents=True, exist_ok=True)

    page_json = folder / "page.json"
    page_json.write_text(
        json.dumps(asdict(capture), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        f"# {capture.label}",
        "",
        f"- **Menu section:** {capture.section}",
        f"- **URL:** {capture.url}",
        f"- **Title:** {capture.title or '(not visited)'}",
        f"- **Visited:** {'yes' if capture.visited else 'no'}",
    ]
    if capture.note:
        lines.append(f"- **Note:** {capture.note}")

    if capture.headings:
        lines.extend(["", "## Headings", ""])
        lines.extend(f"- {h}" for h in capture.headings)

    if capture.buttons:
        lines.extend(["", "## Buttons / actions (sample)", ""])
        lines.extend(f"- {b}" for b in capture.buttons[:30])

    if capture.inputs:
        lines.extend(["", "## Form fields (sample)", ""])
        for inp in capture.inputs[:30]:
            parts = [p for p in [inp.get("id"), inp.get("name"), inp.get("placeholder"), inp.get("label")] if p]
            lines.append(f"- `{inp.get('tag')}` ({inp.get('type', '')}) {' / '.join(parts)}")

    lines.extend(["", "## Counts", ""])
    lines.append(f"- Tables: {capture.table_count}")
    lines.append(f"- Forms: {capture.form_count}")
    lines.append(f"- In-app links on page: {len(capture.links_on_page)}")

    if capture.links_on_page:
        lines.extend(["", "## Subpages / links on this page", ""])
        for link in capture.links_on_page[:40]:
            lines.append(f"- {link['text']} → `{link['url']}`")
        if len(capture.links_on_page) > 40:
            lines.append(f"- … and {len(capture.links_on_page) - 40} more")

    if screenshot_path and screenshot_path.exists():
        lines.extend(["", "## Screenshot", "", "![page screenshot](screenshot.png)"])

    (folder / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_site_map(captures: list[PageCapture], menu_links: list[MenuLink], home: PageCapture) -> None:
    lines = [
        "# Transunit site map (discovered)",
        "",
        f"Base URL: `{BASE_URL}`",
        "",
        "## After login (landing)",
        "",
        f"- Folder: `{home.folder}/` — {home.url}",
        "",
        "## All Menus → pages",
        "",
    ]

    by_section: dict[str, list[PageCapture]] = {}
    for cap in captures:
        by_section.setdefault(cap.section, []).append(cap)

    for section in sorted(by_section):
        lines.append(f"### {section}")
        lines.append("")
        for cap in by_section[section]:
            status = "visited" if cap.visited else "menu-only / skipped"
            lines.append(f"- **{cap.label}** → [`{cap.folder}/`]({cap.folder}/) ({status})")
            lines.append(f"  - URL: `{cap.url}`")
        lines.append("")

    lines.extend(["## Raw menu URLs", "", "| Section | Label | URL | External |", "| --- | --- | --- | --- |"])
    for link in menu_links:
        lines.append(f"| {link.section} | {link.label} | `{link.url}` | {'yes' if link.external else 'no'} |")

    (PAGES_DIR / "SITE_MAP.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    index = {
        "base_url": BASE_URL,
        "home": asdict(home),
        "pages": [asdict(c) for c in captures],
        "menu_links": [asdict(m) for m in menu_links],
    }
    (PAGES_DIR / "site-index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    if PAGES_DIR.exists():
        for child in PAGES_DIR.iterdir():
            if child.is_dir():
                for f in child.iterdir():
                    f.unlink()
                child.rmdir()
            elif child.is_file():
                child.unlink()
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=opts)
    wait = WebDriverWait(driver, 30)

    try:
        login(driver, wait)

        menu_links = merge_menu_links(
            collect_menu_links(driver, wait),
            collect_quick_nav_links(driver),
        )

        home = PageCapture(
            folder="00-after-login",
            section="Home",
            label="After login landing",
            url=driver.current_url,
        )
        home = capture_live_page(driver, wait, home)
        shot = PAGES_DIR / home.folder / "screenshot.png"
        shot.parent.mkdir(parents=True, exist_ok=True)
        driver.save_screenshot(str(shot))
        write_page_folder(home, shot)
        captures: list[PageCapture] = []
        used_folders: set[str] = set()

        visited_urls: set[str] = {home.url}

        for link in menu_links:
            folder = folder_name(link.section, link.label, link.url)
            if folder in used_folders:
                folder = f"{folder}-{len(used_folders)}"
            used_folders.add(folder)

            capture = PageCapture(
                folder=folder,
                section=link.section,
                label=link.label,
                url=link.url,
                note="",
            )
            if link.external or "logout" in link.url.lower() or link.url.startswith(f"{BASE_URL}/#menu-"):
                if link.external:
                    capture.note = "External menu target."
                elif "logout" in link.url.lower():
                    capture.note = "Logout skipped."
                else:
                    capture.note = "No flyout links for this menu section."
            else:
                if capture.url in visited_urls:
                    capture.note = "Same URL as an earlier page; see that folder for full capture."
                    write_page_folder(capture, None)
                    captures.append(capture)
                    print(f"Skipped duplicate URL: {capture.folder}")
                    continue
                capture = capture_live_page(driver, wait, capture)
                visited_urls.add(capture.url)
                shot = PAGES_DIR / capture.folder / "screenshot.png"
                shot.parent.mkdir(parents=True, exist_ok=True)
                driver.save_screenshot(str(shot))
                write_page_folder(capture, shot)
                captures.append(capture)
                print(f"Captured: {capture.folder} ({capture.url})")
                continue

            write_page_folder(capture, None)
            captures.append(capture)
            print(f"Documented (not visited): {capture.folder} — {capture.note}")

        write_site_map(captures, menu_links, home)
        print(f"\nDone. {len(captures) + 1} folders under {PAGES_DIR}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
