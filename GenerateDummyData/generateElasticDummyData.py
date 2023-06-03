import random
import pandas as pd
from datetime import datetime

def generateRandomCar():
    # Read the csv file into a pandas dataframe
    df = pd.read_csv('./GenerateDummyData/cleanedScrapedResults.csv')
    
    #Remove the first and last character from the marca column
    df['marca'] = df['marca'].str[1:-1]
    #Remove the first and last character from the modelo column
    df['modelo'] = df['modelo'].str[1:-1]
    # Based on the cells from the combustible column, pick a random motor
    df['motor'] = [pickRandomMotor(row) for row in df['combustible']]
    # Pick a random tipo de vehiculo
    df['tipo_vehiculo'] = [pickTipoVehicle() for row in range(len(df))]
    # Pick the passengers based on the tipo de vehiculo
    df['pasajeros'] = [pickPassengers(row) for row in df['tipo_vehiculo']]
    # Set the gerente_id for all rows
    df['gerente_id'] = '646e3b245ecacccc95b27c1e'
    # Generate a random array of colors
    df['colores'] = [generateColorArray() for row in range(len(df))]
    # Generate a random array of characteristics
    df['caracteristicas'] = [pickCharacteristics() for row in range(len(df))]
    # Generate a random array of extras
    df['extras'] = [generateExtras() for row in range(len(df))]
    # Generate a random array of enganches
    df['enganche'] = [generateEnganche() for row in range(len(df))]
    # Generate a random array of plazos
    df['plazos'] = [generatePlazos() for row in range(len(df))]
    # Generate the photos for each car
    df['fotos_3d'] = [generate_dummy_links() for row in range(len(df))]
    # Fill the ficha_tecnica column with the following link: https://github.com/SFMBa01029956/TC3005B.501
    df['ficha_tecnica'] = 'https://github.com/SFMBa01029956/TC3005B.501'
    # Generate the entrega column
    df['entrega'] = [generateEntrega() for row in range(len(df))]


    df.to_csv('./GenerateDummyData/newScraped.csv', index=False)

def addIds():
    df = pd.read_csv('./GenerateDummyData/descriptionsImages.csv')

    # Set the data type of the color column to a list
    df['colores'] = df['colores'].apply(lambda x: eval(x))

    df['agencia_id'] = '6475ce431870c4941b667158'

    df['gerente_id'] = '6475d196b0304a50ba2a3113'

    # For each row, fill the fotos_3d column with the 'imagenes' field of the first dictionary in the colors column list
    df['fotos_3d'] = [[row[0]['imagenes']] for row in df['colores']]

    # Iterate through each dictionary in the colores column list
    for row in df['colores']:
        # Iterate through each dictionary in the list
        for color in row:
            # Set the 'imagenes' string inside a list
            color['imagenes'] = [color['imagenes']]
    

    df.to_csv('./GenerateDummyData/finalScraped.csv', index=False)

def pickRandomMotor(motorType):
    motors = []
    if motorType == 'Gasolina':
        motors = [
            'V6',
            'Inline-4',
            'V8',
            'V6 Turbocharged',
            'Inline-6',
            'V10',
            'Inline-5',
            'Boxer-4',
            'Inline-3',
            'V8 Twin-Turbo'
        ]
    elif motorType == 'Híbrido':
        motors = [
            'Hybrid',
            'Hybrid Electric',
            'Inline-4 Hybrid'
        ]
    elif motorType == 'electric':
        motors = [
            'Electric',
            'Electric Motor',
            'Electric Drive'
        ]
    elif motorType == 'Diesel':
        motors = [
            'Turbocharged Diesel',
            'V6 Diesel',
            'Inline-4 Diesel'
        ]

    return random.choice(motors)

def pickTipoVehicle():
    tipos_vehiculos = [
        'Sedán',
        'SUV',
        'Hatchback',
        'Familiar',
        'Coupé',
        'Camioneta',
        'Deportivo'
    ]

    return random.choice(tipos_vehiculos)

