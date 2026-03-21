<div align="center">

```
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
  ║       🌐  T H E   I N T E R N E T   R E S E A R C H E R                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

**An AI-powered research agent that searches the web, understands context, and delivers structured reports — then lets you chat with the findings.**

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-Compatible-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Tavily](https://img.shields.io/badge/Tavily-Web_Search-00B4D8?style=for-the-badge)](https://tavily.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What Is This?

**The Internet Researcher** is a fully agentic research tool built on **LangGraph** that autonomously:

1. 🔍 **Searches** the web for your topic using Tavily
2. 🧩 **Embeds** the results into a vector store (ChromaDB)
3. 📝 **Generates** a structured research report via an LLM
4. 💬 **Lets you chat** with the report using a follow-up Q&A agent

All wrapped in a clean **Streamlit** UI with support for both **local Ollama models** and **OpenAI's cloud models**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌐 **Live Web Search** | Powered by Tavily — fetches fresh, real-time results |
| 🗄️ **Semantic Retrieval** | ChromaDB vector store with similarity search |
| 🤖 **Dual Model Support** | Run locally with Ollama OR use OpenAI cloud models |
| 📑 **Auto Report Generation** | LLM drafts a clean, structured report from retrieved data |
| 💬 **Chat with Your Research** | Follow-up Q&A agent grounded in your report |
| 🧠 **Persistent Memory** | LangGraph `InMemorySaver` keeps context across turns |
| 🖥️ **Streamlit UI** | Clean sidebar config, live status updates, chat interface |

---

## 🏗️ Architecture

```
User Input (Topic)
       │
       ▼
┌──────────────┐
│  web_search  │  ◄── Tavily API (real-time web results)
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    embed     │  ◄── ChromaDB + Ollama/OpenAI Embeddings
└──────┬───────┘       (similarity search, top-k retrieval)
       │
       ▼
┌──────────────┐
│ final_output │  ◄── Ollama (local) or OpenAI (cloud) LLM
└──────┬───────┘
       │
       ▼
  📑 Research Report
       │
       ▼
┌──────────────┐
│  Chat Agent  │  ◄── Grounded Q&A on the report
└──────────────┘
```

> Built with **LangGraph StateGraph** — each step is a typed node with clean state transitions.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed (for local models)
- A [Tavily API key](https://tavily.com) (free tier available)
- *(Optional)* An [OpenAI API key](https://platform.openai.com/api-keys) for cloud models

---

### 1. Clone the Repository

```bash
git clone https://github.com/Katta-Nitish/internet-researcher-agent.git
cd the-internet-researcher
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Pull Local Models (Ollama only)

```bash
ollama pull qwen3:4b           # Chat model
ollama pull nomic-embed-text   # Embedding model
```

### 4. Run the App

```bash
streamlit run The_Internet_Researcher.py
```

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-community
langchain-ollama
langchain-openai
langgraph
tavily-python
chromadb
```

> Save this as `requirements.txt` and run `pip install -r requirements.txt`.

---

## ⚙️ Configuration

All configuration is done through the **sidebar** in the app — no `.env` file needed.

### 🖥️ Local Mode (Ollama)

| Setting | Default | Description |
|---|---|---|
| Provider | `Local (Ollama)` | Uses locally running Ollama models |
| Chat Model | `qwen3:4b` | Any Ollama-compatible chat model |
| Embed Model | `nomic-embed-text` | Any Ollama-compatible embedding model |
| Tavily API Key | *(required)* | For web search |

### ☁️ Cloud Mode (OpenAI)

| Setting | Options | Description |
|---|---|---|
| Provider | `OpenAI` | Uses OpenAI API |
| Chat Model | `gpt-4o`, `gpt-4o-mini`, `gpt-4-turbo`, `gpt-3.5-turbo` | Cloud LLM |
| Embed Model | `text-embedding-3-small`, `text-embedding-3-large`, `text-embedding-ada-002` | Cloud embeddings |
| OpenAI API Key | *(required)* | Your `sk-...` key |
| Tavily API Key | *(required)* | For web search |


---

## 🔄 How It Works — Step by Step

```
1. 📝  You enter a research topic in the text input

2. 🌐  The app queries Tavily's Search API for live web results

3. 🧩  Results are chunked and embedded into ChromaDB
        using your chosen embedding model (local or cloud)

4. 🔎  A similarity search retrieves the top-5 most relevant chunks

5. 🤖  The LLM (Ollama or OpenAI) drafts a structured report
        from the retrieved context

6. 💬  A chat agent is initialized, grounded in your report,
        so you can ask follow-up questions
```

---

## 📁 Project Structure

```
the-internet-researcher/
│
├── The_Internet_Researcher.py   # Main application
├── i1.png                       # App logo/image
├── requirements.txt             # Python dependencies
└── README.md                    # You are here
```

---

## 🛠️ Built With

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — Agentic workflow orchestration
- **[LangChain](https://langchain.com)** — LLM tooling and agent framework
- **[Streamlit](https://streamlit.io)** — Web UI
- **[Tavily](https://tavily.com)** — Real-time web search API
- **[ChromaDB](https://trychroma.com)** — Local vector store
- **[Ollama](https://ollama.com)** — Local LLM inference
- **[OpenAI](https://openai.com)** — Cloud LLM & embeddings

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 🙋 FAQ

**Q: Can I use models other than OpenAI for cloud inference?**  
A: Currently OpenAI is supported as the cloud provider. You can extend `get_llm()` to add other providers like Anthropic, Groq, or Mistral using their respective LangChain integrations.

**Q: Is my API key stored anywhere?**  
A: No. API keys are entered in the Streamlit sidebar and exist only in your browser session. They are never written to disk.

**Q: The app crashes after running multiple searches — why?**  
A: ChromaDB creates a new in-memory collection per search. For heavy usage, consider persisting the vector store to disk by passing a `persist_directory` to `Chroma.from_texts()`.

---

<div align="center">

Made with ❤️ and a lot of ☕

⭐ **If you found this useful, give it a star!** ⭐

</div>
