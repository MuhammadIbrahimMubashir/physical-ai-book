# build_index.py
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import glob

# Create folder for FAISS index if it doesn't exist
os.makedirs("rag-backend/faiss_index", exist_ok=True)

# Load all chapter files
chapter_files = sorted(glob.glob("docs/chapter-*.md"))  # adjust if file names differ
chapters = []

for file_path in chapter_files:
    with open(file_path, "r", encoding="utf-8") as f:
        chapters.append(f.read())

# Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chapters).astype("float32")

# Build FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and docs
faiss.write_index(index, "rag-backend/faiss_index/index.faiss")
with open("rag-backend/faiss_index/docs.pkl", "wb") as f:
    pickle.dump(chapters, f)

print("✅ FAISS index and docs.pkl have been created successfully!")
