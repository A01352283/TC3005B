
db.createCollection('automovil', {
    validator: {
        $jsonSchema: {
            bsonType: 'object',
            // Prevent any other fields from being added to the document
            additionalProperties: false,
            required: ['marca', 'modelo', 'año', 'precio', 'color', 'combustible', 'disponibilidad', 'motor', 'agencia', 'tipo_vehiculo', 'fotografias'],
            properties: {
                _id: { 
                    bsonType: "objectId" 
                },
                marca: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                modelo: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                año: {
                    bsonType: 'int',
                    description: 'Debe ser un int y es requerido'
                },
                precio: {
                    bsonType: 'int',
                    description: 'Debe ser un int y es requerido'
                },
                color: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                combustible: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                disponibilidad: {
                    bsonType: 'bool',
                    description: 'Debe ser un bool y es requerido'
                },
                motor: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                agencia: {
                    bsonType: 'objectId',
                    description: 'Debe ser un objectId y es requerido'
                },
                tipo_vehiculo: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                fotografias: {
                    bsonType: 'objectId',
                    description: 'Debe ser un objectId y es requerido'
                }
            }
        }
    }
});

// Make an valid insert to test the schema
db.automovil.insertOne({
    marca: 'Toyota',
    modelo: 'Corolla',
    año: 2019,
    precio: 100000,
    color: 'Rojo',
    combustible: 'Magna',
    disponibilidad: true,
    motor: 'Automatico',
    agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
    tipo_vehiculo: 'Sedan',
    fotografias: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b")
});


// Make the previous insertMany valid but with varying years, prices, and vehicle types
db.automovil.insertMany([
    {
        marca: 'Volkswagen',
        modelo: 'Jetta',
        año: 2019,
        precio: 200000,
        color: 'Rojo',
        combustible: 'Magna',
        disponibilidad: true,
        motor: 'Automatico',
        agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
        tipo_vehiculo: 'Camioneta',
        fotografias: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b")
    },
    {
        marca: 'Ford',
        modelo: 'Fusion',
        año: 2019,
        precio: 300000,
        color: 'Rojo',
        combustible: 'Magna',
        disponibilidad: true,
        motor: 'Automatico',
        agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
        tipo_vehiculo: 'Camioneta',
        fotografias: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b")
    }
]);

// Make an invalid insert to test the schema where there is an aditional field
db.automovil.insertOne({
    marca: 'Toyota',
    modelo: 'Corolla',
    año: 2019,
    precio: 100000,
    color: 'Rojo',
    combustible: 'Magna',
    disponibilidad: true,
    motor: 'Automatico',
    agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
    tipo_vehiculo: 'Sedan',
    fotografias: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
    aditional_field: 'This is an aditional field'
});

// Make an invalid insert to test the schema
db.automovil.insertOne({
    marca: 'Toyota',
    modelo: 'Corolla',
    año: 2019,
    precio: 100000,
    color: 'Rojo',
    combustible: 'Magna',
    disponibilidad: true,
    motor: 'Automatico',
    agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
    tipo_vehiculo: 'Sedan',
    fotografias: '5e9b9b9b9b9b9b9b9b9b9b9b'
});

// Make an invalid insert to test the schema where año is not an int
db.automovil.insertOne({
    marca: 'Toyota',
    modelo: 'Corolla',
    año: '2019',
    precio: 100000,
    color: 'Rojo',
    combustible: 'Magna',
    disponibilidad: true,
    motor: 'Automatico',
    agencia: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b"),
    tipo_vehiculo: 'Sedan',
    fotografias: ObjectId("5e9b9b9b9b9b9b9b9b9b9b9b")
});