CREATE TABLE Roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

INSERT INTO Roles (nombre)
VALUES 
('Administrador'),
('Usuaria');

CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(200) NOT NULL,
    nombre_usuario VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    rol_id INT REFERENCES Roles(id)
);


CREATE TABLE Alcaldias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    clave_inegi VARCHAR(10)
);

INSERT INTO Alcaldias (nombre, clave_inegi)
VALUES
('Álvaro Obregón', '09010'),
('Azcapotzalco', '09020'),
('Benito Juárez', '09030'),
('Coyoacán', '09040'),
('Cuajimalpa de Morelos', '09050'),
('Cuauhtémoc', '09060'),
('Gustavo A. Madero', '09070'),
('Iztacalco', '09080'),
('Iztapalapa', '09090'),
('La Magdalena Contreras', '09100'),
('Miguel Hidalgo', '09110'),
('Milpa Alta', '09120'),
('Tláhuac', '09130'),
('Tlalpan', '09140'),
('Venustiano Carranza', '09150'),
('Xochimilco', '09160');

CREATE TABLE Albergues (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(50),
    codigo_postal VARCHAR(10),
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6),
    id_alcaldia INT REFERENCES Alcaldias(id)
);

INSERT INTO Albergues (nombre, direccion, telefono, codigo_postal, latitud, longitud, id_alcaldia)
VALUES
('Unidad Elena Poniatowska en Iztapalapa', 'Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella colonia el Santuario Aculco', '55 9131 0545', NULL, 19.351890, -99.066200, 9),
('Casa de las Siempre Vivas, antes Módulo De Atención A La Mujer', 'Paraje San Juan, El Vergel #24, Francisco Villa, Iztapalapa', 'Desconocido', NULL, 19.354200, -99.067900, 9),
('Centro de Atención Para Mujeres Maltratadas A.c. Muuknequi', 'Dr. Jimenez 114-Interior 10, Doctores, Cuauhtémoc', '55 5761 9684', NULL, 19.425700, -99.146000, 6),
('Casa de la Mujer', 'Parcialidad 11, Peralvillo, Morelos, Cuauhtémoc', 'Desconocido', NULL, 19.445800, -99.134000, 6),
('Centro de Atención a la violencia Intrafamiliar C.A.V.I.', 'Calle Gral. Gabriel Hernández 56, Doctores, Cuauhtémoc', '55 5345 5229', NULL, 19.425000, -99.145800, 6),
('Unión Nacional de Mujeres Mexicanas', 'Topacio 4, Centro Histórico de la Cdad. de México, Centro, Cuauhtémoc', '55 5522 6326', NULL, 19.432600, -99.133200, 6),
('Ministerios De Amor Ac', 'Actipan 16, Insurgentes Mixcoac, Benito Juárez', '55 5611 1111', NULL, 19.377300, -99.177400, 3),
('Luna', 'Camino Cerro de la Estrella s/n Centro Social Villa Estrella, Módulo 4 El Santuario, Aculco, Iztapalapa', 'Desconocido', NULL, 19.351800, -99.066000, 9),
('Unidad Benita Galeana en Benito Juárez', 'Eje Central Lázaro Cárdenas 695, piso 1, colonia Narvarte Poniente, alcaldía Benito Juárez', '55 5160 0039‬', NULL, 19.392700, -99.153700, 3),
('LUNA Benita Galeana', 'Eje 5 Sur Ramos Millán 95, colonia Niños Héroes de Chapultepec', '55 2124 4929‬', NULL, 19.386800, -99.148000, 3),
('Unidad Juana de Asbaje en Cuauhtémoc', 'Aldama, Violeta y Mina s/n, sótano edificio de la alcaldía, colonia Buenavista', '5591315945', NULL, 19.447400, -99.151000, 6),
('LUNA Cihual in Calli – Mercado. Secretaría de las Mujeres', 'Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro', '55 1549 1512', NULL, 19.192900, -99.021500, 12),
('Albergue Casa Madre Teresa', 'Allende 55, Rosas del Tepeyac, Gustavo A. Madero', '55 5781 3647', NULL, 19.486800, -99.114500, 7),
('Unidad Marcela Lagarde en Azcapotzalco', 'Av. 22 de febrero 421, colonia Barrio de San Marcos', '55 1716 0998', NULL, 19.481600, -99.186700, 2),
('Unidad Amparo Ochoa en Cuajimalpa', 'Prolongación 16 de septiembre s/n casi esquina Av. Veracruz, colonia Contadero', '55 5813 5000', NULL, 19.358000, -99.285000, 5),
('Sede Castorena', 'José María Castorena 187, colonia Cuajimalpa', '55 9131 9552', NULL, 19.360500, -99.286200, 5),
('Sede Agrícola Oriental', 'Av. Sur 8, s/n, casi con Av. Javier Rojo Gómez (atrás del deportivo Leandro Valle), colonia Agrícola Oriental', '55 2063 2369', NULL, 19.395700, -99.091900, 8),
('Unidad Cristina Pacheco', 'Piaztic s/n (frente a secundaria 262), colonia San José Atacaxco', '55 9134 7709', NULL, 19.327200, -99.243900, 10),
('Sede Observatorio', 'Av. Observatorio s/n esq. General José María Mendívil, colonia Daniel Garza', '55 1715 6328', NULL, 19.400400, -99.200600, 11),
('Unidad Cihual in Calli', 'Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro', '55 2127 4515', NULL, 19.192800, -99.021400, 12),
('Sede Calmecac', 'Av. Puebla 250, esq. Av. Nuevo León, colonia Villa Milpa Alta (interior Casa de Cultura CALMECAC)', '55 2580 7821', NULL, 19.192000, -99.019200, 12),
('Unidad Rosario Castellanos', 'Margarita 5 entre Geranio y Jacaranda, colonia Quiahuatla', '55 5266 8764', NULL, 19.283800, -99.009900, 13),
('Unidad Yaocíhuatl', 'Carretera Federal a Cuernavaca 2, colonia La Joya', '55 1707 6599', NULL, 19.282000, -99.205000, 14),
('Sede Santa Úrsula', 'Camino a Santa Úrsula 24, esq. Textitlán, colonia Santa Úrsula Xitla', '55 1707 6591', NULL, 19.299800, -99.151400, 14),
('Unidad Esperanza Brito de Martí', 'Prolongación Lucas Alamán 11, piso 1, colonia Del Parque, Venustiano Carranza', '55 1673 1905', NULL, 19.423200, -99.096700, 15),
('Unidad Laureana Wright González', 'Francisco I. Madero 11, colonia Barrio El Rosario, Xochimilco', '55 2208 5517', NULL, 19.260200, -99.104700, 16),
('Sede San Cristóbal', 'Dalia s/n, Plaza San Cristóbal, colonia Barrio San Cristóbal', '55 5161 6504', NULL, 19.257800, -99.106300, 16);


