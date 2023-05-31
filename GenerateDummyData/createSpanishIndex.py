from elasticsearch import Elasticsearch
from dotenv import dotenv_values

# Load the environment variables
env_vars = dotenv_values('./GenerateDummyData/.env')

api_key = env_vars['API_KEY']
cloud_id = env_vars['CLOUD_ID']

# Create a connection to Elasticsearch
es = Elasticsearch(api_key=api_key, cloud_id=cloud_id)

# Specify the index name
index_name = 'autos'

def createIndex(index_name):
    # Define the index settings with BM25 similarity
    settings = {
        "index": {
            "similarity": {
                "default": {
                    "type": "BM25"
                }
            },
            "analysis": {
                "analyzer": {
                    "spanish_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "snowball_spanish", "stop_spanish"]
                    }
                },
                "filter": {
                    "stop_spanish": {
                        "type": "stop",
                        "stopwords": "_spanish_"
                    },
                    "snowball_spanish": {
                        "type": "snowball",
                        "language": "Spanish"
                    }
                }
            }
        }
    }

    # Define the index mappings
    mappings = {
        "properties": {
            "your_field_name": {
                "type": "text",
                "analyzer": "spanish_analyzer"
            }
        }
    }

    # Create the index with settings and mappings
    es.indices.create(index=index_name, body={"settings": settings, "mappings": mappings})

def queryIndex(index_name, prompt):
    # Define the query
    query = {
        "query": {
            "match": {
                "content": prompt
            }
        },
        "size": 20  # Retrieve at least 20 results
    }

    # Query the index
    results = es.search(index=index_name, body=query)

    # Return the results
    return results

print(queryIndex('autos', 'Auto familiar con calefacción y aire acondicionado.'))