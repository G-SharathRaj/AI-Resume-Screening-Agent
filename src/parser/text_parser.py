from pathlib import Path


def extract_text_from_txt(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"{file_path} not found.")

    return path.read_text(encoding="utf-8")