-- Inserts para datos_usuario
INSERT INTO datos_usuario (nombres, apellidos, email, contraseña, número_telefónico, is_account_verified, email_verification_token, account_provider) VALUES
    ('John', 'Doe', 'johndoe@example.com', '4d186321c1a7f0f354b297e8914ab240', '1234567890', 1, NULL, NULL),
    ('Jane', 'Doe', 'janedoe@example.com', 'f7c3bc1d808e04732adf679965ccc34ca7ae3441', '0987654321', 1, NULL, NULL),
    ('Bob', 'Smith', 'bobsmith@example.com', '3b2ce82ff53e0e0cbb7b77e78c192a7e1bd1639f', '5551234567', 0, 'qwertyuiopasdfghjklzxcvbnm123456', NULL),
    ('Alice', 'Johnson', 'alicejohnson@example.com', '3858f62230ac3c915f300c664312c63f6f7', NULL, 0, 'poiuytrewqasdfghjklmnbvcxz987654', NULL),
    ('Mark', 'Davis', 'markdavis@example.com', 'b6d767d2f8ed5d21a44b0e5886680cb9', NULL, 1, NULL, NULL),
    ('Sarah', 'Lee', 'sarahlee@example.com', 'e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4', '1112223333', 1, NULL, 'Google'),
    ('David', 'Brown', 'davidbrown@example.com', 'b6d767d2f8ed5d21a44b0e5886680cb9', '4445556666', 0, 'lkjhgfdsapoiuytrewqzxcvbnm987654', NULL),
    ('Karen', 'Miller', 'karenmiller@example.com', '1679091c5a880faf6fb5e6087eb1b2dc', '7778889999', 1, NULL, NULL),
    ('Michael', 'Wilson', 'michaelwilson@example.com', '8f14e45fceea167a5a36dedd4bea2543', NULL, 0, 'mnbvcxzlkjhgfdsapoiuytrewq123456', NULL),
    ('Linda', 'Moore', 'lindamoore@example.com', 'c16a5320fa475530d9583c34fd356ef5', NULL, 1, NULL, NULL),
    ('Juan', 'García', 'juangarcia@example.com', 'c16a5320fa475530d9583c34fd356ef5', '5551234567', true, NULL, NULL),
    ('María', 'Rodríguez', 'mariarodriguez@example.com', 'c16a5320fa475530d9583c34fd356ef5', NULL, false, 'S5fRcEwP7YjKpZq3xVvA9b2tLnMhX4gU', NULL),
    ('Pedro', 'Hernández', 'pedrohernandez@example.com', 'c16a5320fa475530d9583c34fd356ef5', '5552345678', true, NULL, NULL),
    ('Laura', 'González', 'lauragonzalez@example.com', 'c16a5320fa475530d9583c34fd356ef5', NULL, true, NULL, 'Google'),
    ('Alejandro', 'Díaz', 'alejandrodiaz@example.com', 'd033e22ae348aeb5660fc2140aec35850c4da997', '5553456789', false, 'sT6wGhM9nZxQ2vF5jKlP3rB7yXcD4', NULL),
    ('Ana', 'Sánchez', 'anasanchez@example.com', '8268d3ec3ce6f14551251a9fbd8b1df2d4c25f4a', '5554567890', true, NULL, NULL),
    ('José', 'Pérez', 'joseperez@example.com', '62e6f2776486fa4161c8e98d34de07e29ef9a9a5', NULL, false, 'aB5hRc8NpKtS3fZjVqWx2n4G6mY9uXy', NULL),
    ('Carla', 'Martínez', 'carlamartinez@example.com', 'd033e22ae348aeb5660fc2140aec35850c4da997', '5555678901', true, NULL, 'Google'),
    ('Javier', 'Flores', 'javierflores@example.com', 'b1f7c90ddc0f8587c369f9e146d7b523443eabcc', NULL, true, NULL, NULL),
    ('Juan', 'Pérez', 'juanperez@mail.com', '8268d3ec3ce6f14551251a9fbd8b1df2d4c25f4a', '5551234567', 1, NULL, NULL),
    ('María', 'García', 'mariagarcia@mail.com', 'waI5pAVhMqJgDzujZtH9Z9J82kmnu4e4jwvC1Wjk8yBcPe', '5559876543', 1, NULL, 'Google'),
    ('Luis', 'Hernández', 'luishernandez@mail.com', 'df209a6171fc2d1c69f38b0f586c67c92a83df50', '5551112233', 0, 'abcd1234efgh5678ijkl9012mnop3456', NULL),
    ('Ana', 'Martínez', 'anamartinez@mail.com', 'kVbO6lBNNIzBua6LdU6zguu1jUZV7MNkP76JFVfMJSI6oJux6UdxW', '5555555555', 1, NULL, 'Google'),
    ('Pedro', 'González', 'pedrogonzalez@mail.com', 'df209a6171fc2d1c69f38b0f586c67c92a83df50', '5557778888', 0, 'qrst1234uvwx5678yzab9012cdef3456', NULL),
    ('Silvia', 'Romero', 'silviaromero@example.com', '4ce4e4e4b9dfe7f0a232eef5287d86e6fc6c8d96', '5556789012', false, 'pT7qRsU9fXvN3mZaB6jKl4E5wY8cD2xH', 'Google');

