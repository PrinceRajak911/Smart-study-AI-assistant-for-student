# src/app.py
import streamlit as st
from agent import explain_topic, summarize_text, create_quiz, make_notes
from utils import extract_text_from_pdf

st.set_page_config(page_title="Smart Study Assistant", layout="centered")
st.title("Smart Study Assistant — Gemini (Demo)")

mode = st.selectbox("Choose action", ["Explain Topic", "Summarize Text", "Create Quiz", "Make Notes", "Upload PDF"])

if mode == "Explain Topic":
    topic = st.text_input("Enter topic (e.g., 'Backpropagation')")
    level = st.selectbox("Student level", ["middle-school", "highschool", "undergraduate", "graduate"], index=1)
    if st.button("Explain") and topic.strip():
        with st.spinner("Generating explanation..."):
            out = explain_topic(topic, level=level)
        st.markdown(out)

elif mode == "Summarize Text":
    text = st.text_area("Paste text here (or upload PDF via Upload PDF)")
    num = st.slider("Max bullet points", 3, 12, 6)
    if st.button("Summarize") and text.strip():
        with st.spinner("Summarizing..."):
            out = summarize_text(text, max_sentences=num)
        st.markdown(out)

elif mode == "Create Quiz":
    topic = st.text_input("Enter topic for quiz")
    n = st.slider("Number of questions", 5, 20, 10)
    if st.button("Create Quiz") and topic.strip():
        with st.spinner("Creating quiz..."):
            out = create_quiz(topic, num_questions=n)
        st.markdown(out)

elif mode == "Make Notes":
    text = st.text_area("Paste chapter / notes here")
    if st.button("Make Notes") and text.strip():
        with st.spinner("Creating notes..."):
            out = make_notes(text)
        st.markdown(out)

elif mode == "Upload PDF":
    uploaded = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded is not None:
        with open("tmp.pdf", "wb") as f:
            f.write(uploaded.getbuffer())
        raw = extract_text_from_pdf("tmp.pdf")
        st.markdown("*Extracted text preview (first 1000 chars):*")
        st.text(raw[:1000])
        if st.button("Summarize PDF"):
            with st.spinner("Summarizing PDF..."):
                out = summarize_text(raw, max_sentences=8)
            st.markdown(out)