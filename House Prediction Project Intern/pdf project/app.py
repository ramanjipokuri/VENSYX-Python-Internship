import streamlit as st
import pdfplumber
from pdf2image import convert_from_bytes
from paddleocr import PaddleOCR
from transformers import pipeline
from PIL import Image
import tempfile

# ---------- INIT ----------
st.title("📄 Document Analyzer (PDF/Image → Summary + Key Points)")

ocr = PaddleOCR(use_angle_cls=True, lang='en')
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


# ---------- OCR ----------
def extract_text_from_image(image_path):
    result = ocr.ocr(image_path)
    text = ""

    for line in result:
        for word in line:
            text += word[1][0] + " "

    return text


# ---------- PDF ----------
def extract_text_from_pdf(file_bytes):
    text = ""

    try:
        with pdfplumber.open(file_bytes) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
    except:
        pass

    # scanned PDF
    if len(text.strip()) == 0:
        images = convert_from_bytes(file_bytes.read())

        for img in images:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                img.save(tmp.name)
                text += extract_text_from_image(tmp.name)

    return text


# ---------- CHUNK ----------
def chunk_text(text, size=1000):
    return [text[i:i+size] for i in range(0, len(text), size)]


# ---------- SUMMARIZE ----------
def summarize_text(text):
    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        result = summarizer(chunk, max_length=120, min_length=30)
        summaries.append(result[0]['summary_text'])

    return " ".join(summaries)


# ---------- KEY POINTS ----------
def extract_key_points(text):
    prompt = f"Extract key points from this text:\n{text[:2000]}"
    result = summarizer(prompt, max_length=100, min_length=30)
    return result[0]['summary_text']


# ---------- UI ----------
uploaded_file = st.file_uploader("Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:

    st.success("File uploaded successfully!")

    # Detect type
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        image = Image.open(uploaded_file)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            image.save(tmp.name)
            text = extract_text_from_image(tmp.name)

    text = " ".join(text.split())

    st.subheader("📌 Extracted Text (Preview)")
    st.write(text[:1000])

    if st.button("Analyze Document"):

        summary = summarize_text(text)
        key_points = extract_key_points(text)

        st.subheader("🧠 Summary")
        st.write(summary)

        st.subheader("🔑 Key Points")
        st.write(key_points)