-- Inserts para datos_lugar
INSERT INTO datos_lugar (nombre, email, contraseña, número_telefónico) VALUES
    ('Autogroup USA', 'info@autogroupusa.com', 'd033e22ae348aeb5660fc2140aec35850c4da997', '5551234234'),
    ('DriveNation', 'info@drivenation.com', '03862b30edf5d5d5ffda7ef1955f5f5b0d5e3df3', '5555678713'),
    ('AutoNation', 'info@autonation.com', 'e9e9e7b05d09f954f7f6c2df1fb8c8e1d44b9c7f', '5554321543'),
    ('CarMax', 'info@carmax.com', 'b1f7c90ddc0f8587c369f9e146d7b523443eabcc', '5558763455'),
    ('Group 1 Automotive', 'info@group1auto.com', '2af1d8a09de5416c0bb6d63bf104c8d3d3b6ddc3', '5552345253'),
    ('Sonic Automotive', 'info@sonicautomotive.com', '8268d3ec3ce6f14551251a9fbd8b1df2d4c25f4a', '5557890452'),
    ('Penske Automotive Group', 'info@penskeautomotive.com', '62e6f2776486fa4161c8e98d34de07e29ef9a9a5', '5553456423'),
    ('Asbury Automotive Group', 'info@asburyauto.com', 'df209a6171fc2d1c69f38b0f586c67c92a83df50', '5559012626'),
    ('Lithia Motors', 'info@lithia.com', '717eab2280be5c100ee14fb78a6dbdcf6edf7166', '5556789543'),
    ('Hendrick Automotive Group', 'info@hendrickauto.com', '4ce4e4e4b9dfe7f0a232eef5287d86e6fc6c8d96', '5550123624'),
    ('Grupo Automotriz de la Laguna', 'gal@grupolaguna.com', '$2y$10$op4utk.VdRRyRV8es57OtOVSVSnm0m0mYZTHoBL9zs5/KRz5h5J5y', '8717591234'),
    ('Autos del Valle', 'info@autosdelvalle.com', '$2y$10$2w5yEx/waI5pAVhMqJgDzujZtH9Z9J82kmnu4e4jwvC1Wjk8yBcPe', '6566423120'),
    ('Agencia Automotriz del Centro', 'ventas@agenciaacentro.com', '$2y$10$U6rMkstTc/CWdX00De50du1g3/kNpjNcPmmFdeCPh72G/2oLQjvOu', '5551267890'),
    ('Grupo Automotriz del Bajío', 'contacto@grupoautomotrizbajio.com', '$2y$10$uDeeH.3qorj12YYLE8gFh.Giz29LQV7myzjvX8V7RmkKjQ5N5ia5m', '4771234567'),
    ('Autos de Occidente', 'atencionaclientes@autosdeoccidente.com', '$2y$10$8StSN.yMjGB57S1jK58tEuY4t4mvvc8bF3kP0s.qJklF9NTH/Yxby', '3339876543'),
    ('Agencia Automotriz del Pacífico', 'info@agenciapacifico.com', '$2y$10$0D7hLKWnkjK2QzTcT2/.OObAefUNF9S9GZkhIVd.IJNdLc0iHBYEa', '6625551212'),
    ('Grupo Automotriz del Golfo', 'contacto@grupoautomotrizgolfo.com', '$2y$10$fPhGj7rq1B6K33XusVx8KOcPbxnVMyU6lLb6z8U6wzZsODcqphs.y', '2292223333'),
    ('Autos del Norte', 'ventas@autosdelnorte.com', '$2y$10$QnkQZ/E/Sd9DjTuLl59pauuaFkqN3w4t4lH5stYYM5D5q8g77iX/m', '8181234567'),
    ('Agencia Automotriz del Sur', 'contacto@agenciasur.com', '$2y$10$kVbO6lBNNIzBua6LdU6zguu1jUZV7MNkP76JFVfMJSI6oJux6UdxW', '5555551212'),
    ("Auto World Inc.", "info@autoworld.com", "5f4dcc3b5aa765d61d8327deb882cf99", "5551234567"),
    ("Car Land Agency", "sales@carland.com", "c4ca4238a0b923820dcc509a6f75849b", "5559876543"),
    ("Speedy Cars LLC", "info@speedycars.com", "1a1dc91c907325c69271ddf0c944bc72", "5555551212"),
    ("Auto Universe Corp.", "contact@autouniverse.com", "8f14e45fceea167a5a36dedd4bea2543", "5551237890"),
    ("Motor Emporium", "sales@motoremporium.com", "3c59dc048e8850243be8079a5c74d079", "5554567890"),
    ("Car Connect Inc.", "info@carconnect.com", "d4f6d80d3bb06c986eaf01bcbd78e903", "5552223333"),
    ("Elite Cars Group", "sales@elitecarsgroup.com", "7c6a180b36896a0a8c02787eeafb0e4c", "5557894561"),
    ("The Car Spot", "contact@thecarspot.com", "6c8349cc7260ae62e3b1396831a8398f", "5555559876"),
    ("Auto Plaza", "info@autoplaza.com", "e1671797c52e15f763380b45e841ec32", "5551112233"),
    ("Car Avenue", "sales@caravenue.com", "d41d8cd98f00b204e9800998ecf8427e", "5557771234");

