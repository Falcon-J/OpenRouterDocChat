# OpenRouter Doc Chat — MVP

Minimal, professional starter repo to upload documents, parse them, and chat with an OpenRouter LLM.

## Goals

- Load PDFs / text files
- Provide robust error handling + retry logic
- Interactive chat loop using OpenRouter-compatible Python client
- GitHub-ready: .gitignore, simple tests, CI skeleton

## Quickstart

1. Clone the repo
2. Create virtualenv and install deps
   ```bash
   python -m venv venv
   source venv/bin/activate  # windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Create `.env` with `OPENROUTER_API_KEY` and optionally `OPENROUTER_MODEL`
4. Run the app:

   ```bash
   python main.py --doc examples/sample.pdf
   ```

## Next improvements (post-MVP)

- RAG (embeddings + vector DB)
- Streamlit UI
- Dockerfile + deploy pipeline
- More tests and linting
"# OpenRouterDocChat" 
