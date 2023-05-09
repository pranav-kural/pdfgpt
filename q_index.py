# Retrieve query index
import os
from dotenv import load_dotenv

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    LLMPredictor,
    ServiceContext
)
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.llms import OpenAI

# import parameters
from params import model_name, temperature, max_tokens, documents_directory

# import pinecone index
from pinecone_index import p_index

# Load environment variables
load_dotenv()

# set Open AI API key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# LLM Predictor
llm_predictor = LLMPredictor(
    llm=OpenAI(temperature=temperature, model_name=model_name, max_tokens=max_tokens)
)
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# load documents
documents = SimpleDirectoryReader(documents_directory).load_data()

# create pincone vector store
vector_store = PineconeVectorStore(
    pinecone_index=p_index
)

# attach pinecone vector store to LlamaIndex storage context
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# query index
q_index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context)

# print token utilization for building index
print('Document indexing token utilization: ', llm_predictor.last_token_usage)