import pandas as pd
from elasticsearch import Elasticsearch
import json

# Connecting to Elasticsearch
client = Elasticsearch(cloud_id="", http_auth=('', ""))

# Reading the CSV file with explicit encoding
df = pd.read_csv('./GenerateDummyData/conjunto32.csv')

# Converting the dataframe to a dictionary
data = df.to_dict(orient='records')

# Save the data as a JSON file
data_json = json.dumps(data, indent=4, ensure_ascii=False)

# Save the json data to a file with explicit encoding
with open('./GenerateDummyData/conjunto32.json', 'w', encoding='utf-8') as f:
    f.write(data_json)
