# LangChain Master Class 🔗

A comprehensive LangChain tutorial repository with three real-world projects covering chains, agents, RAG, and ReAct patterns.

## Projects

### 1. Ice Breaker 🧊
An app that takes a person's name and generates a summary and conversation starters using LangChain agents and LinkedIn data.

**Key concepts:** Agents, Tools, Output Parsers, LinkedIn API integration, Flask web UI

```
ice_breaker/
├── app.py                  # Flask web application
├── ice_breaker.py          # Main LangChain logic
├── output_parsers.py       # Custom output parsers
├── agents/
│   └── linkedin_lookup.py  # LinkedIn lookup agent
├── third_parties/
│   └── linkedin.py         # LinkedIn API client
├── tools/
│   └── tools.py            # Custom LangChain tools
└── templates/
    └── index.html          # Web UI
```

### 2. Medium Analyzer 📝
Ingests Medium blog posts and enables semantic search and Q&A over the content.

**Key concepts:** Document ingestion, text splitting, vector stores, retrieval chains

```
medium-analyzer/
├── ingestion.py        # Document ingestion pipeline
├── mediumblog1.txt     # Sample blog content
└── requirements.txt
```

### 3. ReAct LangChain 🧠
Implementation of the ReAct (Reasoning + Acting) pattern using LangChain agents with streaming callbacks.

**Key concepts:** ReAct agents, callbacks, streaming output, tool usage

```
react-langchain/
├── main.py             # ReAct agent implementation
├── callbacks.py        # Streaming callback handlers
└── requirements.txt
```

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

## Setup

```bash
git clone https://github.com/nofaukost/langchain-master-class.git
cd langchain-master-class

# Choose a project
cd ice_breaker  # or medium-analyzer or react-langchain
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY=your_key_here
```

## License

MIT