def pickPassengers(tipo_vehiculo):
    if tipo_vehiculo == 'Sedán':
        return random.randint(4, 6)
    elif tipo_vehiculo == 'SUV':
        return random.randint(4, 7)
    elif tipo_vehiculo == 'Hatchback':
        return random.randint(4, 6)
    elif tipo_vehiculo == 'Familiar':
        return random.randint(4, 7)
    elif tipo_vehiculo == 'Coupé':
        return random.randint(2, 4)
    elif tipo_vehiculo == 'Camioneta':
        return random.randint(4, 7)
    elif tipo_vehiculo == 'Deportivo':
        return random.randint(2, 4)

def generateColorArray():
    colores = pickColors(random.randint(1,4))

    return colores

def pickColors(num_colors):
    common_colors = [
        ('Blanco', '#FFFFFF'),
        ('Negro', '#000000'),
        ('Gris Claro', '#D3D3D3'),
        ('Gris Medio', '#808080'),
        ('Gris Oscuro', '#696969'),
        ('Gris Azulado', '#708090'),
        ('Plata', '#C0C0C0'),
        ('Blanco Perla', '#F8F8FF'),
        ('Blanco Nieve', '#FFFAFA'),
        ('Negro Noche', '#2F2F2F'),
        ('Negro Azabache', '#0D0D0D'),
        ('Rojo Oscuro', '#8B0000'),
        ('Azul Oscuro', '#00008B'),
        ('Marrón Oscuro', '#8B4513'),
        ('Beige', '#F5F5DC')
    ]

    colores = []


    for i in range(num_colors):
        # Extract colors and hex values into separate lists
        colors, hex_values = zip(*common_colors)
        
        # Select colors based on the distribution
        selected_color = random.sample(colors, k=1)

        # Retrieve the hex values for the selected colors
        selected_hex_values = [hex_values[colors.index(color)] for color in selected_color]

        imagenes = generate_dummy_links() # TODO take the scraped image from Kavak

        color = {'nombre': selected_color[0], 'valor_hexadecimal': selected_hex_values[0], 'imagenes': imagenes}

        colores.append(color)

    return colores

def generate_dummy_links():
    links = []
    for _ in range(random.randint(1,5)):
        random_number = random.randint(100000, 999999)
        random_number2 = random.randint(10000000000, 99999999999)
        link = f"https://http2.mlstatic.com/D_NQ_NP_{random_number}-MLM{random_number2}_022023-O.jpg"
        links.append(link)
    return links

def pickCharacteristics():
    caracteristicas_auto = [
        "Tecnología Bluetooth",
        "Aire acondicionado",
        "Frenos ABS",
        "Control de crucero",
        "Sistema de navegación",
        "Asientos de cuero",
        "Cámara de visión trasera",
        "Encendido sin llave",
        "Faros LED",
        "Sistema de sonido premium",
        "Asientos con calefacción",
        "Volante multifuncional",
        "Sensor de estacionamiento",
        "Sistema de arranque remoto",
        "Control de estabilidad",
        "Sistema de frenado de emergencia",
        "Luces automáticas",
        "Pantalla táctil",
        "Sistema de monitoreo de presión de neumáticos",
        "Asistente de mantenimiento de carril",
        "Sistema de asistencia de estacionamiento",
        "Asientos con memoria",
        "Reproductor de CD/DVD",
        "Control de tracción",
        "Sistema de reconocimiento de voz",
        "Espejos eléctricos",
        "Techo solar",
        "Asientos con masaje",
        "Conectividad USB",
        "Sistema de frenado regenerativo"
    ]

    return random.sample(caracteristicas_auto, random.randint(1,5))

