from src.parser.pdf_parser import extract_text_from_pdf

pdf_path = "sample_data/resumes/resume.pdf"

text = extract_text_from_pdf(pdf_path)

print("=" * 80)
print(text[:2000])
print("=" * 80)