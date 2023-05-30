import openai
from dotenv import dotenv_values
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_random_exponential

# Load the CSV file
df = pd.read_csv('./GenerateDummyData/newScraped1000.csv')

# Load the environment variables
env_vars = dotenv_values('./GenerateDummyData/.env')

openai.api_key = env_vars['OPENAI_API_KEY']

# Create the function to prompt GPT-3
@retry(wait=wait_random_exponential(min=3, max=60), stop=stop_after_attempt(10)) # Retry the function if it fails
def promptGPT(prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature= 1.1,
    max_tokens= 850,
    frequency_penalty= 0.1,
    presence_penalty= 0.1
    )

    return completion.choices[0].message["content"]

# For each row in the dataframe, get the "marca", "modelo", "año", "características", "combustible", "tipo" and "transmision" columns
for index, row in df.iterrows():
    # Get the values from the columns
    marca = row['marca']
    modelo = row['modelo']
    año = str(row['año'])
    caracteristicas = row['caracteristicas']
    combustible = row['combustible']
    tipo = row['tipo_vehiculo']
    transmision = row['transmision']

    # Create the prompt
    prompt = f"Para un {marca} {modelo} {año}, sin exceder las 350 palabras, describe su mejor caso de uso, dedicado a su público más adecuado. Características: {caracteristicas}. Combustible: {combustible}. Tipo: {tipo}. Transmisión: {transmision}."

    print(f"Current index: {index}")

    # Call the function
    description = promptGPT(prompt)

    # Add the description to the dataframe
    df.loc[index, 'descripcion'] = description

# Save the dataframe to a CSV file
df.to_csv('./GenerateDummyData/newScrapedWithDescriptions.csv', index=False)


