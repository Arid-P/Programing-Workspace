from pathlib import Path
from pypdf import PdfWriter
from icecream import ic 

def get_folders(parent: Path) -> list[Path]:
    return sorted([
        f for f in parent.iterdir()
        if f.is_dir() and f.name not in {"combined", "00 Short Notes", "01 Practice & Helper Book"}
    ])


def merge_pdfs(folder: Path, output_path: Path) -> int:
    pdfs = sorted(folder.rglob("*.pdf"))
    if not pdfs:
        return 0

    writer = PdfWriter()
    for pdf in pdfs:
        writer.append(str(pdf))

    with open(output_path, "wb") as f:
        writer.write(f)

    return len(pdfs)


def main():
    parent = Path("../../", "Download", "X")  # Change if needed
    combined_dir = parent / "combined"
    combined_dir.mkdir(exist_ok=True)

    folders = get_folders(parent)
    if not folders:
        print("No folders found.")
        exit()

    for folder in folders:
        output_path = combined_dir / f"{folder.name}.pdf"

        if output_path.exists():                          # ← check added
            print(f"⏭ {folder.name} → already combined, skipping")
            continue

        count = merge_pdfs(folder, output_path)

        if count:
            print(f"✓ {folder.name} → {count} PDFs merged → {output_path}")
        else:
            print(f"⚠ {folder.name} → skipped (no PDFs found)")
        print()
        
    print("\nDone!")


if __name__ == "__main__":
    main()