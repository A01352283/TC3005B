import pandas as pd
from elasticsearch import Elasticsearch
import json
import ast

from dotenv import dotenv_values

# Load the environment variables
env_vars = dotenv_values('./GenerateDummyData/.env')

api_key = env_vars['API_KEY_AUTOS_PRUEBA']
cloud_id = env_vars['CLOUD_ID']

# Connecting to Elasticsearch
client = Elasticsearch(api_key=api_key, cloud_id=cloud_id)

# Reading the CSV file with explicit encoding
df = pd.read_csv('./GenerateDummyData/finalScrapedExpandedDescription_20230531201457.csv')

# Read the data type of the colores column as a list
df['colores'] = df['colores'].apply(ast.literal_eval)
df['caracteristicas'] = df['caracteristicas'].apply(ast.literal_eval)
df['extras'] = df['extras'].apply(ast.literal_eval)
df['enganche'] = df['enganche'].apply(ast.literal_eval)
df['fotos_3d'] = df['fotos_3d'].apply(ast.literal_eval)
df['entrega'] = df['entrega'].apply(ast.literal_eval)

# Read the data type of the plazos column as a dictionary
df['plazos'] = df['plazos'].apply(ast.literal_eval)

# In the entrega column, where we have an array of dictionaries, read the data type of the precio values as a float
df['entrega'] = df['entrega'].apply(lambda x: [{'precio': float(d['precio'])} for d in x])


# Converting the dataframe to a dictionary
data = df.to_dict(orient='records')

# Save the data as a JSON file
data_json = json.dumps(data, indent=4, ensure_ascii=False)


# Save the json data to a file with explicit encoding
with open('./GenerateDummyData/conjunto.json', 'w', encoding='utf-8') as f:
    f.write(data_json)

# Specify the index name
index_name = 'autos_prueba'

# For each document in the data
for doc in data:
    formatted_doc = json.dumps(doc, indent=4, ensure_ascii=False)
    # Index the document
    client.index(index=index_name, body=formatted_doc)

