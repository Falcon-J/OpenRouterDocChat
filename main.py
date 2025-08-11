import argparse
from src.loader import DocumentLoader
from src.llm_client import OpenRouterClient
from src.chat import DocChat
from src.config import settings
import os


def run_interactive(doc_path: str):
    loader = DocumentLoader()
    try:
        if doc_path.lower().endswith('.pdf'):
            text = loader.load_pdf(doc_path)
        else:
            text = loader.load_txt(doc_path)
    except Exception as e:
        print(f"Error loading document: {e}")
        return

    client = OpenRouterClient()
    chat = DocChat(client)

    print("Document loaded. You can now ask questions. Type 'exit' to quit.")
    while True:
        q = input('\nQuestion> ').strip()
        if not q:
            continue
        if q.lower() in ('exit', 'quit'):
            break
        try:
            ans = chat.ask_with_doc(text, q)
            print('\nAnswer:\n', ans)
        except Exception as e:
            print(f"LLM error: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--doc', '-d', required=True, help='Path to document (PDF or .txt)')
    args = parser.parse_args()
    run_interactive(args.doc)
