DROP SCHEMA IF EXISTS swivelDB;
CREATE SCHEMA swivelDB;
USE swivelDB;

CREATE TABLE usuario_final(
    usuario_final_id INT NOT NULL AUTO_INCREMENT,
    datos_usuario_id INT NOT NULL REFERENCES datos_usuario(datos_usuario_id),
    dirección_id INT NOT NULL REFERENCES dirección(dirección_id),
    PRIMARY KEY (usuario_final_id)
);

CREATE TABLE vendedor(
    vendedor_id INT NOT NULL AUTO_INCREMENT,
    datos_usuario_id INT NOT NULL REFERENCES datos_usuario(datos_usuario_id),
    contar_ventas_en_proceso INT NOT NULL,
    contar_ventas_completadas INT NOT NULL,
    gerente_id INT NOT NULL REFERENCES gerente(gerente_id),
    PRIMARY KEY (vendedor_id)
);

CREATE TABLE gerente(
    gerente_id INT NOT NULL AUTO_INCREMENT,
    datos_usuario_id INT NOT NULL REFERENCES datos_usuario(datos_usuario_id),
    agencia_id INT NOT NULL REFERENCES agencia(agencia_id),
    PRIMARY KEY (gerente_id)
);

CREATE TABLE agencia(
    agencia_id INT NOT NULL AUTO_INCREMENT,
    dirección_id INT NOT NULL REFERENCES dirección(dirección_id),
    datos_lugar_id INT NOT NULL REFERENCES datos_lugar(datos_lugar_id),
    grupo_automotriz_id INT NOT NULL REFERENCES grupo_automotriz(grupo_automotriz_id),
    PRIMARY KEY (agencia_id)
);

CREATE TABLE grupo_automotriz(
    grupo_automotriz_id INT NOT NULL AUTO_INCREMENT,
    datos_lugar_id INT NOT NULL REFERENCES datos_lugar(datos_lugar_id),
    dirección_id INT NOT NULL REFERENCES dirección(dirección_id),
    PRIMARY KEY (grupo_automotriz_id)
);

CREATE TABLE superadmin(
    superadmin_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(254) NOT NULL,
    apellidos VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(254) NOT NULL,
    PRIMARY KEY (admin_id)
);

CREATE TABLE dirección(
    dirección_id INT NOT NULL AUTO_INCREMENT,
    calle VARCHAR(254) NOT NULL,
    número_exterior VARCHAR(15) NOT NULL,
    número_interior VARCHAR(15),
    ciudad VARCHAR(32) NOT NULL,
    estado VARCHAR(32) NOT NULL,
    país VARCHAR(64) NOT NULL,
    código_postal CHAR(5) NOT NULL,
    PRIMARY KEY (dirección_id)
);

CREATE TABLE lista_deseos(
    user_id INT NOT NULL REFERENCES usuario_final(usuario_final_id),
    auto_id INT NOT NULL REFERENCES automovil(auto_id),
    PRIMARY KEY (user_id, auto_id)
);

CREATE TABLE datos_usuario(
    datos_usuario_id INT NOT NULL AUTO_INCREMENT,
    nombres VARCHAR(254) NOT NULL,
    apellidos VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(254) NOT NULL,
    número_telefónico CHAR(10),
    is_account_verified BOOLEAN NOT NULL,
    email_verification_token CHAR(32),
    account_provider CHAR(254),
    PRIMARY KEY (datos_usuario_id)
);

CREATE TABLE datos_lugar(
    datos_lugar_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(254) NOT NULL,
    email VARCHAR(254) NOT NULL,
    contraseña VARCHAR(254) NOT NULL,
    número_telefónico CHAR(10) NOT NULL,
    PRIMARY KEY (datos_lugar_id)
);

CREATE TABLE documentos(
    documentos_id INT NOT NULL AUTO_INCREMENT,
    usuario_final_id INT NOT NULL REFERENCES usuario_final(usuario_final_id),
    nombre_documento VARCHAR(254) NOT NULL,
    url_documento VARCHAR(65532) NOT NULL,
    PRIMARY KEY (documentos_id)
);

CREATE TABLE automovil(
    auto_id INT NOT NULL AUTO_INCREMENT,
    agencia_id INT NOT NULL REFERENCES agencia(agencia_id),
    marca VARCHAR(32) NOT NULL,
    modelo VARCHAR(254) NOT NULL,
    año INT NOT NULL,
    precio INT NOT NULL,
    color VARCHAR(254) NOT NULL,
    combustible VARCHAR (10) NOT NULL,
    autonomía INT NOT NULL,
    transmisión VARCHAR (10) NOT NULL,
    cantidad INT NOT NULL,
    motor VARCHAR (15) NOT NULL,
    tipo_vehículo VARCHAR (254) NOT NULL,
    descripción TEXT NOT NULL,
    PRIMARY KEY (auto_id)
    )