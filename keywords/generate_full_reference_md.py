import os
import xml.etree.ElementTree as ET


BASE_DIR = r"c:\Users\Lokesh\Documents\GitHub\Robot-Framework-Python\keywords\full_reference"
OUT_DIR = os.path.join(BASE_DIR, "markdown_split")


def clean(text: str) -> str:
    value = " ".join((text or "").split())
    if len(value) > 360:
        return value[:357] + "..."
    return value


def write_library_markdown(xml_path: str, out_root: str) -> str:
    library_name = os.path.splitext(os.path.basename(xml_path))[0]
    lib_dir = os.path.join(out_root, library_name)
    os.makedirs(lib_dir, exist_ok=True)

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

    out_file = os.path.join(lib_dir, f"{library_name}_keywords.md")
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

    with open(out_file, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines).rstrip() + "\n")

    return library_name


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    xml_files = sorted(
        [f for f in os.listdir(BASE_DIR) if f.lower().endswith(".xml")]
    )

    done = []
    for xml_file in xml_files:
        lib = write_library_markdown(os.path.join(BASE_DIR, xml_file), OUT_DIR)
        done.append(lib)

    readme = os.path.join(OUT_DIR, "README.md")
    with open(readme, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Full Robot Keyword Reference (Installed Libraries)\n\n")
        f.write("Generated from `robot.libdoc` XML files.\n\n")
        f.write("Libraries:\n")
        for lib in done:
            f.write(f"- `{lib}/{lib}_keywords.md`\n")

    print(f"Generated markdown for {len(done)} libraries in {OUT_DIR}")


if __name__ == "__main__":
    main()
