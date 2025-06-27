import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from chromadb import PersistentClient
from dotenv import load_dotenv
load_dotenv()

# Cần set biến môi trường OPENAI_API_KEY trước khi chạy!
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

documents = SimpleDirectoryReader(input_dir="./data").load_data()

client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("rag_docs")
vector_store = ChromaVectorStore(chroma_collection=collection, client=client)

index = VectorStoreIndex.from_documents(documents, vector_store=vector_store)
index.storage_context.persist(persist_dir="./storage")
print("✅ Ingest completed with OpenAI embedding.")