-- Inserts para dirección
INSERT INTO dirección (calle, número_interior, número_exterior, ciudad, estado, país, código_postal)VALUES
    ('Calle Hidalgo', '23', '12', 'Ciudad de México', 'Ciudad de México', 'México', '06500'),
    ('Avenida Juárez', '205', '19', 'Puebla', 'Puebla', 'México', '72000'),
    ('Boulevard Francisco Villa', '1015', '23', 'León', 'Guanajuato', 'México', '37260'),
    ('Calle 5 de Mayo', '10', '55', 'Oaxaca', 'Oaxaca', 'México', '68000'),
    ('Calle Bravo', '32', '17', 'Tijuana', 'Baja California', 'México', '22000'),
    ('Avenida San Francisco', '345', '72', 'Mérida', 'Yucatán', 'México', '97000'),
    ('Calle Morelos', '21', '98', 'Guadalajara', 'Jalisco', 'México', '44100'),
    ('Avenida Benito Juárez', '570', '11', 'Monterrey', 'Nuevo León', 'México', '64000'),
    ('Calle Miguel Hidalgo', '90', '32', 'Cancún', 'Quintana Roo', 'México', '77500'),
    ('Avenida de la Reforma', '105', '25', 'México', 'Ciudad de México', 'México', '06600'),
    ('Av. México', '150', 'A', 'Monterrey', 'Nuevo León', 'México', '64100'),
    ('Calle Durango', '12', '', 'Tijuana', 'Baja California', 'México', '22040'),
    ('Av. Revolución', '1455', '', 'Ciudad de México', 'Ciudad de México', 'México', '01090'),
    ('Calle Reforma', '125', '', 'Puebla', 'Puebla', 'México', '72000'),
    ('Av. Hidalgo', '350', 'C', 'Guadalajara', 'Jalisco', 'México', '44100'),
    ('Calle Victoria', '25', 'B', 'Mérida', 'Yucatán', 'México', '97000'),
    ('Av. Insurgentes', '1300', '', 'Toluca', 'Estado de México', 'México', '50020'),
    ('Calle Independencia', '75', 'A', 'Aguascalientes', 'Aguascalientes', 'México', '20040'),
    ('Av. Juárez', '500', '', 'Querétaro', 'Querétaro', 'México', '76000'),
    ('Calle Guerrero', '28', 'B', 'Oaxaca de Juárez', 'Oaxaca', 'México', '68000');

