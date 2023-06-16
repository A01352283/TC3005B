from elasticsearch import Elasticsearch
import random

# Establish a connection to Elastic Cloud
cloud_id = 'your_cloud_id'
username = 'your_username'
password = 'your_password'
es = Elasticsearch(cloud_id=cloud_id, http_auth=(username, password))

# List of strings to choose from
strings = ['string1', 'string2', 'string3']

# Update all documents in the index
index_name = 'your_index_name'

count = 0  # Initialize counter

for doc in es.search(index=index_name, size=1000)['hits']['hits']:
    # Select a random string from the list
    selected_string = random.choice(strings)

    # Fields dependent on the selected string
    if selected_string == 'string1':
        field1 = 'value1'
        field2 = 'value2'
    elif selected_string == 'string2':
        field1 = 'value3'
        field2 = 'value4'
    else:
        field1 = 'value5'
        field2 = 'value6'

    # Update the document
    doc_id = doc['_id']
    updated_doc = {
        'field1': field1,
        'field2': field2
    }

    es.update(index=index_name, id=doc_id, body={'doc': updated_doc})

    count += 1  # Increment counter
    print(f"Updated document {count}")

print("Update process completed")


