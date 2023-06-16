# Update the index of the elastic search engine
import elasticsearch
from elasticsearch import Elasticsearch
import json
import ast
import random
from dotenv import load_dotenv

env_vars = load_dotenv('./.env')

#cloud_id = 'swivelElasticTest:dXMtZWFzdDQuZ2NwLmVsYXN0aWMtY2xvdWQuY29tOjQ0MyQ1YjA4ZGYyMmE4ZTQ0ZDVjODhiNTI2ODY2N2EzOGI5ZCQ5NWYyNzJiNzg0N2E0NDlkYmY2YTYxY2ExNDAyMDU3Mw=='
cloud_id = env_vars['CLOUD_ID']

# Api Key for autos
api_key = env_vars['API_KEY_AUTOS']

# Api Key for autos_dev
# api_key = env_vars['API_KEY_AUTOS_DEV']

client = Elasticsearch(cloud_id = cloud_id, api_key=api_key)

# Lista de agencias
agencia_id = ['648820cccca96c9555319083', '648830e212d77e08c65d349f', '64883a6dce5aad58d77b287c']

# Indice autos
index_name = "autos"
# Indice autos_dev
# index_name = 'autos_dev'

count = 0

# llamar documentos de la base de datos y actualizarlos 
for doc in client.search(index=index_name, size=1000)['hits']['hits']:
    selected_agencia = random.choice(agencia_id)

    # Condiciones para cada agencia
    if selected_agencia == '648820cccca96c9555319083':
        gerente_id = '648821a4cca96c9555319086'
        direccion_agencia = 'Insurgentes Sur No. 1070 y Zona Metropolitana, Insurgentes San Borja, Ciudad de México, CDMX'
        nombre_agencia = 'Mercedes Benz'
        estado_agencia = 'CDMX'
        coordenadas_agencia = '19.3813035,-99.1760988'
        municipio_agencia = 'Benito Juárez'
        grupo_automotriz_id = '6488190fcca96c9555319079'
        nombre_grupo_automotriz = 'Grupo KASA'
    elif selected_agencia == '648830e212d77e08c65d349f':
        gerente_id = '6488326e12d77e08c65d34a3'
        direccion_agencia = 'Antonio Dovali Jaime No.115, Santa Fe, Lomas de Sta Fé, Álvaro Obregón, 01210 Ciudad de México, CDMX'
        nombre_agencia = 'Nissan Santa Fe'
        estado_agencia = 'CDMX'
        coordenadas_agencia = '19.3662561,-99.25929'
        municipio_agencia = 'Cuajimalpa de Morelos'
        grupo_automotriz_id = '6488190fcca96c9555319079'
        nombre_grupo_automotriz = 'Grupo KASA'
    else:
        selected_agencia = '64883a6dce5aad58d77b287c'
        gerente_id = '64883af4ce5aad58d77b287f'
        direccion_agencia = 'Juan Salvador Agraz No. 50, Lomas de Santa Fe, Contadero, Cuajimalpa de Morelos, 05348 Ciudad de México, CDMX'
        nombre_agencia = 'Honda Santa Fe'
        estado_agencia = 'CDMX'
        coordenadas_agencia = '19.3595155,-99.2806805'
        municipio_agencia = 'Cuajimalpa de Morelos'
        grupo_automotriz_id = '64883904ce5aad58d77b2874'
        nombre_grupo_automotriz = 'Calabria Automotriz'

    # Update the document
    doc_id = doc['_id']
    updated_doc = {
        'agencia_id': selected_agencia,
        'gerente_id': gerente_id,
        'direccion_agencia': direccion_agencia,
        'nombre_agencia': nombre_agencia,
        'estado_agencia': estado_agencia,
        'coordenadas_agencia': coordenadas_agencia,
        'municipio_agencia': municipio_agencia,
        'grupo_automotriz_id': grupo_automotriz_id,
        'nombre_grupo_automotriz': nombre_grupo_automotriz
    }

    client.update(index=index_name, id=doc_id, body={'doc': updated_doc})

    # Contador de documentos actualizados
    count += 1  # Increment counter
    print(f"Updated document {count}")

print("Index updated successfully.")