<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🌐  T H E   I N T E R N E T   R E S E A R C H E R   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

**An AI-powered research agent that searches the web, understands context, and delivers structured reports — then lets you chat with the findings.**

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/)
[![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co)
[![Tavily](https://img.shields.io/badge/Tavily-Web_Search-00B4D8?style=for-the-badge)](https://tavily.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

<br>

### 🚀 [Try the Live Demo →](https://internet-researcher-agent-nitish.streamlit.app/)

[![Live Demo](https://img.shields.io/badge/LIVE_DEMO-internet--researcher--agent-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://internet-researcher-agent-nitish.streamlit.app/)

</div>

---

## 🧠 What Is This?

**The Internet Researcher** is a fully agentic research tool built on **LangGraph** that autonomously:

1. 🔍 **Searches** the web for your topic using Tavily
2. 🧩 **Embeds** results into a ChromaDB vector store using HuggingFace embeddings (runs fully offline)
3. 📝 **Generates** a structured research report via **Gemini 2.5 Flash**
4. 💬 **Lets you chat** with the report through a grounded Q&A agent
5. 📥 **Downloads** the final report as a Markdown file

No local GPU needed. Just a free Gemini API key and you're ready to go.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌐 **Live Web Search** | Powered by Tavily — fetches fresh, real-time results |
| 🗄️ **Semantic Retrieval** | ChromaDB + `BAAI/bge-small-en-v1.5` embeddings (CPU-friendly) |
| 🤖 **Gemini 2.5 Flash** | Fast, free-tier Google LLM for report generation and chat |
| 📑 **Sourced Reports** | Every report ends with a `--- SOURCES ---` section listing all URLs |
| 📥 **Download Reports** | Export any report as a `.md` file with one click |
| 💬 **Chat with Research** | Follow-up Q&A agent fully grounded in your report |
| 🧠 **Session Memory** | LangGraph `InMemorySaver` keeps context across the conversation |
| 🧹 **Clear & Reset** | One-click session wipe to start fresh research |
| 🔐 **Secure Key Input** | API key entered via sidebar — never hardcoded |

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
│    embed     │  ◄── HuggingFace BGE Embeddings + ChromaDB
└──────┬───────┘       (top-5 similarity search)
       │
       ▼
┌──────────────┐
│ final_output │  ◄── Gemini 2.5 Flash (report + sources)
└──────┬───────┘
       │
       ▼
  📑 Research Report  ──►  📥 Download as Markdown
       │
       ▼
┌──────────────┐
│  Chat Agent  │  ◄── Gemini 2.5 Flash (grounded Q&A)
└──────────────┘
```

> Built with **LangGraph StateGraph** — each step is a typed node with clean state transitions.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A free [Gemini API key](https://aistudio.google.com/app/apikey) from Google AI Studio
- A [Tavily API key](https://tavily.com) (free tier available)

No GPU or local model installation required.

---

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/internet-researcher-agent.git
cd internet-researcher-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Secrets

Create a `.streamlit/secrets.toml` file for your Tavily key:

```toml
# .streamlit/secrets.toml
TAVILY_API_KEY = "tvly-your-key-here"
```

> Your **Gemini API key** is entered directly in the app sidebar — no config file needed.

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
langchain-huggingface
langchain-google-genai
langgraph
tavily-python
chromadb
pysqlite3-binary
sentence-transformers
```

> Save as `requirements.txt` and run `pip install -r requirements.txt`.

---

## ⚙️ Configuration

### Gemini API Key
Enter your key in the **sidebar** when the app loads. Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### Tavily API Key
Set this in `.streamlit/secrets.toml` as shown above. This keeps it secure and out of your codebase.

---

## 🔄 How It Works — Step by Step

```
1. 📝  Enter your Gemini API key in the sidebar

2. 🔍  Type a research topic and click "Start Research 💡"

3. 🌐  Tavily searches the web and returns live results

4. 🧩  Results are embedded using BAAI/bge-small-en-v1.5 (CPU)
        and stored in ChromaDB for semantic retrieval

5. 🔎  Top-5 most relevant chunks are retrieved via similarity search

6. 🤖  Gemini 2.5 Flash drafts a structured report with cited sources

7. 📥  Download the report as a Markdown file

8. 💬  Ask follow-up questions — the agent answers from your report
```

---

## 📁 Project Structure

```
internet-researcher-agent/
│
├── The_Internet_Researcher.py   # Main application
├── i1.png                       # App logo/image
├── requirements.txt             # Python dependencies
├── .streamlit/
│   └── secrets.toml             # Tavily API key (do not commit!)
└── README.md                    # You are here
```

> ⚠️ Add `.streamlit/secrets.toml` to your `.gitignore` before pushing!

```bash
echo ".streamlit/secrets.toml" >> .gitignore
```

---

## 🛠️ Built With

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — Agentic workflow orchestration
- **[LangChain](https://langchain.com)** — LLM tooling and agent framework
- **[Streamlit](https://streamlit.io)** — Web UI
- **[Tavily](https://tavily.com)** — Real-time web search API
- **[ChromaDB](https://trychroma.com)** — Local vector store
- **[HuggingFace `BAAI/bge-small-en-v1.5`](https://huggingface.co/BAAI/bge-small-en-v1.5)** — CPU-friendly embeddings
- **[Gemini 2.5 Flash](https://aistudio.google.com)** — Google's fast, free-tier LLM

---

## ☁️ Deploying to Streamlit Cloud

The app is already live at **[internet-researcher-agent-nitish.streamlit.app](https://internet-researcher-agent-nitish.streamlit.app/)**.

To deploy your own fork:

1. Push your repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Under **App settings → Secrets**, add:
   ```toml
   TAVILY_API_KEY = "tvly-your-key-here"
   ```
4. Deploy — users will enter their own Gemini API key via the sidebar

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋 FAQ

**Q: Is the Gemini API free?**  
A: Yes! Google AI Studio offers a generous free tier for Gemini 2.5 Flash. No credit card required.

**Q: Does this need a GPU?**  
A: No. The HuggingFace embedding model (`BAAI/bge-small-en-v1.5`) runs on CPU and is lightweight enough for local or cloud deployment.

**Q: Is my API key stored anywhere?**  
A: No. Your Gemini key is entered in the Streamlit sidebar and lives only in your browser session. It is never written to disk.

**Q: Can I deploy this publicly?**  
A: Yes — it's designed for Streamlit Cloud deployment. Each user provides their own Gemini key, and the Tavily key is stored securely in Streamlit secrets.

**Q: What does "Clear Session" do?**  
A: It wipes all session state (report, messages, memory) so you can start a completely fresh research session without restarting the app.

---

<div align="center">

Made with ❤️ and a lot of ☕

⭐ **If you found this useful, give it a star!** ⭐

</div>
