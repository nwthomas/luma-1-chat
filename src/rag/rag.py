#!/usr/bin/env python3

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
from ..constants import *
from typing import List
import os

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))

def load_documents() -> List[str]:
    """Loads PDF documents to be used in embeddings in a vector store"""
    loader = DirectoryLoader("./docs", glob="*.pdf", loader_cls=PyPDFLoader)
    raw_documents = loader.load()
    return raw_documents

def get_split_documents(raw_documents):
    """Chunks PDF documents to be used in embeddings in a vector store"""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_documents = text_splitter.split_documents(raw_documents)
    return split_documents

def embed_documents() -> None:
    """Embeds chunked documents in Pinecone's vector store"""
    raw_documents = load_documents()
    split_documents = get_split_documents(raw_documents)

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    PineconeVectorStore.from_documents(
        documents=split_documents,
        embedding=embeddings,
        index_name=PINECONE_INDEX
    )