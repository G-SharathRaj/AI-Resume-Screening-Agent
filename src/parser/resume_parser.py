from pathlib import Path

from src.parser.pdf_parser import extract_text_from_pdf
from src.parser.docx_parser import extract_text_from_docx
from src.parser.text_parser import extract_text_from_txt


def parse_resume(file_path: str):

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        text = extract_text_from_pdf(file_path)

    elif extension == ".docx":
        text = extract_text_from_docx(file_path)

    elif extension == ".txt":
        text = extract_text_from_txt(file_path)

    else:
        raise ValueError(f"Unsupported file format: {extension}")

    return {
        "filename": Path(file_path).name,
        "filetype": extension,
        "text": text,
    }