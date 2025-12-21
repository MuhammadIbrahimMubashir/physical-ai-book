import streamlit as st
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

# -------------------------------
# CONFIG
# -------------------------------
st.set_page_config(page_title="Physical AI Textbook Chatbot", page_icon="🤖", layout="wide")

# -------------------------------
# LOAD FAISS INDEX AND DOCUMENTS
# -------------------------------
@st.cache_data(show_spinner=True)
def load_index():
    """Load the FAISS index and corresponding documents."""
    try:
        # Load FAISS index
        with open("faiss_index/index.pkl", "rb") as f:
            index = pickle.load(f)
        # Load documents mapping
        with open("faiss_index/file_names.pkl", "rb") as f:
            file_names = pickle.load(f)
        return index, file_names
    except Exception as e:
        st.error("FAISS index or documents not found. Run build_index.py first.")
        return None, None

index, file_names = load_index()

# -------------------------------
# EMBEDDING MODEL
# -------------------------------
@st.cache_resource
def load_model():
    """Load the embedding model once."""
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Physical AI Textbook Chatbot")
st.sidebar.info(
    """
    Ask anything about the textbook chapters (1-9).  
    Powered by local FAISS index and embeddings.  
    """
)

# -------------------------------
# CHATBOT INTERFACE
# -------------------------------
st.header("Physical AI Textbook Chatbot")
st.write("Ask anything about the textbook!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Get user question
question = st.text_input("Type your question:", key="user_question")

# -------------------------------
# PROCESS QUESTION
# -------------------------------
if st.button("Ask", key="ask_button"):
    if not question:
        st.warning("Please type a question!")
    elif index is None:
        st.error("Index not loaded. Please run build_index.py first.")
    else:
        # Convert question to embedding
        question_vector = model.encode([question])
        
        # Search FAISS index
        D, I = index.search(question_vector, k=1)
        doc_idx = I[0][0]
        answer_doc = file_names[doc_idx]

        # Save history
        st.session_state.history.append((question, answer_doc))

# -------------------------------
# DISPLAY CHAT HISTORY
# -------------------------------
for i, (q, a) in enumerate(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Answer:** {a}")
    st.markdown("---")
