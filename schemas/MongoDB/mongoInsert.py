import pymongo
import pandas as pd
import random
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://a01352283:FLt9fVo6fdlecHmn@cluster0.o397qxb.mongodb.net/?retryWrites=true&w=majority")
db = client.AppDB

# Automovil

def insert_random_automovil(numberOfCars):
    # Insert a random number of cars into the collection
    for i in range(numberOfCars):
        # Make a set object id for agencia and fotografias
        agencia_id = ObjectId()
        fotografias_id = ObjectId()

        #Make a random pair of marca and modelo from Ford, Nissan and Toyota with actual models and brands
        marca = random.choice(["Ford", "Nissan", "Toyota"])
        modelo = ""
        if marca == "Ford":
            modelo = random.choice(["Focus", "Fiesta", "Mustang", "Ranger", "F-150"])
        elif marca == "Nissan":
            modelo = random.choice(["Versa", "Sentra", "March", "Kicks", "X-Trail"])
        elif marca == "Toyota":
            modelo = random.choice(["Corolla", "Yaris", "Prius", "Camry", "Rav4"])

        # Randomize the price between 100000 and 1000000
        precio = random.randint(100000, 1000000)

        # Randomize the year between 2010 and 2020
        año = random.randint(2010, 2020)

        # Randomize the color between 5 colors (Rojo, Azul, Verde, Negro, Blanco)
        color = random.choice(["Rojo", "Azul", "Verde", "Negro", "Blanco"])

        # Randomize combustible between Premium and Magna
        combustible = random.choice(["Magna", "Premium"])

        # Randomize motor between Manual and Automatico
        motor = random.choice(["Manual", "Automatico"])   

        db.automovil.insert_one({
            "marca": marca,
            "modelo": modelo,
            "año": año,
            "precio": precio,
            "color": color,
            "combustible": combustible,
            "disponibilidad": True,
            "motor": motor,
            "agencia": agencia_id,
            "tipo_vehiculo": "Sedan",
            "fotografias": fotografias_id
        })

        print(f"{i} documents inserted")

def randomize_automovil():
    # Update each entry and randomize the price with values between 100000 and 1000000 and availability using mongo update for each document
    cursor = db.automovil.find({})
    for document in cursor:
        db.automovil.update_one({"_id": document["_id"]}, {"$set": {"precio": random.randint(100000, 1000000), "disponibilidad": random.choice([True, False])}})
        print(document)

def print_automovilDf():
    # Make a pandas dataframe with the data from the collection
    df = pd.DataFrame(list(db.automovil.find({})))
    print(df)

# Usuario Final

def insert_random_usuario_final(numberOfUsers):
    # Insert a random number of users into the collection
    for i in range(numberOfUsers):
        # Make a set object id for lista_deseos and direccion
        lista_deseos_id = ObjectId()
        direccion_id = ObjectId()

        # Randomize the name between 5 names (Juan, Pedro, Jose, Maria, Alicia)
        nombres = random.choice(["Juan", "Pedro", "Jose", "Maria", "Alicia"])

        # Randomize the last name between 5 last names (Perez, Lopez, Gomez, Hernandez, Martinez)
        apellidos = random.choice(["Perez", "Lopez", "Gomez", "Hernandez", "Martinez"])

        # Randomize the email between 5 emails (gmail, hotmail, yahoo, outlook, aol), add .com to the end
        email = "@" + random.choice(["gmail", "hotmail", "yahoo", "outlook", "aol"]) + ".com"

        # Randomize the password between 5 passwords (password1, password2, password3, password4, password5)
        contraseña = random.choice(["password1", "password2", "password3", "password4", "password5"])

        # Randomize the phone number using any 10 digit number and then make into a string
        numero_telefonico = str(random.randint(1000000000, 9999999999))

        # Randomize the user type between 2 user types (vendedor, comprador)
        tipo_usuario = random.choice(["vendedor", "comprador"])

        db.usuario_final.insert_one({
            "nombres": nombres,
            "apellidos": apellidos,
            "email": nombres+apellidos+email,
            "contraseña": contraseña,
            "numero_telefonico": numero_telefonico,
            "tipo_usuario": tipo_usuario,
            "lista_deseos_id": lista_deseos_id,
            "direccion_id": direccion_id
        })

insert_random_automovil(1)
#insert_random_usuario_final(10000)