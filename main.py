# configure logging
import logging
import sys
import os
from dotenv import load_dotenv

import pinecone

# import parameters
from params import P_REGION
from q_index import create_index, load_index

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# Load environment variables
load_dotenv()

# set Open AI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# set Pinecone API key
pinecone.init(api_key=os.getenv('PINECONE_KEY'), environment=P_REGION)

# Psuedo

# Part 0
# - User provides: document URL, query

# Part I
# - URL of PDF document
# - load and download the document in the DOCUMENT_DIRECTORY
# - create embeddings, store vector store in Pinecone, and generate the query index

# Part II
# - generate embeddings for user's query
# - extract relevant context data from query_index
# - query GPT (with content injected) and obtain the response for user

class Chatbot:
    def __init__(self):
        self.q_index = None
        self.llm_predictor = None
        self.query_engine = None

    def create_index(self, document_url):
        self.q_index, self.llm_predictor = create_index(document_url)
        self.query_engine = self.q_index.as_query_engine()

    def load_index(self):
        self.q_index, self.llm_predictor = load_index()
        self.query_engine = self.q_index.as_query_engine()

    def query_index(self, query_txt):
        # querying the index
        response = self.query_engine.query(query_txt)
        print(f'Query: {query_txt}')
        # display response
        print(response.response)

        print('Tokens used for last query: ', self.llm_predictor.last_token_usage)