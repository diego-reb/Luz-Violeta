CREATE TABLE Usuarias (
    usuaria_id SERIAL PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    edad INTEGER ,
    activo BOOLEAN DEFAULT TRUE,
	correo VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(20) UNIQUE
);

CREATE TABLE Albergues (
    albergue_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    codigo_postal VARCHAR(10),
    id_alcaldia INTEGER,
    FOREIGN KEY (id_alcaldia) REFERENCES alcaldia (alcaldia_id)
);
drop table Albergues

CREATE TABLE Abogados (
    abogado_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    activo BOOLEAN DEFAULT TRUE,
    costo VARCHAR(255),         
    direccion VARCHAR(255)      
);

 
CREATE TABLE Psicologos (
    psicologo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono_contacto VARCHAR(20),
    correo_contacto VARCHAR(100), 
	costo VARCHAR(255), 
    activo BOOLEAN DEFAULT TRUE,
	direccion VARCHAR(255)  
);

CREATE TABLE alcaldia (
    alcaldia_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);


INSERT INTO Albergues (nombre, direccion, telefono, id_alcaldia) VALUES
('Unidad Elena Poniatowska en Iztapalapa', 'Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella colonia el Santuario Aculco', '55 9131 0545', 9 ),
('Casa de las Siempre Vivas, antes Módulo De Atención A La Mujer ', 'Paraje San Juan, El Vergel #24, Francisco Villa, Iztapalapa', 'Desconocido', 9),
('Centro de Atención Para Mujeres Maltratadas A.c. Muuknequi', 'Dr. Jimenez 114-Interior 10, Doctores, Cuauhtémoc', ' 55 5761 9684',6),
('Casa de la Mujer', 'Parcialidad 11, Peralvillo, Morelos, Cuauhtémoc', 'Desconocido', 6),
('Centro de Atención a la violencia Intrafamiliar C.A.V.I.', ' Calle Gral. Gabriel Hernández 56, Doctores, Cuauhtémoc', '55 5345 5229',6),
('Unión Nacional de Mujeres Mexicanas', ' Topacio 4, Centro Histórico de la Cdad. de México, Centro, Cuauhtémoc', '55 5522 6326',6),
('Centro de Atención Para Mujeres Maltratadas A.c. Muuknequi', ' Dr. Jimenez 114-Interior 10, Doctores, Cuauhtémoc', ' 55 5761 9684',6),
('Ministerios De Amor Ac', ' Actipan 16, Insurgentes Mixcoac, Benito Juárez', '55 5611 1111', 3),
('Luna ', ' Camino Cerro de la Estrella s/n Centro Social Villa Estrella, Módulo 4 El Santuario, Aculco, Iztapalapa', 'Desconocido', 9),
('Unidad Benita Galeana en Benito Juárez', 'Eje Central Lázaro Cárdenas 695, piso 1, colonia Narvarte Poniente, alcaldía Benito Juárez,', '55 5160 0039‬',3),
('LUNA Benita Galeana', 'Eje 5 Sur Ramos Millán 95, colonia Niños Héroes de Chapultepec,', '55 2124 4929‬', 3 ),
('Unidad Juana de Asbaje en Cuauhtémoc', ' Aldama, Violeta y Mina s/n, sótano edificio de la alcaldía, colonia Buenavista, alcaldía Cuauhtémoc', '5591315945', 6),
('LUNA Cihual in Calli – Mercado. Secretaría de las Mujeres', 'Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro, alcaldía Milpa Alta (arriba del mercado Benito Juárez', '55 1549 1512',3),
('Albergue Casa Madre Teresa', 'Allende 55, Rosas del Tepeyac, Gustavo A. Madero', '55 5781 3647',7),
('Unidad Marcela Lagarde en Azcapotzalco', ' Av. 22 de febrero 421, colonia Barrio de San Marcos, alcaldía Azcapotzalco','55 1716 0998',2),
('Unidad Amparo Ochoa en Cuajimalpa', 'Prolongación 16 de septiembre s/n casi esquina Av. Veracruz, colonia Contadero, alcaldía Cuajimalpa de Morelos','55 5813 5000 ',5),
('Sede Castorena', 'José María Castorena 187, colonia Cuajimalpa, alcaldía Cuajimalpa de Morelos','55 9131 9552',5),
('Sede Agrícola Oriental', 'Av. Sur 8, s/n, casi con Av. Javier Rojo Gómez (atrás del deportivo Leandro Valle), colonia Agrícola Oriental, alcaldía Iztacalco', '55 2063 2369',8),
('Unidad Cristina Pacheco',' Piaztic s/n (frente a secundaria 262), colonia San José Atacaxco, alcaldía La Magdalena Contreras',' 55 9134 7709',10),
('Sede Observatorio', 'Av. Observatorio s/n esq. General José María Mendívil, colonia Daniel Garza, alcaldía Miguel Hidalgo', ' 55 1715 6328 ',11),
('Unidad Cihual in Calli ', 'Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro, alcaldía Milpa Alta', '55 2127 4515',12),
('Sede Calmecac', 'Av. Puebla 250, esq. Av. Nuevo León, colonia Villa Milpa Alta, alcaldía Milpa Alta (interiror Casa de Cultura CALMECAC)', '55 2580 7821 ',12),
('Unidad Rosario Castellanos', 'Margarita 5 entre Geranio y Jacaranda, colonia Quiahuatla, alcaldía Tláhuac', '55 5266 8764',13),
('Unidad Yaocíhuatl ', 'Carretera Federal a Cuernavaca 2, colonia La Joya, alcaldía Tlalpan', '55 1707 6599',14),
('Sede Santa Úrsula', 'Camino a Santa Úrsula 24, esq. Textitlán, colonia Santa Úrsula Xitla, alcaldía Tlalpan', ' 55 1707 6591',14),
('Unidad Esperanza Brito de Martí ', 'Prolongación Lucas Alamán 11, piso 1, colonia Del Parque, alcaldía Venustiano Carranza', '55 1673 1905',15),
('Unidad Laureana Wright González', 'Francisco I. Madero 11, colonia Barrio El Rosario, alcaldía Xochimilco', ' 55 2208 5517 ',16),
('Sede San Cristóbal', ' Dalia s/n, Plaza San Cristóbal, colonia Barrio San Cristóbal, alcaldía Xochimilco', '55 5161 6504',16);

