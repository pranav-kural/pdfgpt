# configure logging
import logging
import sys

from q_index import q_index, llm_predictor

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# function to query the index and display the results
def query_index(query_txt):
    # querying the index
    query_engine = q_index.as_query_engine()
    response = query_engine.query(query_txt)
    print(f'Query: {query_txt}')
    # display response
    print(response.response)

    print('Tokens used for last query: ', llm_predictor.last_token_usage)


