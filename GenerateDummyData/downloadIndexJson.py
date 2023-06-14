from elasticsearch import Elasticsearch
import json

from dotenv import dotenv_values

# Load the environment variables
env_vars = dotenv_values('./GenerateDummyData/.env')

api_key = env_vars['API_KEY']
cloud_id = env_vars['CLOUD_ID']

# Connecting to Elasticsearch
es = Elasticsearch(api_key=api_key, cloud_id=cloud_id)

# Define the index and search query
index_name = 'autos'
search_query = {
    "query": {
        "match_all": {}  # Example query, modify as per your requirements
    }
}

# Execute the search query
response = es.search(index=index_name, body=search_query, scroll='2m', size=1000)

# Extract the hits and scroll_id from the response
hits = response['hits']['hits']
scroll_id = response['_scroll_id']

# Prepare JSON file for writing
json_file = ',/GenerateDummyData/output.json'
with open(json_file, mode='w') as file:
    # Write the initial response to the JSON file
    file.write(json.dumps(response['hits']['hits'], indent=4, ensure_ascii=False))

# Paginate through the search results using scroll API
while len(hits) > 0:
    response = es.scroll(scroll_id=scroll_id, scroll='2m')
    hits = response['hits']['hits']

    # Append the additional hits to the JSON file
    with open(json_file, mode='a') as file:
        file.write(json.dumps(response['hits']['hits'], indent=4, ensure_ascii=False))

# Print completion message
print(f"JSON file '{json_file}' has been created.")
