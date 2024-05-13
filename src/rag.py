from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv
from constants import *
import os

load_dotenv()

def load_documents():
    loader = DirectoryLoader("./docs", glob="*.pdf", loader_cls=PyPDFLoader)
    raw_documents = loader.load()
    return raw_documents

def get_split_documents(raw_documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_documents = text_splitter.split_documents(raw_documents)
    return split_documents

raw_documents = load_documents()
split_documents = get_split_documents(raw_documents)

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
PineconeVectorStore.from_documents(
    documents=split_documents,
    embedding=embeddings,
    index_name=PINECONE_INDEX
)