db.createCollection('usuario_final', {
    validator: {
        $jsonSchema: {
            bsonType: 'object',
            // Prevent any other fields from being added to the document
            additionalProperties: false,
            required: ['nombres', 'apellidos', 'email', 'contraseña', 'numero_telefonico', 'tipo_usuario', 'lista_deseos_id', 'direccion_id'],
            properties: {
                _id: { 
                    bsonType: "objectId" 
                },
                nombres: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                apellidos: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                email: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                contraseña: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                numero_telefonico: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                tipo_usuario: {
                    bsonType: 'string',
                    description: 'Debe ser un string y es requerido'
                },
                lista_deseos_id: {
                    bsonType: 'objectId',
                    description: 'Debe ser un objectId y es requerido'
                },
                direccion_id: {
                    bsonType: 'objectId',
                    description: 'Debe ser un objectId y es requerido'
                }
            }
        }
    }
});

// Make a valid insert to the collection
db.usuario_final.insertOne({
    nombres: 'Juan',
    apellidos: 'Perez',
    email: 'usuario@mail.com',
    contraseña: '123456',
    numero_telefonico: '5678901234',
    tipo_usuario: 'usuario',
    lista_deseos_id: ObjectId("5f9f5b9b9b9b9b9b9b9b9b9b"),
    direccion_id: ObjectId("5f9f5b9b9b9b9b9b9b9b9b9b")
});