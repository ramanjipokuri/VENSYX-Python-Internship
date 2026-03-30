import os
import pdfplumber
from pdf2image import convert_from_path
from paddleocr import PaddleOCR
from transformers import pipeline

# ---------- INIT ----------
ocr = PaddleOCR(use_angle_cls=True, lang='en')

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


# ---------- OCR FUNCTION ----------
def extract_text_from_image(image_path):
    result = ocr.ocr(image_path)
    text = ""

    for line in result:
        for word in line:
            text += word[1][0] + " "

    return text


# ---------- PDF FUNCTION ----------
def extract_text_from_pdf(pdf_path):
    text = ""

    # Try direct extraction
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"

    # If no text → scanned PDF
    if len(text.strip()) == 0:
        images = convert_from_path(pdf_path)

        for i, img in enumerate(images):
            img_path = f"temp_page_{i}.png"
            img.save(img_path)
            text += extract_text_from_image(img_path)

    return text


# ---------- CHUNKING ----------
def chunk_text(text, size=1000):
    return [text[i:i+size] for i in range(0, len(text), size)]


# ---------- SUMMARIZATION ----------
def summarize_text(text):
    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        result = summarizer(chunk, max_length=120, min_length=30)
        summaries.append(result[0]['summary_text'])

    return " ".join(summaries)


# ---------- MAIN ----------
if __name__ == "__main__":

    file_path = "sample.pdf"   # 👈 change to your file

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    print("\n--- EXTRACTED TEXT ---\n")
    print(text[:1000])   # preview

    summary = summarize_text(text)

    print("\n--- SUMMARY ---\n")
    print(summary)