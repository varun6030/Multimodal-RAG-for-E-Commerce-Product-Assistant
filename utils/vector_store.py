import faiss
import numpy as np

DIMENSION = 384

index = faiss.IndexFlatL2(DIMENSION)
documents = []

def add_document(embedding, metadata):
    index.add(np.array([embedding]).astype("float32"))
    documents.append(metadata)

def search(embedding, k=3):
    _, indices = index.search(
        np.array([embedding]).astype("float32"), k
    )
    return [documents[i] for i in indices[0]]
