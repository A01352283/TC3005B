import requests
from bs4 import BeautifulSoup
import urllib.parse

import pandas as pd

from tenacity import retry, stop_after_attempt, wait_random_exponential

# This function will get the image source from the first image that appears in the search results
@retry(wait=wait_random_exponential(min=3, max=60), stop=stop_after_attempt(10)) # Retry the function if it fails
def getCarImages(search_query):
    #Unite the search query with underscores, like this: "ford_focus"
    search_query = search_query.replace(" ", "_")

    search_url = "https://www.kavak.com/mx/seminuevos/?keyword=" + urllib.parse.quote_plus(search_query) + "&page=0"

    # Send a GET request to the search URL
    response = requests.get(search_url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Do a try catch to get the image source
    try:
        # Get the first image element that's inside a div with the class card-img
        image_element = soup.find('div', class_='card-img').find('img')
        # Get the image source from the first image element
        image_source = image_element['src']
    except:
        image_source = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.gmt-sales.com%2Fwp-content%2Fuploads%2F2015%2F10%2Fno-image-found.jpg&f=1&nofb=1&ipt=b4ddfe840b28dae8c4f2ac65ebc8b0bf59576f952b352279eb3a6fe858f24c51&ipo=images"

    # Return the image source
    return image_source

def writeImageToCarColumn():
    df = pd.read_csv('./GenerateDummyData/newScrapedWithDescriptions.csv')

    # Parse the colores column from a string to a list of dictionaries
    df['colores'] = df['colores'].apply(lambda x: eval(x))
    
    checkpoint_interval = 10 # Save the index to the checkpoint file every 10 rows
    checkpoint_file = './GenerateDummyData/checkpoint.txt' # The file where the index will be saved
    output_file = './GenerateDummyData/descriptionsImages.csv' # The file where the dataframe will be saved

    # For each row in the dataframe, get the "marca", "modelo" and "año" columns
    for index, row in df.iterrows():
        print(f"Current index: {index}")
        if index > 0 and index % checkpoint_interval == 0: # If the index is a multiple of the checkpoint interval
            with open(checkpoint_file, 'w') as checkpoint: # Open the checkpoint file
                checkpoint.write(str(index)) # Save the index to the checkpoint file
                print(f"Checkpoint saved at index {index}")

        # Get the values from the columns
        marca = row['marca']
        modelo = row['modelo']
        año = str(row['año'])

        # For each "nombre" in the "colores" column, which is a list of dictionaries, get the color name
        for color in row['colores']:
            color_name = color['nombre']

            # Replace the value in the "imagenes" key in the colores column with the image source
            color['imagenes'] = getCarImages(marca + " " + modelo + " " + año + " " + color_name)

        # Save the dataframe to a CSV file after each iteration
        df.to_csv(output_file, index=False)

# Check if there's a checkpoint file
try:
    with open('checkpoint.txt', 'r') as checkpoint: 
        last_progress = int(checkpoint.read())
        df = pd.read_csv('./GenerateDummyData/conjunto32.csv')
        df = df.iloc[last_progress:] # Get the rows from the last checkpoint
        writeImageToCarColumn()
except FileNotFoundError: # If there's no checkpoint file
    writeImageToCarColumn() # Call the function without a checkpoint
