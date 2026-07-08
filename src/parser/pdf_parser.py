import pdfplumber
from pathlib import Path


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract text from a PDF resume.

    Args:
        file_path (str): Path to the PDF file.

    Returns:
        str: Extracted text.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the PDF cannot be read.
    """

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extracted_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_text += page.extract_text() or ""

        return extracted_text.strip()

    except Exception as e:
        raise ValueError(f"Error reading PDF: {e}")