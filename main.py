import argparse
from src.loader import DocumentLoader
from src.llm_client import OpenRouterClient
from src.chat import DocChat
from src.config import settings
import os


def run_interactive(doc_path: str):
    loader = DocumentLoader()
    try:
        # Use the new auto-detection method
        text = loader.load_document(doc_path)
    except Exception as e:
        print(f"Error loading document: {e}")
        return

    client = OpenRouterClient()
    chat = DocChat(client)

    # Show file info
    supported_exts = DocumentLoader.get_supported_extensions()
    print(f"Document loaded successfully!")
    print(f"File type: {os.path.splitext(doc_path)[1]}")
    print(f"Supported formats: {', '.join(supported_exts)}")
    print(f"Text length: {len(text)} characters")
    print("You can now ask questions. Type 'exit' to quit.")
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
    parser.add_argument('--doc', '-d', required=True, 
                       help='Path to document (.pdf, .txt, .docx, .md)')
    args = parser.parse_args()
    run_interactive(args.doc)