def generateExtras():
    extras = [
        {
            "titulo": "Sistema de Navegación GPS",
            "precio": 9000.00,
            "descripcion": "Proporciona indicaciones de navegación precisas y actualizadas"
        },
        {
            "titulo": "Tapicería de Cuero",
            "precio": 6000.00,
            "descripcion": "Asientos de cuero de alta calidad para mayor elegancia y confort"
        },
        {
            "titulo": "Sistema de Sonido Premium",
            "precio": 7000.00,
            "descripcion": "Ofrece una experiencia de audio envolvente de alta fidelidad"
        },
        {
            "titulo": "Techo Solar Panorámico",
            "precio": 8000.00,
            "descripcion": "Amplia apertura de techo para disfrutar de la vista y la luz natural"
        },
        {
            "titulo": "Sistema de Arranque por Botón",
            "precio": 4000.00,
            "descripcion": "Permite encender el motor con solo presionar un botón"
        },
        {
            "titulo": "Control de Estabilidad Electrónico",
            "precio": 5500.00,
            "descripcion": "Mejora la estabilidad y el control del vehículo en situaciones de emergencia"
        },
        {
            "titulo": "Sistema de Frenado de Emergencia",
            "precio": 7500.00,
            "descripcion": "Aplica frenos de forma automática para evitar colisiones o reducir su impacto"
        },
        {
            "titulo": "Asientos Calefaccionados",
            "precio": 5000.00,
            "descripcion": "Proporciona calor en los asientos para mayor confort en climas fríos"
        },
        {
            "titulo": "Alerta de Cambio de Carril",
            "precio": 6000.00,
            "descripcion": "Advierte al conductor cuando se desvía involuntariamente de su carril"
        },
        {
            "titulo": "Control de Crucero Inteligente",
            "precio": 8500.00,
            "descripcion": "Mantiene una velocidad constante y segura adaptándose al tráfico"
        },
        {
            "titulo": "Sistema de Asistencia de Aparcamiento",
            "precio": 7000.00,
            "descripcion": "Facilita el estacionamiento mediante sensores y guías visuales"
        },
        {
            "titulo": "Asientos con Memoria",
            "precio": 5500.00,
            "descripcion": "Permite guardar y recuperar configuraciones personalizadas de asientos"
        },
        {
            "titulo": "Volante Forrado en Cuero",
            "precio": 3000.00,
            "descripcion": "Proporciona un agarre suave y cómodo durante la conducción"
        },
        {
            "titulo": "Control de Tracción",
            "precio": 4000.00,
            "descripcion": "Mejora la tracción y la estabilidad del vehículo en superficies resbaladizas"
        },
        {
            "titulo": "Espejos Laterales Eléctricos",
            "precio": 2500.00,
            "descripcion": "Permite ajustar los espejos exteriores de forma electrónica"
        },
        {
            "titulo": "Sistema de Frenos de Disco",
            "precio": 5000.00,
            "descripcion": "Proporciona un frenado más eficiente y seguro"
        },
        {
            "titulo": "Encendido Automático de Luces",
            "precio": 3500.00,
            "descripcion": "Activa y desactiva las luces del vehículo automáticamente según las condiciones de luz"
        },
        {
            "titulo": "Sistema de Detección de Punto Ciego",
            "precio": 7000.00,
            "descripcion": "Advierte al conductor sobre vehículos en el punto ciego"
        },
        {
            "titulo": "Sistema de Sonido Surround",
            "precio": 6000.00,
            "descripcion": "Brinda una experiencia de audio envolvente en todo el vehículo"
        },
        {
            "titulo": "Sistema de Asistencia al Estacionamiento en Paralelo",
            "precio": 8000.00,
            "descripcion": "Ayuda al conductor a estacionar el vehículo de manera precisa en espacios paralelos"
        },
        {
            "titulo": "Climatizador Automático",
            "precio": 4500.00,
            "descripcion": "Regula automáticamente la temperatura y el flujo de aire en el vehículo"
        },
        {
            "titulo": "Sistema de Aviso de Cambio de Carril",
            "precio": 6500.00,
            "descripcion": "Alerta al conductor cuando se produce un cambio de carril involuntario"
        },
        {
            "titulo": "Espejos Retrovisores con Calefacción",
            "precio": 3500.00,
            "descripcion": "Descongela y evita la formación de hielo en los espejos retrovisores"
        },
        {
            "titulo": "Sistema de Asistencia de Mantenimiento de Carril",
            "precio": 7500.00,
            "descripcion": "Ayuda a mantener el vehículo en el centro del carril de manera automática"
        },
        {
            "titulo": "Sensores de Estacionamiento Delanteros y Traseros",
            "precio": 5500.00,
            "descripcion": "Proporciona advertencias audibles y visuales para facilitar el estacionamiento"
        },
        {
            "titulo": "Sistema de Reconocimiento de Señales de Tráfico",
            "precio": 7000.00,
            "descripcion": "Detecta y muestra en el panel de instrumentos las señales de tráfico relevantes"
        },
        {
            "titulo": "Espejos Retrovisores Plegables Eléctricamente",
            "precio": 4000.00,
            "descripcion": "Permite plegar los espejos retrovisores de forma eléctrica para facilitar el estacionamiento"
        },
        {
            "titulo": "Asistente de Arranque en Pendientes",
            "precio": 3500.00,
            "descripcion": "Facilita el arranque en pendientes sin deslizamientos hacia atrás"
        },
        {
            "titulo": "Sistema de Frenado de Emergencia con Detección de Peatones",
            "precio": 10000.00,
            "descripcion": "Frena automáticamente si detecta peatones en la trayectoria del vehículo"
        },
        {
            "titulo": "Luces Delanteras LED",
            "precio": 6000.00,
            "descripcion": "Ofrece una iluminación más brillante y nítida con menor consumo de energía"
        },
        {
            "titulo": "Control de Velocidad de Crucero Adaptativo",
            "precio": 8500.00,
            "descripcion": "Ajusta automáticamente la velocidad del vehículo según la distancia con el vehículo que lo precede"
        }
    ]

    return random.sample(extras, random.randint(1,5))

