# LUMA 1 CHAT

This repository contains server code for the [Luma-1](https://github.com/joebritt/luma1) drum machine PDF documentation, enabling the ability to chat against it in real time.

## Table of Contents

- [Embeddings](#embeddings)
- [Running the Server With Docker](#running-the-server-with-docker)
- [Running the Server Without Docker](#running-the-server-without-docker)

## Embeddings

Before you can chat against the document, you'll need to embed it in a vector store.

Start by going to [Pinecone](https://app.pinecone.io) to create a new account. Create a new index with the name of `luma-1-index` and a dimension of `1536`. Next, create a new API key in Pinecone and then create an `.env` file at the root of this project with the following environment variable in it:

```bash
PINECONE_API_KEY="<api key here>"
```

Next, go to OpenAI's developer dashboard and get an API key. Put this in your `.env` file as well like this:

```bash
OPENAI_API_KEY="<api key here>"
```

Once this is done, you can run the following command to embed the PDF document data:

```bash
make embed
```

## Running the Server With Docker

Run the following commands to fire up a new docker container loca

## Running the Server Without Docker

First, create a new virtual environment:

```bash
python3 -m venv venv
```

Next, activate it:

```bash
source /venv/bin/activate
```

Finally, go ahead and install the required dependencies with this make command:

```bash
make install
```

Once you've done this, you can run the server locally with this command:

```bash
make run
```

You'll be able to hit `http://localhost:3200/v1/chat` to ask questions against the docs.
