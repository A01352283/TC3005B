''' Make a script to insert n amount of dummy data into the MySQL database that uses the following schema, inserting the  referenced data first.: 
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
'''

import mysql.connector
from mysql.connector import errorcode
import random
import string

# Connect to the database
try:
    cnx = mysql.connector.connect(user='root', password='123456', host='localhost', database='swivelDB')
    cursor = cnx.cursor()
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

# Create a list of names
names = ['John', 'Jane', 'Joe', 'Jill', 'Jack', 'Jenny', 'Jesse', 'Jasmine', 'Jared', 'Juan', 'Javier']
lastNames = ['Smith', 'Jones', 'Johnson', 'Jackson', 'Jenkins', 'Jensen', 'Johansson', 'Johanson', 'Jameson']

# Create a list of emails
emails = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com', 'icloud.com', 'msn.com', 'live.com', 'mail.com', 'protonmail.com']

# Create a list of passwords
passwords = ['1234', 'pass', 'contraseña', '12345', 'secreto', 'password']

# Create a list of phone numbers
phoneNumbers = ['1234567890', '0987654321', '123456789', '098765432', '12345678', '09876543', '1234567', '0987654', '123456', '098765']

# Create a list of user types
userTypes = ['usuario_final', 'vendedor', 'gerente', 'agencia', 'grupo_automotriz', 'superadmin']

# Create a list of streets
streets = ['Main', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Maple', 'Hill', 'River', 'Lake']

# Create a list of street numbers
streetNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Create a list of cities
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# Create a list of states
states = ['New York', 'California', 'Illinois', 'Texas', 'Pennsylvania', 'Arizona', 'Florida', 'Ohio', 'Michigan', 'Georgia']

# Create a list of countries
countries = ['United States', 'Mexico', 'Canada', 'United Kingdom', 'France', 'Germany', 'Spain', 'Italy', 'Argentina', 'Brazil']

# Create a list of zip codes
zipCodes = ['10001', '90001', '60601', '77001', '19101', '85001', '33101', '44101', '48201', '30301']

# Create a list of agency names
agencyNames = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'BMW', 'Mercedes', 'Audi']

# Create a list of group names
groupNames = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'Hyundai', 'Kia', 'BMW', 'Mercedes', 'Audi']

# Create a list of wish lists
