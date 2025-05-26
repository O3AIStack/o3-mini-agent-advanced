# O3 Mini Agent Advanced

This repository provides a modular, session-aware AI agent template built for the O3 Mini Stack. It supports multi-step reasoning, memory tracking, token usage logging, and production deployment via GitHub Actions and Azure Container Apps.

## 🔧 Features

- 🧠 Session-based memory (in-memory, extendable)
- 🔗 Multi-step agent flow (e.g., Summarizer → Evaluator)
- 📜 Prompt templates for structured reasoning
- 🧮 Token usage logging via `tiktoken`
- ☁️ Azure-ready Docker deployment with CI/CD
- 🔐 OpenAI v1 SDK integration (GPT-3.5 or GPT-4)

## 📦 Ideal For

- Agent builders using O3 Mini (Low/Medium)
- AI DevOps teams deploying reasoning workflows
- Developers transitioning from stateless prompts to structured agents

## 🌐 Learn More

For deployment patterns, agent logic, and tutorials, visit [O3AIStack.com](https://o3aistack.com).

## 📁 Project Structure

```bash
o3-mini-agent-advanced/
├── src/
│   ├── main.py              # FastAPI API entry point
│   ├── memory.py            # Session memory layer
│   ├── logic/
│   │   ├── summarize.py     # Step 1: Summarization agent
│   │   └── evaluator.py     # Step 2: Evaluation agent
│   └── utils.py             # Token tools and prompt loader
├── prompts/
│   ├── summarizer.txt
│   └── evaluator.txt
├── .github/workflows/
│   └── deploy.yml           # GitHub CI/CD for Azure
├── requirements.txt
├── Dockerfile
└── README.md