CREATE TABLE Abogados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    telefono VARCHAR(50),
    correo VARCHAR(100),
    costo VARCHAR(100),
    direccion TEXT,
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6)
);

INSERT INTO Abogados (nombre, telefono, correo, costo, direccion, latitud, longitud)
VALUES
('Facultad de Derecho - Mtra. Fabiola Patricia Lambarry Garzón', 'DESCONOCIDO', 'bufetejuridico@derecho.unam.mx', 'GRATUITO', 'Bufete Jurídico Sede CU', 19.3329, -99.1860),
('Fiscalía de Investigación de Delitos de Violencia de Género (FGJCDMX)', '55 5200 9000', 'DESCONOCIDO', 'GRATUITO', 'Sede Central de la Fiscalía (varias unidades)', 19.4326, -99.1332),
('Fiscalía Central de Investigación para la Atención del Delito de Trata de Personas', '55 5345 5067', 'DESCONOCIDO', 'GRATUITO', 'Dr. Vértiz 59, Col. Doctores, Cuauhtémoc, C.P. 06720.', 19.4258, -99.1458),
('Cuauhtémoc - LUNA Juana de Asbaje', '55 9131 5945', 'DESCONOCIDO', 'GRATUITO', 'Mina 205, Buenavista (Sótano del edificio de la Alcaldía).', 19.4474, -99.1510),
('Benito Juárez - Sede Eje Central', '55 5160 0039', 'DESCONOCIDO', 'GRATUITO', 'Eje Central Lázaro Cárdenas 695, piso 1, Narvarte Poniente.', 19.3927, -99.1537),
('Iztapalapa - Unidad Elena Poniatowska', '55 9131 0545', 'DESCONOCIDO', 'GRATUITO', 'Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella s/n.', 19.3518, -99.0660),
('Gustavo A. Madero - Sede La Joyita', '55 5035 1300', 'DESCONOCIDO', 'GRATUITO', 'Camellón de Oriente 95 y Norte 50, La Joyita.', 19.4868, -99.1145);


CREATE TABLE Psicologos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    telefono_contacto VARCHAR(50),
    correo_contacto VARCHAR(100),
    costo VARCHAR(100),
    direccion TEXT,
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6)
);

INSERT INTO Psicologos (nombre, telefono_contacto, correo_contacto, costo, direccion, latitud, longitud)
VALUES
('Centros de Formación y Servicios Psicológicos (CFSP)', 'DESCONOCIDO', 'DESCONOCIDO', 'Cuotas de recuperación (sujeto a valoración socioeconómica)', 'Circuito Ciudad Universitaria, C.U., 04510 Ciudad de México, CDMX', 19.3327, -99.1868),
('Programa de Atención Psicológica a Distancia (UNAM)', '55 5025 0855', 'DESCONOCIDO', 'GRATUITO', 'Servicio telefónico a distancia (No es exclusivo de CU)', 19.3333, -99.1845),
('Clínica Comunitaria Eleia', '5556612177', 'DESCONOCIDO', 'Cuotas ajustadas al ingreso (accesibles)', 'Av. Insurgentes Sur 1971, Plaza Inn, Álvaro Obregón, 01020 Ciudad de México', 19.3618, -99.1862),
('Centro Mexicano de Psicología Integrativa (CEMEPI)', '5595069766', 'DESCONOCIDO', '$450 a $500 MXN', 'Av. Insurgentes Sur 1677-Piso 8, Guadalupe Inn, Álvaro Obregón', 19.3610, -99.1845),
('Centro de Atención Psicológica Integral (CEPASI)', '55 2643 1318', 'contacto@ceapsi.mx', 'Individual/Infantil: $400 MXN. Pareja: $500 MXN.', 'C. Ote. 158 332, Moctezuma 2da Secc, Venustiano Carranza', 19.4298, -99.0973),
('Centros de Integración Juvenil (CIJ)', '5556133794', 'DESCONOCIDO', 'Especializados en adicciones y orientación general', 'Eje Vial 8 Sur, Ermita Iztapalapa 2206, Constitución de 1917, Iztapalapa', 19.3581, -99.0718),
('Línea SOS Mujeres CDMX', '*765', 'DESCONOCIDO', 'GRATUITO (Crisis inmediata 24/7)', 'DESCONOCIDO', NULL, NULL),
('Red Nacional de Refugios (RNR)', '800 822 4460', 'DESCONOCIDO', 'GRATUITO (Línea nacional)', 'DESCONOCIDO', NULL, NULL);