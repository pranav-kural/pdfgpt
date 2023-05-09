# Retrieve query index


from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    LLMPredictor,
    ServiceContext
)
from llama_index.vector_stores import PineconeVectorStore
from llama_index.storage.storage_context import StorageContext
from langchain.llms import OpenAI
import pinecone

from file_utils import download_pdf, clear_documents_directory

# import parameters
from params import (
    P_SOURCE_FILE_PATH,
    P_SOURCE_DIRECTORY,
    P_INDEX_NAME,
    P_MODEL_NAME,
    P_MAX_TOKENS,
    P_TEMPERATURE
)

# method to create new index - generates embeddings for the document and stores in Pinecone
def create_index(document_url):
    """
    method to create new index - generates embeddings for the document and stores in Pinecone
    :param document_url: URL of PDF document
    """

    # download the document in the document directory
    download_pdf(url=document_url, file_path=P_SOURCE_FILE_PATH)

    # get index from Pinecone
    p_index = pinecone.Index(P_INDEX_NAME)

    # LLM Predictor
    llm_predictor = LLMPredictor(
        llm=OpenAI(temperature=P_TEMPERATURE, model_name=P_MODEL_NAME, max_tokens=P_MAX_TOKENS)
    )
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    # load documents
    documents = SimpleDirectoryReader(P_SOURCE_DIRECTORY).load_data()

    # create pincone vector store
    vector_store = PineconeVectorStore(
        pinecone_index=p_index
    )

    # attach pinecone vector store to LlamaIndex storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # query index
    q_index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)

    # print token utilization for building index
    print('Document indexing token utilization: ', llm_predictor.last_token_usage, end='\n')

    return q_index, llm_predictor

def load_index():
    """
    method to load existing index
    """
    
    # remove existing files from document directory
    clear_documents_directory()

    # get index from Pinecone
    p_index = pinecone.Index(P_INDEX_NAME)

    # LLM Predictor
    llm_predictor = LLMPredictor(
        llm=OpenAI(temperature=P_TEMPERATURE, model_name=P_MODEL_NAME, max_tokens=P_MAX_TOKENS)
    )
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    # load documents
    documents = SimpleDirectoryReader(P_SOURCE_DIRECTORY).load_data()

    # create pincone vector store
    vector_store = PineconeVectorStore(
        pinecone_index=p_index
    )

    # attach pinecone vector store to LlamaIndex storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # query index
    q_index = GPTVectorStoreIndex.from_documents(documents, storage_context=storage_context, service_context=service_context)

    # print token utilization for building index
    print('Document indexing token utilization: ', llm_predictor.last_token_usage, end='\n')

    return q_index, llm_predictor