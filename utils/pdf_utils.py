import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    """Extract text from a PDF file."""
    text = ""
    with open(pdf_file_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text
