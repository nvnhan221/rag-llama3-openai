# 🧠 RAG Chatbot with LLaMA 3 + OpenAI Embedding

This project demonstrates a private Retrieval-Augmented Generation (RAG) chatbot using:

- 🔍 OpenAI Embedding (`text-embedding-3-small`)
- 🦙 Local LLaMA 3 (via GGUF & llama.cpp)
- 💾 ChromaDB as vector store
- 🌐 Streamlit web UI
- 📁 Local ingestion of `.txt` or `.pdf`
- ✅ `.env` support for managing API keys

---

## 📦 Requirements

- Python 3.10+
- OpenAI API Key
- LLaMA 3 GGUF file (e.g., `Meta-Llama-3-8B-Instruct.Q2_K.gguf`)

---

## 🚀 Setup Instructions

### 1. Clone and prepare environment

```bash
cd rag-llama3-openai

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 2. Prepare `.env` file

Create a `.env` file in the root directory with your OpenAI API key:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### 3. Add GGUF model file

Put your LLaMA 3 model file into the `./models` folder.

Example:
```
./models/Meta-Llama-3-8B-Instruct.Q2_K.gguf
```

---

### 4. Add content to ingest

Put `.txt` or `.pdf` files into the `./data` directory.

You can start with the included example: `data/sample_programming.txt`.

---

### 5. Run ingestion (create index)

```bash
python ingest.py
```

✅ This will use OpenAI to embed your documents and store them with ChromaDB.

---

### 6. Launch the chatbot UI

```bash
streamlit run app.py
```

Then visit:
```
http://localhost:8501
```

---

## ⚙️ Tech Stack

| Component      | Library                        |
|----------------|--------------------------------|
| LLM            | LLaMA 3 via `llama.cpp` (gguf) |
| Embedding      | `openai.text-embedding-3-small`|
| Vector DB      | `chromadb`                     |
| Framework      | `llama-index`                  |
| UI             | `streamlit`                    |

---

## 💡 Tips

- ✅ Enable batching and caching in `OpenAIEmbedding` for better performance.
- 🌐 If connection issues occur, check VPN or firewall settings.
- 📚 You can add any domain-specific data (programming, finance, etc.) into `data/`.

---

## 🧼 Cleanup

To reset the index, delete the following folders:

```bash
rm -rf chroma_db storage
```

---

## 📄 License

MIT – feel free to modify and use in your own projects.