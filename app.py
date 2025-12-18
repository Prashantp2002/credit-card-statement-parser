import streamlit as st
import tempfile

from utils.pdf_reader import extract_text
from utils.issuer_detector import detect_issuer

from parsers import hdfc, icici, sbi, axis, citibank,generic

PARSERS = {
    "HDFC": hdfc,
    "GENERIC": generic,
    "ICICI": icici,
    "SBI": sbi,
    "Axis": axis,
    "Citibank": citibank
}

st.set_page_config(page_title="Credit Card Statement Parser")
st.title("📄 Credit Card Statement Parser")

uploaded_file = st.file_uploader(
    "Upload Credit Card Statement PDF",
    type=["pdf"]
)

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    try:
        text = extract_text(pdf_path)
        #st.text(text[:500])

        issuer = detect_issuer(text)

        if issuer == "Unknown":
            st.error("Unsupported or unknown credit card issuer.")
        else:
            result = PARSERS[issuer].parse(text)
            st.success(f"Issuer Detected: {issuer}")
            st.json(result)

    except Exception as e:
        st.error(f"Failed to parse PDF: {e}")
