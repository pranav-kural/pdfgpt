from fastapi import FastAPI

from app import Chatbot

app = FastAPI()

# global chatbot instance
chatbot = Chatbot()

@app.get("/")
async def read_root():
    return { 
        "API": "PDF-GPT",
        "To set up a new index (provide url to PDF file)": "GET /create?document_url={document_url}",
        "To load the existing index": "GET /load",
        "To query the chatbot": "GET /query?q={query}"
        }

@app.get("/create/")
async def create(document_url: str):
    print("######## Creating index for document: ", document_url)
    chatbot.create_index(document_url)
    return {
        "index": "created",
        "document_url": document_url
        }

@app.get("/load/")
async def load_index():
    chatbot.load_index()
    return {"index": "loaded"}

@app.get("/query/")
async def query(q: str):
    print("######## Query asked: ", q)
    query_txt, response, token_usage = chatbot.query_index(q)
    return {
        "query": query_txt,
        "response": response,
        "tokens_used": token_usage
        }