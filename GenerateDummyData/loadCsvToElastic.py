import pandas as pd
from elasticsearch import Elasticsearch
import json

from dotenv import dotenv_values

# Load the environment variables
env_vars = dotenv_values('./GenerateDummyData/.env')

api_key = env_vars['API_KEY']
cloud_id = env_vars['CLOUD_ID']

# Connecting to Elasticsearch
client = Elasticsearch(api_key=api_key, cloud_id=cloud_id)

# Reading the CSV file with explicit encoding
df = pd.read_csv('./GenerateDummyData/finalScrapedExpandedDescription_20230531201457.csv')

# Converting the dataframe to a dictionary
data = df.to_dict(orient='records')

# Save the data as a JSON file
data_json = json.dumps(data, indent=4, ensure_ascii=False)

# Save the json data to a file with explicit encoding
with open('./GenerateDummyData/conjunto32.json', 'w', encoding='utf-8') as f:
    f.write(data_json)

# Specify the index name
index_name = 'autos'

# For each document in the data
for doc in data:
    # Index the document
    client.index(index=index_name, body=json.dumps(doc))