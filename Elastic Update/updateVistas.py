# Update the index of the elastic search engine
import elasticsearch
from elasticsearch import Elasticsearch
import json
import ast
import random
from dotenv import load_dotenv

env_vars = load_dotenv('./.env')

cloud_id = env_vars['CLOUD_ID']
api_key = env_vars['API_KEY_AUTOS']

client = Elasticsearch(cloud_id = cloud_id, api_key=api_key)

index_name = "autos"

# Lista para vistas de autos
random_vistas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0

#Body for vistas de autos
query = {"query": {"match_all": {}}}
response = client.search(index=index_name, body=query, size=1000)

for hit in response['hits']['hits']:
    document_id = hit['_id']
    random_value = random.choice(random_vistas) if random_vistas else None

    update_body = {
        'doc': {
            'cantidad': random_value
        }
    }

    client.update(index=index_name, id=document_id, body=update_body)
    # Contador de documentos actualizados
    count += 1  # Increment counter
    print(f"Updated document {count}")

print("Index updated successfully.")