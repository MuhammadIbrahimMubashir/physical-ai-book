from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# ---------------------------
# App setup
# ---------------------------
app = FastAPI(title="Physical AI Book RAG API")

# ---------------------------
# Config
# ---------------------------
INDEX_PATH = "faiss_index"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3

# ---------------------------
# Load everything once
# ---------------------------
model = SentenceTransformer(MODEL_NAME)
index = faiss.read_index(f"{INDEX_PATH}/index.faiss")

with open(f"{INDEX_PATH}/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

# ---------------------------
# Request model
# ---------------------------
class Question(BaseModel):
    question: str

# ---------------------------
# Routes
# ---------------------------
@app.get("/")
def root():
    return {"status": "RAG backend running"}

@app.post("/ask")
def ask_question(q: Question):
    embedding = model.encode([q.question])
    _, indices = index.search(embedding, TOP_K)

    answers = [chunks[i] for i in indices[0]]

    return {
        "question": q.question,
        "answers": answers
    }
