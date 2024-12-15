import pdfplumber
from docx import Document

def read_document(file_path, file_type):
    content = []
    if file_type == "pdf":
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    content.append(text)
    elif file_type == "docx":
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            content.append(paragraph.text)
    elif file_type == "txt":
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.readlines()
    return "\n".join(content)

def split_into_chunks(text, max_chunk_size=1000):
    sentences = text.split("\n")
    chunks = []
    current_chunk = []

    for sentence in sentences:
        if len(" ".join(current_chunk) + sentence) < max_chunk_size:
            current_chunk.append(sentence)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sentence]

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
