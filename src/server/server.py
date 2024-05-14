#!/usr/bin/env python3

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from ..constants import *
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")

app = Flask(SERVER_NAME)

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
document_vectorstore = PineconeVectorStore(
    index_name=PINECONE_INDEX,
    embedding=embeddings
)

retriever = document_vectorstore.as_retriever()

template = PromptTemplate(
    template="{query} context: {context}, rules: Don't ever mention the existence of documents or documentation. Instead just summarize the context instead of referencing its existence.",
    input_variables=["query", "context"],
)

def get_relevant_documents(prompt):
    """Embeds a prompt and performs nearest neighbor search in a vector database via a retriever"""
    return retriever.invoke(prompt)

@app.route("/v1/chat")
def run_server():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data received"}), 400

    prompt = data.get("prompt")
    if prompt is None:
        return jsonify({"error": "Prompt key not found in JSON data"}), 400

    prompt_with_context = template.invoke(
        {
            "query": prompt,
            "context": get_relevant_documents(prompt),
        },
    )

    llm = ChatOpenAI(temperature=0.4)
    result = llm.invoke(prompt_with_context)
    if result.content is None:
        return jsonify({"error": "There was an error processing the request"}), 500

    return jsonify({"result": result.content})