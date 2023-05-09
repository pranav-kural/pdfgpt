# Setup & expose pinecone

import os
import pinecone

# import parameters
from params import p_region, p_index_name

# set Pinecone API key
pinecone.init(api_key=os.getenv('PINECONE_KEY'), environment=p_region)

# get index from Pinecone
p_index = pinecone.Index(p_index_name)
