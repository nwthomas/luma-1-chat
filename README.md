# LUMA 1 CHAT

This repository contains server code for the [Luma-1](https://github.com/joebritt/luma1) drum machine PDF documentation, enabling the ability to chat against it in real time.

## Table of Contents

- [Environment Variables](#environment-variables)
- [Doing Embeddings](#doing-embeddings)
- [Running the Server With Docker](#running-the-server-with-docker)
- [Running the Server Without Docker](#running-the-server-without-docker)
- [Sending Requests](#sending-requests)

## Environment Variables

All functionality of this server requires:

1. An OpenAI API key (model access)
2. A Pinecone API key (vector store access)

Start by going to [Pinecone](https://app.pinecone.io) to create a new account. Create a new index with the name of `luma-1-index` and a dimension of `1536`. Next, create a new API key in Pinecone and then create an `.env` file at the root of this project with the following environment variable in it:

```bash
PINECONE_API_KEY="<api key here>"
```

Next, go to OpenAI's developer dashboard and get an API key. Put this in your `.env` file as well like this:

```bash
OPENAI_API_KEY="<api key here>"
```

## Doing Embeddings

Before you can chat against the document, you'll need to embed it in a vector store. Assuming that you've done the [Environment Variables](#environment-variables) section above, you can run the following command to embed the PDF document data:

```bash
make embed
```

## Running the Server With Docker

> NOTE: This section requires that you have [Docker](https://www.docker.com/) installed locally. Also, make sure you've completed the [Environment Variables](#environment-variables) section above before continuing on.

Run the following commands to build a new docker container locally:

```bash
make build
```

Once that's done, run the docker container with this command:

```bash
make run-docker
```

You should now be able to directly make requests against the server:

## Running the Server Without Docker

> Make sure you've completed the [Environment Variables](#environment-variables) section above before continuing on.

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

## Sending Requests

Once you have the server running, you can send requests to `http://localhost:3200/v1/chat` like this:

Request:

```json
{
  "prompt": "How can I add new sounds?"
}
```

Response:

```json
{
  "result": "To add new sounds to the Luma-1, you can use the Load Voice Bank command to load downloaded sounds onto the device via its internal SD card or the Luma-1 Web Application. You can put your sample files into specific folders for different drum sounds, ensuring they are in u-law format and no larger than 32KB. You can also build a custom Voice Bank from EPROM and SysEx sounds and save it to the SD card. To load your new Drum Bank, navigate through the menu and select the folder containing your loaded sounds. The Luma-1 will process the new samples and return to normal drum machine operation."
}
```
