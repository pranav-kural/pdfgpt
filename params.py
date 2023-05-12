# Parameters

# Pinecone
P_REGION = "asia-southeast1-gcp-free"
P_INDEX_NAME = "gptindex"
# location of documents to index
P_SOURCE_DIRECTORY = "data/documents/"
P_SOURCE_FILE_PATH = "data/documents/source.pdf"
P_DUMMY_FILE_PATH = "data/documents/empty.txt"
# specify the model to use
P_EMBEDDING_MODEL = "gpt-3.5-turbo"
P_CHAT_MODEL = "gpt-3.5-turbo"
P_CHAT_MAX_TOKENS = 2096
P_CHAT_TEMPERATURE = 0.6
P_EMBEDDING_MAX_TOKENS = 2096
P_EMBEDDING_TEMPERATURE = 0.6

# link to sample PDF file
P_PDF_FILE = "https://www.pkural.ca/SOP-for-Quality-Improvement.pdf"