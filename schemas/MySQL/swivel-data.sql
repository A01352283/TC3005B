INSERT INTO usuario_final (nombres, apellidos, email, contraseña, numero_telefonico, tipo_usuario, lista_deseos_id, dirección_id)
VALUES ('Juan', 'Perez', 'juanPerez@mail.com', '1234', '12345678', 'usuario_final', 1, 1);

INSERT INTO vendedor (nombres, apellidos, email, contraseña, numero_telefonico, tipo_usuario, gerente_id)
VALUES ('Pedro', 'Gonzalez', 'pedroGonzales', '1234', '12345678', 'vendedor', 1);

INSERT INTO gerente (nombres, apellidos, email, contraseña, numero_telefonico, tipo_usuario, agencia_id)
VALUES ('Maria', 'Garcia', 'mariaGarcia@mail.com', '1234', '12345678', 'gerente', 1);

INSERT INTO agencia (nombre, email, contraseña, grupo_automotriz_id, dirección_id)
VALUES ('Agencia 1', 'agencia1@mail.com', '1234', 1, 1);

INSERT INTO grupo_automotriz (nombre_grupo_automotriz, email, contraseña, tipo_usuario, dirección_id)
VALUES ('Grupo 1', 'grupo1@mail.com', '1234', 'grupo_automotriz', 1);

INSERT INTO superadmin (nombres, apellidos, email, contraseña, tipo_usuario)
VALUES ('Super', 'Admin', 'superadmin@mail.com', '1234', 'superadmin');

INSERT INTO dirección (calle, número_exterior, ciudad, estado, país, código_postal)
VALUES ('Calle 1', '1', 'Ciudad 1', 'Estado 1', 'País 1', '12345');

-- Select all the agencies that have the direccion street name "Calle 1"
SELECT * FROM agencia WHERE dirección_id IN (SELECT dirección_id FROM dirección WHERE calle = 'Calle 1');