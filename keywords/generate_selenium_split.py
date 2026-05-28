import os
import xml.etree.ElementTree as ET


BASE_DIR = r"c:\Users\Lokesh\Documents\GitHub\Robot-Framework-Python\keywords"
XML_PATH = os.path.join(BASE_DIR, "seleniumlibrary_all_keywords.xml")
OUT_DIR = os.path.join(BASE_DIR, "seleniumlibrary_full_split")


def category_for(name: str) -> str:
    n = name.lower()
    if any(x in n for x in ["browser", "window", "location", "title", "go to", "reload", "maximize"]):
        return "browser_and_navigation"
    if any(
        x in n
        for x in [
            "input",
            "click",
            "double click",
            "drag",
            "drop",
            "mouse",
            "press keys",
            "submit",
            "checkbox",
            "radio button",
            "select from list",
            "unselect",
        ]
    ):
        return "element_actions_and_forms"
    if any(x in n for x in ["wait", "should", "contain", "visible", "enabled", "disabled", "text", "page should", "element should"]):
        return "waits_and_assertions"
    if any(x in n for x in ["frame", "alert", "confirm", "prompt", "select window", "switch window"]):
        return "frames_alerts_and_windows"
    if any(x in n for x in ["cookie", "screenshot", "capture", "javascript", "execute"]):
        return "cookies_screenshots_and_javascript"
    if any(x in n for x in ["timeout", "implicit wait", "speed"]):
        return "timeouts_and_runtime_settings"
    return "miscellaneous"


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    root = ET.parse(XML_PATH).getroot()

    all_keywords = []
    for kw in root.findall(".//kw"):
        name = kw.attrib.get("name", "").strip()
        if not name:
            continue

        args = []
        for arg in kw.findall("./arguments/arg"):
            value = (arg.text or "").strip()
            if value:
                args.append(value)

        doc = (kw.findtext("doc") or "").strip()
        doc_line = " ".join(doc.split())
        if len(doc_line) > 320:
            doc_line = doc_line[:317] + "..."

        all_keywords.append((name, args, doc_line))

    grouped = {}
    for item in all_keywords:
        grouped.setdefault(category_for(item[0]), []).append(item)

    for key in grouped:
        grouped[key].sort(key=lambda x: x[0].lower())

    ordered_categories = [
        "browser_and_navigation",
        "element_actions_and_forms",
        "waits_and_assertions",
        "frames_alerts_and_windows",
        "cookies_screenshots_and_javascript",
        "timeouts_and_runtime_settings",
        "miscellaneous",
    ]

    created_files = []

    for index, category in enumerate(ordered_categories, start=1):
        items = grouped.get(category, [])
        if not items:
            continue

        filename = f"{index:02d}_{category}.md"
        path = os.path.join(OUT_DIR, filename)
        created_files.append(filename)

        lines = [f"# SeleniumLibrary Keywords - {category.replace('_', ' ').title()}", ""]
        for name, args, doc in items:
            lines.append(f"## {name}")
            lines.append("")
            lines.append("**Syntax**")
            lines.append("```robot")
            syntax = "    ".join([name] + args) if args else name
            lines.append(syntax)
            lines.append("```")
            lines.append("")
            if doc:
                lines.append("**Description**")
                lines.append(doc)
                lines.append("")

        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write("\n".join(lines).rstrip() + "\n")

    readme_path = os.path.join(OUT_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("# SeleniumLibrary Full Split Keyword Notes\n\n")
        handle.write("Auto-generated from installed SeleniumLibrary via `robot.libdoc`.\n\n")
        handle.write("Files:\n")
        for filename in created_files:
            handle.write(f"- `{filename}`\n")

    print(f"Generated {len(created_files)} files in {OUT_DIR}")


if __name__ == "__main__":
    main()
