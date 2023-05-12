# PDF-GPT

Query PDFs using GPT - Open AI + Pinecone (vector store) + LlamaIndex

## Usage

Easiest way would be to run the app locally by cloning the repo:

     git clone https://github.com/pranav-kural/pdfgpt.git

Then run the server using:

    uvicorn main:app --reload

## Endpoints

Using below endpoint, provide URL to the PDF file you want the API to create a vector store for. This vector store will then be stored in [Pinecone](https://www.pinecone.io/) and will be queried when queries are made to the chatbot.

    /create?document_url={document_url}

If you've already created an index, and want to load it from [Pinecone](https://www.pinecone.io/), use the `load` endpoint

    /load

To make a query and get response:

    /query?q={query text}

## How it works?

Below is a brief overview of what happens when user makes a query:

1. The query embeddings are generated
2. Vector store is searched with the query embeddings to extract closest neighbors
3. Closest neighbor embedding values are used to retrieve most relevant portion of content that relate to given query
4. Chat completion request is made to Chat model (ex, OpenAI GPT 3.5 turbo) by providing it the content related to the query as context and the query itself
5. Response returned

## Screenshots

Example screenshots:

![CDB402A4-4CAE-41FD-A027-40A3860C6F35](https://github.com/pranav-kural/pdfgpt/assets/17651852/dd1ee34b-c4e6-4556-a2d7-bc6afd621cd3)

## To-be-implemented

- Add authentication, API Key and user management to the API
- Add authentication for endpoints (including verification of API key through session id)
- Ability for users to create, save, delete and interact with multiple chatbots
