import streamlit as st
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

# Load FAISS index
try:
    index = faiss.read_index("rag-backend/faiss_index/index.faiss")
except Exception as e:
    st.error(f"FAISS index not found. Run build_index.py first. Error: {e}")
    st.stop()

# Load document mapping
try:
    with open("rag-backend/faiss_index/docs.pkl", "rb") as f:
        docs = pickle.load(f)
except Exception as e:
    st.error(f"Document mapping not found. Run build_index.py first. Error: {e}")
    st.stop()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

st.title("Physical AI Textbook Chatbot")
st.write("Ask anything about the textbook chapters (1-9).")

# Text input
question = st.text_input("Type your question:")

if question:
    # Create embedding for the question
    question_vector = model.encode([question]).astype(np.float32)

    # Search in FAISS index
    D, I = index.search(question_vector, k=1)
    doc_index = I[0][0]

    # Return the corresponding chapter/content
    answer = docs[doc_index]
    st.markdown(f"**Answer:** {answer}")
