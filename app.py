import os
import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.llama_cpp.base import LlamaCPP
from dotenv import load_dotenv
load_dotenv()

Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

llm = LlamaCPP(
    model_path="./models/Meta-Llama-3-8B-Instruct.Q2_K.gguf",
    temperature=0.7,
    max_new_tokens=512,
    context_window=4096,
    model_kwargs={"n_gpu_layers": 0, "n_batch": 128, "n_threads": 8}
)

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine(llm=llm)

st.set_page_config(page_title="RAG Chatbot - OpenAI", layout="wide")
st.title("💬 Private RAG Chatbot (OpenAI Embedding)")

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        response = query_engine.query(query)
        st.markdown(f"**Answer:**\n\n{response}")