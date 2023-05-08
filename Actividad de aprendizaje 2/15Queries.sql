-- Select all the agencies that have the ciudad "Ciudad de México"
SELECT * FROM agencia 
JOIN dirección ON agencia.dirección_id = dirección.dirección_id 
WHERE dirección.ciudad = "Ciudad de México";

--Retrieve all columns from the usuario_final table for users who have a verified account
SELECT * FROM usuario_final 
JOIN datos_usuario ON usuario_final.datos_usuario_id = datos_usuario.datos_usuario_id 
WHERE datos_usuario.is_account_verified = TRUE;

-- Retrieve the nombre and apellidos of the superadmin with superadmin_id = 1
SELECT nombre, apellidos FROM superadmin 
WHERE superadmin_id = 1;

-- Retrieve the marca and modelo columns from the automovil table for cars with a precio greater than 20000:
SELECT marca, modelo FROM automovil 
WHERE precio > 20000;

-- Retrieve the nombre and email columns from the datos_lugar table for places with a nombre that contains the word "Automotriz"
SELECT nombre, email FROM datos_lugar 
WHERE nombre LIKE '%Automotriz%';

-- Retrieve the calle, ciudad, and país columns from the dirección table for locations with a país equal to 'Mexico' and a ciudad not equal to 'Mexico City':
SELECT calle, ciudad, país FROM dirección 
WHERE país = 'Mexico' AND ciudad <> 'Mexico City';

-- Retrieve the nombre and apellidos columns from the superadmin table for admins with an email domain of 'swivel.com.mx':
SELECT nombre, apellidos FROM superadmin 
WHERE email LIKE '%@swivel.com.mx';

-- Retrieve the usuario_final_id and url_documento column from the documentos table for documents associated with the user with usuario_final_id equal to 5 and a nombre_documento containing the string 'identificación':
SELECT usuario_final_id, url_documento FROM documentos 
WHERE usuario_final_id = 5 AND nombre_documento LIKE '%identificación%';

-- Retrieve the ciudad, estado and código postal columns from the dirección table for locations with a ciudad not equal to 'Mexico City' or a estado equal to 'Jalisco':
SELECT ciudad, estado, código_postal FROM dirección 
WHERE ciudad <> 'Mexico City' OR estado = 'Jalisco';

-- Select all the data for the user with ID 3:
SELECT * FROM usuario_final 
INNER JOIN datos_usuario ON usuario_final.datos_usuario_id = datos_usuario.datos_usuario_id 
INNER JOIN dirección ON usuario_final.dirección_id = dirección.dirección_id 
WHERE usuario_final.usuario_final_id = 3;

-- Select the email, nombre, and apellidos of all superadmins in the system:
SELECT email, nombre, apellidos FROM superadmin;

-- Select the name and phone number of all agencias in Yucatán:
SELECT nombre, número_telefónico FROM agencia 
INNER JOIN datos_lugar ON agencia.datos_lugar_id = datos_lugar.datos_lugar_id 
INNER JOIN dirección ON agencia.dirección_id = dirección.dirección_id 
WHERE dirección.estado = 'Yucatán';

--Select the total number of cars available for sale in the system:
SELECT SUM(cantidad) FROM automovil;

--Select the number of vendors associated with each gerente:
SELECT gerente_id, COUNT(vendedor_id) AS num_vendors FROM vendedor GROUP BY gerente_id;

-- Select the number of cars with a fuel type of "Gasolina" for each brand:
SELECT marca, COUNT(auto_id) AS num_gasolina_cars FROM automovil WHERE combustible = 'Gasolina' GROUP BY marca;