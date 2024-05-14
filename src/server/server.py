#!/usr/bin/env python3

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from constants import *
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = Flask("luma-1")

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
    return retriever.get_relevant_documents(prompt)


@app.route("/v1/chat")
def index():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data received"}), 400

    prompt = data.get("prompt")
    if prompt is None:
        return jsonify({"error": "Prompt key not found in JSON data"}), 400

    prompt_with_context = template.invoke(
        {
            "query": user_input,
            "context": get_relevant_documents(user_input),
        },
    )

    llm = ChatOpenAI(temperature=0.4)
    result = llm.invoke(prompt_with_context)

    return jsonify({"value": result})

if __name__ == "__main__":
    app.run(port=SERVER_PORT)