-- Inserts para automovil
INSERT INTO automovil (agencia_id, marca, modelo, año, precio, color, combustible, autonomía, transmisión, cantidad, motor, tipo_vehículo, descripción) VALUES
    (1, "Ford", "Mustang", 2022, 450000, "Rojo", "Gasolina", 350, "Manual", 5, "5.0L V8", "Deportivo", "El nuevo Mustang es el auto deportivo definitivo. Con un motor V8 de 5.0L que produce 460 caballos de fuerza, este Mustang es capaz de acelerar de 0 a 100 km/h en menos de 4 segundos."),
    (1, "Chevrolet", "Spark", 2022, 150000, "Azul", "Gasolina", 500, "Manual", 3, "1.2L I4", "Compacto", "El Spark es un auto compacto y ágil que es ideal para la ciudad. Con un motor de 1.2L y una transmisión manual de 5 velocidades, este auto es muy eficiente en términos de combustible."),
    (2, "Toyota", "Sienna", 2022, 700000, "Blanco", "Gasolina", 700, "Automático", 2, "3.5L V6", "Minivan", "La Sienna es una minivan familiar que cuenta con una gran cantidad de características de seguridad y comodidad. Con una capacidad de 7 pasajeros, este auto es ideal para viajes largos."),
    (3, "Nissan", "Kicks", 2022, 300000, "Gris", "Gasolina", 600, "Automático", 4, "1.6L I4", "SUV", "El Nissan Kicks es un SUV pequeño y ágil que es perfecto para la ciudad. Con una gran cantidad de características de seguridad y tecnología, este auto es una excelente opción para personas que buscan un auto compacto pero cómodo."),
    (4, "Honda", "Civic", 2022, 400000, "Negro", "Gasolina", 550, "Manual", 6, "2.0L I4", "Deportivo", "El Honda Civic es un auto deportivo que ofrece un gran equilibrio entre potencia y eficiencia. Con un motor de 2.0L y una transmisión manual de 6 velocidades, este auto es una excelente opción para personas que buscan un auto divertido de conducir."),
    (5, "Hyundai", "Kona", 2022, 350000, "Rojo", "Eléctrico", 400, "Automático", 2, "Eléctrico", "SUV", "El Hyundai Kona es un SUV eléctrico que ofrece una gran autonomía y un alto nivel de tecnología. Con una batería de iones de litio de alta capacidad, este auto es capaz de recorrer hasta 400 km con una sola carga."),
    (2, 'Toyota', 'Camry', 2022, 500000, 'Rojo', 'Gasolina', 700, 'Automático', 8, '2.5L I4', 'Sedán', 'El Toyota Camry 2022 es un sedán de lujo con excelente rendimiento de combustible, equipado con una pantalla táctil de 8 pulgadas, cámara de visión trasera, sistema de audio premium y mucho más.'),
    (3, 'Volkswagen', 'Jetta', 2023, 550000, 'Blanco', 'Gasolina', 650, 'Manual', 5, '1.4L I4', 'Sedán', 'El Volkswagen Jetta 2023 es un elegante sedán compacto con características avanzadas como la pantalla táctil de 6.5 pulgadas, cámara trasera, sistema de sonido premium y más.'),
    (1, 'Ford', 'Explorer', 2021, 850000, 'Negro', 'Gasolina', 750, 'Automático', 4, '3.0L V6', 'SUV', 'La Ford Explorer 2021 es una SUV de lujo con un interior espacioso y equipada con características avanzadas como una pantalla táctil de 10.1 pulgadas, asientos de cuero y mucho más.'),
    (5, 'Chevrolet', 'Camaro', 2022, 700000, 'Amarillo', 'Gasolina', 600, 'Manual', 3, '6.2L V8', 'Deportivo', 'El Chevrolet Camaro 2022 es un deportivo de alto rendimiento con características avanzadas como una pantalla táctil de 7 pulgadas, cámara trasera, sistema de audio premium y más.'),
    (4, 'Honda', 'Odyssey', 2023, 950000, 'Azul', 'Gasolina', 500, 'Automático', 6, '3.5L V6', 'Minivan', 'La Honda Odyssey 2023 es una minivan espaciosa y equipada con características avanzadas como una pantalla táctil de 8 pulgadas, asientos de cuero, cámara trasera y más.'),
    (2, 'Toyota', 'Rav4', 2021, 720000, 'Blanco', 'Gasolina', 800, 'Automático', 7, '2.5L I4', 'SUV', 'La Toyota Rav4 2021 es una SUV de alto rendimiento con características avanzadas como una pantalla táctil de 7 pulgadas, sistema de audio premium, cámara trasera y más.'),
    (3, 'Volkswagen', 'Tiguan', 2023, 690000, 'Rojo', 'Gasolina', 750, 'Automático', 6, '2.0L I4', 'SUV', 'La Volkswagen Tiguan 2023 es una SUV de lujo con características avanzadas como una pantalla táctil de 10.1 pulgadas, asientos de cuero, cámara trasera y más.');

