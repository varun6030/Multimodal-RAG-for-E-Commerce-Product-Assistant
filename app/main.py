import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
import tempfile

from models.image_caption import generate_caption
from models.embeddings import get_embedding
from models.llm import generate_answer
from utils.vector_store import add_document, search

st.set_page_config(
    page_title="Multimodal RAG Product Assistant",
    layout="centered"
)

st.title("🛍️ Multimodal RAG Product Assistant")

uploaded_image = st.file_uploader(
    "Upload a product image",
    type=["jpg", "jpeg", "png"]
)

user_query = st.text_input(
    "Ask a question about the product"
)

if uploaded_image and user_query:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        tmp.write(uploaded_image.read())
        image_path = tmp.name

    with st.spinner("Analyzing image..."):
        caption = generate_caption(image_path)

    st.subheader("🔍 Image Understanding")
    st.write(caption)

    embedding = get_embedding(caption)

    add_document(
        embedding,
        {
            "description": caption,
            "category": "Unknown",
            "price": "N/A"
        }
    )

    results = search(embedding)

    with st.spinner("Generating answer..."):
        answer = generate_answer(user_query, results)

    st.subheader("🤖 AI Answer")
    st.write(answer)

else:
    st.info("⬆️ Upload an image and ask a question to begin.")
