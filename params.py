# Parameters

## Pinecone
p_region = "asia-southeast1-gcp-free"
p_index_name = "gptindex"

# if creating index, set to True, if False, will load index from disk
creating_index = False
# index file name, if creating index, will save index to disk
# if loading index, will load index from this file
index_file_name = 'data/indices/ai_benefit_text_index_gpt.json'
# if creating index, location of documents to index
documents_directory = 'data/documents'
# specify the model to use
model_name = 'gpt-3.5-turbo'
max_tokens = 2096
temperature = 0.6
# queries to make
queries = [
  'What are benefits of IDPS systems built using AI?',
  'How can AI help in preventing malicious attacks?',
  ]