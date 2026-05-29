"""Generate markdown keyword reference from libdoc XML exports."""
from pathlib import Path
import os
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
BASE_DIR = ROOT / "docs" / "reference" / "libdoc"
OUT_DIR = ROOT / "docs" / "reference" / "markdown"


def clean(text: str) -> str:
    value = " ".join((text or "").split())
    if len(value) > 360:
        return value[:357] + "..."
    return value


def write_library_markdown(xml_path: Path, out_root: Path) -> str:
    library_name = xml_path.stem
    lib_dir = out_root / library_name
    lib_dir.mkdir(parents=True, exist_ok=True)

    root = ET.parse(xml_path).getroot()
    keywords = []
    for kw in root.findall(".//kw"):
        name = (kw.attrib.get("name") or "").strip()
        if not name:
            continue
        args = []
        for arg in kw.findall("./arguments/arg"):
            arg_val = (arg.text or "").strip()
            if arg_val:
                args.append(arg_val)
        doc = clean(kw.findtext("doc") or "")
        keywords.append((name, args, doc))

    keywords.sort(key=lambda k: k[0].lower())

    out_file = lib_dir / f"{library_name}_keywords.md"
    lines = [f"# {library_name} Keywords", ""]
    for name, args, doc in keywords:
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

    out_file.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    return library_name


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    xml_files = sorted(BASE_DIR.glob("*.xml"))

    done = []
    for xml_path in xml_files:
        lib = write_library_markdown(xml_path, OUT_DIR)
        done.append(lib)

    readme = OUT_DIR / "README.md"
    readme.write_text(
        "# Full Robot Keyword Reference (Installed Libraries)\n\n"
        "Generated from `robot.libdoc` XML files in `docs/reference/libdoc/`.\n\n"
        "Regenerate:\n\n"
        "```powershell\n"
        "python scripts/generate_full_reference_md.py\n"
        "```\n\n"
        "Libraries:\n"
        + "".join(f"- `{lib}/{lib}_keywords.md`\n" for lib in done),
        encoding="utf-8",
        newline="\n",
    )

    print(f"Generated markdown for {len(done)} libraries in {OUT_DIR}")


if __name__ == "__main__":
    main()
