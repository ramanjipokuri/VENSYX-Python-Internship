import streamlit as st
import pdfplumber
from pdf2image import convert_from_bytes
from paddleocr import PaddleOCR
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from PIL import Image
import tempfile

# ---------------- UI ----------------
st.set_page_config(page_title="Document Analyzer", layout="wide")
st.title("📄 AI Document Analyzer")
st.write("Upload PDF/Image → Get Summary + Key Points")

# ---------------- INIT ----------------
@st.cache_resource
def load_ocr():
    return PaddleOCR(use_angle_cls=True, lang='en')

@st.cache_resource
def load_summarizer():
    model_name = "t5-small"   # stable + lightweight

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return pipeline("summarization", model=model, tokenizer=tokenizer)

ocr = load_ocr()
summarizer = load_summarizer()

# ---------------- OCR ----------------
def extract_text_from_image(image_path):
    result = ocr.ocr(image_path)
    text = ""

    if result:
        for line in result:
            for word in line:
                text += word[1][0] + " "

    return text

# ---------------- PDF ----------------
def extract_text_from_pdf(file_bytes):
    text = ""

    try:
        with pdfplumber.open(file_bytes) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except:
        pass

    # scanned PDF fallback
    if len(text.strip()) == 0:
        images = convert_from_bytes(file_bytes.read())

        for img in images:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                img.save(tmp.name)
                text += extract_text_from_image(tmp.name)

    return text

# ---------------- CLEAN ----------------
def clean_text(text):
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    return text

# ---------------- CHUNK ----------------
def chunk_text(text, size=800):
    return [text[i:i+size] for i in range(0, len(text), size)]

# ---------------- SUMMARIZE ----------------
def summarize_text(text):
    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        try:
            result = summarizer(chunk, max_length=120, min_length=30)
            summaries.append(result[0]['summary_text'])
        except:
            continue

    return " ".join(summaries)

# ---------------- KEY POINTS ----------------
def extract_key_points(text):
    prompt = "summarize key points: " + text[:1500]

    try:
        result = summarizer(prompt, max_length=100, min_length=30)
        return result[0]['summary_text']
    except:
        return "Unable to extract key points."

# ---------------- UI ----------------
uploaded_file = st.file_uploader(
    "Upload PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    st.success("File uploaded successfully!")

    text = ""

    # -------- FILE TYPE --------
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        image = Image.open(uploaded_file)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            image.save(tmp.name)
            text = extract_text_from_image(tmp.name)

    text = clean_text(text)

    # -------- DEBUG INFO --------
    st.info(f"Extracted Text Length: {len(text)}")

    if len(text) == 0:
        st.error("❌ No text extracted. Try another file.")
    else:
        st.subheader("📌 Text Preview")
        st.write(text[:1000])

        if st.button("🚀 Analyze Document"):

            with st.spinner("Analyzing..."):

                summary = summarize_text(text)
                key_points = extract_key_points(text)

            st.subheader("🧠 Summary")
            st.write(summary if summary else "No summary generated.")

            st.subheader("🔑 Key Points")
            st.write(key_points)