def generateEnganche():
    enganches = [
        10,
        15,
        20,
        25,
        30,
        35,
        40
    ]

    # Make a list with a random number of enganches and then sort it
    finalEnganches = random.sample(enganches, random.randint(1,5))
    finalEnganches.sort()

    return finalEnganches

def generatePlazos():
    # Generate a single one decimal float between 4 and 6
    interest_rate = round(random.uniform(4, 6), 1)
    # Generate a random interest rate for each plazo based on the interest rate that rises 0.1% for each plazo
    plazo = {
        "12": interest_rate,
        "24": interest_rate + 0.1,
        "36": interest_rate + 0.2,
        "48": interest_rate + 0.4,
        "60": interest_rate + 0.6
    }

    return plazo
        
def generateEntrega():
    entrega = [
    {
      "nombre": "Domicilio",
      "precio": random.randint(3000, 15000),
      "descripcion": "Lo llevamos a la puerta de tu casa"
    },
    {
      "nombre": "Recoger en Agencia",
      "precio": 0.00,
      "descripcion": "Recoge tu auto en la agencia GRATIS"
    }
  ]
    
    return entrega

# Adds info from other columns to the description column
def updateDescription():
    df = pd.read_csv("./GenerateDummyData/finalScraped.csv")

    # Set the data type of the color column to a list
    df['colores'] = df['colores'].apply(lambda x: eval(x))

    # Set the data type of the extras column to a list
    df['extras'] = df['extras'].apply(lambda x: eval(x))
    
    # Motor, pasajeros, colores, extras are the fields to be added to the description
    # For each row, add the motor to the description following the format f"Motor: {motor}"
    df['descripcion'] = df['descripcion'] + df['motor'].apply(lambda x: f" Motor {x} ")

    # For each row, add the pasajeros to the description following the format f"Pasajeros: {pasajeros}"
    df['descripcion'] = df['descripcion'] + df['pasajeros'].apply(lambda x: f"{x} pasajeros ")

    # Get each 'nombre' value from the list of dictionaries of the 'colores' column and add the colors to the description following the format f"Colores: {colores}"
    df['descripcion'] = df['descripcion'] + df['colores'].apply(lambda x: f"Colores: {', '.join([color['nombre'] for color in x])} ")

    # Get each 'titulo' value from the list of dictionaries of the 'extras' column and add the extras to the description following the format f"Extras: {extras}"
    df['descripcion'] = df['descripcion'] + df['extras'].apply(lambda x: f"Extras: {', '.join([extra['titulo'] for extra in x])}.")

    # Save the dataframe to a csv file with the date appended at the end
    df.to_csv(f"./GenerateDummyData/finalScrapedExpandedDescription_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv", index=False)
    

updateDescription()