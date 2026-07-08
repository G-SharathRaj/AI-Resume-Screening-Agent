from pathlib import Path
from docx import Document


def extract_text_from_docx(file_path: str) -> str:
    """
    Extract text from a DOCX resume.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    document = Document(path)

    paragraphs = [
        paragraph.text.strip()
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)