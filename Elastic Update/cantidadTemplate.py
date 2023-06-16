from elasticsearch import Elasticsearch
import random

# Connect to Elasticsearch
es = Elasticsearch('http://localhost:9200')

# Define your index
index_name = 'your_index_name'

# Define the list of random values
random_values = ['value1', 'value2', 'value3', 'value4', 'value5']

# Retrieve all documents from the index
query = {"query": {"match_all": {}}}
response = es.search(index=index_name, body=query, size=10000)  # Increase the size if needed

# Update each document with a random value
for hit in response['hits']['hits']:
    document_id = hit['_id']
    random_value = random.choice(random_values)
    
    update_body = {
        'doc': {
            'your_field_name': random_value 
        }
    }
    
    es.update(index=index_name, id=document_id, body=update_body)

print('All documents updated successfully.')
