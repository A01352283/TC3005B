DROP SCHEMA IF EXISTS swivelDB;
CREATE SCHEMA swivelDB;
USE swivelDB;

CREATE TABLE usuario_final(
    usuario_final_id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(254) NOT NULL,
    apellidos VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    numero_telefonico VARCHAR(50),
    tipo_usuario CHAR(50) NOT NULL,
    lista_deseos_id INT REFERENCES lista_deseos(lista_deseos_id),
    dirección_id INT REFERENCES dirección(dirección_id),
    PRIMARY KEY (usuario_final_id)
);

CREATE TABLE vendedor(
    vendedor_id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(254) NOT NULL,
    apellidos VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    numero_telefonico VARCHAR(50),
    tipo_usuario CHAR(50) NOT NULL,
    gerente_id INT REFERENCES gerente(gerente_id),
    PRIMARY KEY (vendedor_id)
);

CREATE TABLE gerente(
    gerente_id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(254) NOT NULL,
    apellidos VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    numero_telefonico VARCHAR(50),
    tipo_usuario CHAR(50) NOT NULL,
    agencia_id INT REFERENCES agencia(agencia_id),
    PRIMARY KEY (gerente_id)
);

CREATE TABLE agencia(
    agencia_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    tipo_usuario CHAR(50) NOT NULL,
    grupo_automotriz_id INT REFERENCES grupo_automotriz(grupo_automotriz_id),
    dirección_id INT REFERENCES dirección(dirección_id),
    PRIMARY KEY (agencia_id)
);

CREATE TABLE grupo_automotriz(
    grupo_automotriz_id INT NOT NULL AUTO_INCREMENT,
    nombre_grupo_automotriz VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    tipo_usuario CHAR(50) NOT NULL,
    dirección_id INT REFERENCES dirección(dirección_id),
    PRIMARY KEY (grupo_automotriz_id)
);

CREATE TABLE superadmin(
    admin_id INT NOT NULL AUTO_INCREMENT,
    nombres CHAR(50) NOT NULL,
    apellidos CHAR(50) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(30) NOT NULL,
    tipo_usuario CHAR(50) NOT NULL,
    PRIMARY KEY (admin_id)
);

CREATE TABLE dirección(
    dirección_id INT NOT NULL AUTO_INCREMENT,
    calle VARCHAR(254) NOT NULL,
    número_exterior VARCHAR(10) NOT NULL,
    ciudad VARCHAR(60) NOT NULL,
    estado VARCHAR(254) NOT NULL,
    país VARCHAR(254) NOT NULL,
    código_postal VARCHAR(5) NOT NULL,
    PRIMARY KEY (dirección_id)
);

CREATE TABLE lista_deseos(
    lista_deseos_id INT NOT NULL AUTO_INCREMENT,
    -- Array of car ids
    PRIMARY KEY (lista_deseos_id)
);

CREATE TABLE automovil(
    auto_id INT NOT NULL AUTO_INCREMENT,
    marca VARCHAR(254) NOT NULL,
    modelo VARCHAR(254) NOT NULL,
    año VARCHAR(4) NOT NULL,
    precio INT NOT NULL,
    color VARCHAR(254) NOT NULL,
    combustible CHAR (75) NOT NULL,
    litros INT NOT NULL,
    motor VARCHAR (75),
    transmisión CHAR (75) NOT NULL,
    tipo_vehículo CHAR (75) NOT NULL,
    descripción VARCHAR (2000),
    agencia_id INT REFERENCES agencia(agencia_id),
    PRIMARY KEY (auto_id)
    )