from . import rag
from dotenv import load_dotenv
import os

if __name__ == "__main__":
    print("Starting embeddings for Luma-1 documents")
    rag.embed_documents()
    print("Finished embeddings for Luma-1 documents")