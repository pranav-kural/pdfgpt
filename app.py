# configure logging
import logging
import sys
import os
from dotenv import load_dotenv

import pinecone

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
    """
    Chatbot class - create content-aware chatbot
    """
    def __init__(self):
        self.llm_predictor = None
        self.query_engine = None

    def create_index(self, document_url):
        """ 
        method to create new index - generates embeddings for the document and stores in Pinecone
        :param document_url: URL of PDF document
        """
        if not document_url:
            raise ValueError("Please provide a valid document URL")
        elif not document_url.endswith('.pdf'):
            print("######## Invalid document extension: ", document_url)
            raise ValueError("Please provide a valid PDF document URL")
        print("######## Creating index for document: ", document_url)
        q_index, self.llm_predictor, chat_service_context = create_index(document_url)
        self.query_engine = q_index.as_query_engine(service_context=chat_service_context)

    def load_index(self):
        """
        method to load index
        """
        q_index, self.llm_predictor, service_context = load_index()
        self.query_engine = q_index.as_query_engine(service_context=service_context)

    def query_index(self, query_txt):
        """
        method to query index
        :param query_txt: query text
        """
        # check if query text is provided
        if not query_txt:
            raise ValueError("Please provide a valid query text")
        # check if query engine is initialized
        if not self.query_engine:
            print("######## Query asked: ", query_txt)
            raise ValueError("Please initialize the query engine")
        # querying the index
        response = self.query_engine.query(query_txt)
        # return response
        return query_txt, response.response, self.llm_predictor.last_token_usage

        