-- Inserts para documentos
INSERT INTO documentos(usuario_final_id, nombre_documento, url_documento) VALUES
    (1, 'identificación', 'https://example-bucket.s3.amazonaws.com/identificacion_1.pdf'),
    (1, 'licencia de conducir', 'https://example-bucket.s3.amazonaws.com/licencia_1.pdf'),
    (2, 'identificación', 'https://example-bucket.s3.amazonaws.com/identificacion_2.pdf'),
    (2, 'licencia de conducir', 'https://example-bucket.s3.amazonaws.com/licencia_2.pdf'),
    (3, 'identificación', 'https://example-bucket.s3.amazonaws.com/identificacion_3.pdf'),
    (3, 'licencia de conducir', 'https://example-bucket.s3.amazonaws.com/licencia_3.pdf'),
    (4, 'identificación', 'https://example-bucket.s3.amazonaws.com/identificacion_4.pdf'),
    (4, 'licencia de conducir', 'https://example-bucket.s3.amazonaws.com/licencia_4.pdf'),
    (5, 'identificación', 'https://example-bucket.s3.amazonaws.com/identificacion_5.pdf'),
    (5, 'licencia de conducir', 'https://example-bucket.s3.amazonaws.com/licencia_5.pdf');

-- Inserts para superadmin
INSERT INTO superadmin (nombre, apellidos, email, contraseña) VALUES
    ('John', 'Doe', 'johndoe@swivel.com.mx', '2c8f0e0f9faef341af5ed5c6b5f6a9871eef5aa6'),
    ('Jane', 'Doe', 'janedoe@swivel.com.mx', 'b78d8d50398524a2e2e2686e7da54513d726bb92'),
    ('Mike', 'Smith', 'mikesmith@swivel.com.mx', '42f336edf79051a7d557cf8dd846eed7e9ebea25'),
    ('Sarah', 'Johnson', 'sarahjohnson@swivel.com.mx', 'f6d8d93c256c8441e62b3297b2d65a1a7a903ce2'),
    ('David', 'Lee', 'davidlee@swivel.com.mx', '36ed1b93d1f3a4f4adec97a34e3f99c3b3a417a9'),
    ('Emily', 'Chen', 'emilychen@swivel.com.mx', 'aa88f389f2c2e8d77e62c9f9e35ce9406f5b6a47'),
    ('Juan', 'García', 'juangarcia@swivel.com.mx', '22f0efc994fbaaae27f2e162c1a480b2a06a1c20'),
    ('María', 'Hernández', 'mariahernandez@swivel.com.mx', '71dbf5e636f7a4668f399be9f89ab855fd2f1e92'),
    ('Pedro', 'González', 'pedrogonzalez@swivel.com.mx', 'f81920e0447a3a3a221005ec83bcb9f9ebc688fa'),
    ('Lucía', 'Rodríguez', 'luciarodriguez@swivel.com.mx', 'e8f9b9a7a38a23a0de7d8aeb29f18bb2b1340b6c');

-- Inserts para usuario_final
INSERT INTO usuario_final (datos_usuario_id, dirección_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Inserts para vendedor
INSERT INTO vendedor (datos_usuario_id, contar_ventas_en_proceso, contar_ventas_completadas, gerente_id) VALUES
    (11, 5, 10, 1),
    (12, 3, 8, 2),
    (13, 7, 12, 3),
    (14, 1, 2, 4),
    (15, 0, 5, 5),
    (16, 2, 6, 6),
    (17, 4, 9, 7),
    (18, 6, 11, 8),
    (19, 2, 7, 9),
    (20, 8, 15, 10);

-- Inserts para gerente
INSERT INTO gerente (datos_usuario_id, agencia_id) VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Inserts para agencia
INSERT INTO agencia (dirección_id, datos_lugar_id, grupo_automotriz_id) VALUES
    (11, 21, 1),
    (12, 22, 2),
    (13, 23, 3),
    (14, 24, 4),
    (15, 25, 5),
    (16, 26, 6),
    (17, 27, 7),
    (18, 28, 8),
    (19, 29, 9),
    (20, 30, 10);

-- Inserts para grupo_automotriz
INSERT INTO grupo_automotriz (datos_lugar_id, dirección_id) VALUES
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 16),
    (17, 17),
    (18, 18),
    (19, 19),
    (20, 20);

-- Inserts para lista_deseos
INSERT INTO lista_deseos(user_id, auto_id) VALUES 
    (1, 3),
    (1, 5),
    (2, 2),
    (2, 4),
    (3, 7),
    (3, 10),
    (4, 1),
    (4, 9),
    (5, 6),
    (5, 8); 