INSERT INTO alcaldia (nombre) VALUES
('Álvaro Obregón'),
('Azcapotzalco'),
('Benito Juárez'),
('Coyoacán'),
('Cuajimalpa de Morelos'),
('Cuauhtémoc'),
('Gustavo A. Madero'),
('Iztacalco'),
('Iztapalapa'), 
('La Magdalena Contreras'),
('Miguel Hidalgo'),
('Milpa Alta'),
('Tláhuac'),
('Tlalpan'),
('Venustiano Carranza'),
('Xochimilco');



INSERT INTO Psicologos (nombre, telefono_contacto, correo_contacto, costo, activo, direccion) VALUES
('Centros de Formación y Servicios Psicológicos (CFSP)', 'DESCONOCIDO', 'DESCONOCIDO', 'Cuotas de recuperación (sujeto a valoración socioeconómica)', TRUE, $$Circuito Ciudad Universitaria, C.U., 04510 Ciudad de México, CDMX 19°20'06.6"N 99°11'20.5"W$$),
('Programa de Atención Psicológica a Distancia (UNAM)', '55 5025 0855', 'DESCONOCIDO', 'GRATUITO', TRUE, 'Servicio telefónico a distancia (No es exclusivo de CU)'),
('Clínica Comunitaria Eleia', '5556612177', 'DESCONOCIDO', 'Cuotas de recuperación ajustadas al ingreso (accesibles)', TRUE, $$Av. Insurgentes Sur 1971-Piso 3, Plaza Inn, Álvaro Obregón, 01020 Ciudad de México, CDMX 19°21'07.2"N 99°11'13.3"W$$),
('Centro Mexicano de Psicología Integrativa (CEMEPI)', '5595069766', 'DESCONOCIDO', '$450 a $500 MXN', TRUE, $$Av. Insurgentes Sur 1677-Piso 8, Guadalupe Inn, Álvaro Obregón, 01020 Ciudad de México, CDMX 19°21'40.8"N 99°11'01.4"W$$),
('Centro de Atención Psicológica Integral (CEPASI)', '55 2643 1318', 'contacto@ceapsi.mx', 'Individual/Infantil: $400 MXN. Pareja: $500 MXN.', TRUE, 'C. Ote. 158 332, Moctezuma 2da Secc, Venustiano Carranza, 15530 Ciudad de México, CDMX'),
('Centros de Integración Juvenil (CIJ)', '5556133794', 'DESCONOCIDO', 'Entre: Especializados en adicciones y orientación general', TRUE, $$Eje Vial 8 Sur, Ermita Iztapalapa 2206, Constitución de 1917, Iztapalapa, 09260 Ciudad de México, CDMX 19°20'50.1"N 99°03'09.2"W$$),
('Línea SOS Mujeres CDMX', '*765', 'DESCONOCIDO', 'GRATUITO (Crisis inmediata 24/7)', TRUE, 'DESCONOCIDO'),
('Red Nacional de Refugios (RNR)', '800 822 4460', 'DESCONOCIDO', 'GRATUITO (Línea nacional)', TRUE, 'DESCONOCIDO');

INSERT INTO Abogados (nombre, telefono, correo, costo, direccion) VALUES
('Facultad de Derecho - Mtra. Fabiola Patricia Lambarry Garzón', 'DESCONOCIDO', 'bufetejuridico@derecho.unam.mx', 'GRATUITO', 'Bufete Jurídico Sede CU'),
('Fiscalía de Investigación de Delitos de Violencia de Género (FGJCDMX)', '55 5200 9000 (Central de la Fiscalía)', 'DESCONOCIDO', 'GRATUITO', 'Sede Central de la Fiscalía (varias unidades)'),
('Fiscalía Central de Investigación para la Atención del Delito de Trata de Personas', '55 5345 5067 / 55 5345 5068', 'DESCONOCIDO', 'GRATUITO', 'Dr. Vértiz 59, Col. Doctores, Cuauhtémoc, C.P. 06720.'),
('Cuauhtémoc - LUNA Juana de Asbaje', '55 9131 5945', 'DESCONOCIDO', 'GRATUITO', 'Mina 205, Buenavista (Sótano del edificio de la Alcaldía).'),
('Benito Juárez - Sede Eje Central', '55 5160 0039', 'DESCONOCIDO', 'GRATUITO', 'Eje Central Lázaro Cárdenas 695, piso 1, Narvarte Poniente.'),
('Iztapalapa - Unidad Elena Poniatowska', '55 9131 0545', 'DESCONOCIDO', 'GRATUITO', 'Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella s/n.'),
('Gustavo A. Madero - Sede La Joyita', '55 5035 1300', 'DESCONOCIDO', 'GRATUITO', 'Camellón de Oriente 95 y Norte 50, La Joyita.');


DROP TABLE psicologos;

ALTER TABLE Abogados ALTER COLUMN telefono TYPE VARCHAR(50);