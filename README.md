# Multimodal RAG for E-Commerce Product Assistant

A fully local, free, multimodal AI application that:
- Understands product images
- Retrieves similar products using vector search
- Answers user questions using a local LLM (Ollama)

## Tech Stack
- Python
- Streamlit
- BLIP (image captioning)
- Sentence-Transformers
- FAISS
- Ollama (Mistral)

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app/main.py
