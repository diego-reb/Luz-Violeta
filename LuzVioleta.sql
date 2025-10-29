CREATE TABLE Roles (
    id_rol SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contrasena VARCHAR(200) NOT NULL,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    rol_id INT REFERENCES Roles(id_rol)
);

CREATE TABLE Alcaldias (
    id_alcaldia SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    clave_inegi VARCHAR(20) UNIQUE
);

CREATE TABLE Visitas_pagina (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuarios(id_usuario) ON DELETE SET NULL,
    ip_address INET NOT NULL,
    fecha_visita TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Boton_ayuda (
    id_boton SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES Usuarios(id_usuario) ON DELETE SET NULL,
    tipo_ayuda VARCHAR(100) NOT NULL,
    ubicacion_lat DECIMAL(10,6),
    ubicacion_log DECIMAL(10,6),
    id_alcaldia INT REFERENCES Alcaldias(id_alcaldia),
    fecha_presion TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Centros_ayuda (
    id_centro SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    tipo VARCHAR(100),
    direccion VARCHAR(200),
    id_alcaldia INT REFERENCES Alcaldias(id_alcaldia),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    horario VARCHAR(100),
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6),
    activo BOOLEAN DEFAULT TRUE,
    id_inegi VARCHAR(50),
    fecha_actualizacion DATE
);

CREATE TABLE Psicologos (
    id_psicologo SERIAL PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    especialidad VARCHAR(100),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    id_alcaldia INT REFERENCES Alcaldias(id_alcaldia),
    direccion_consultorio VARCHAR(200),
    horario_atencion VARCHAR(100),
    costo NUMERIC(10,2),
    cedula_profesional VARCHAR(50) UNIQUE,
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Ayuda_legal (
    id_ayuda SERIAL PRIMARY KEY,
    nombre_organizacion VARCHAR(150) NOT NULL,
    tipo_ayuda VARCHAR(100),
    direccion VARCHAR(200),
    id_alcaldia INT REFERENCES Alcaldias(id_alcaldia),
    telefono VARCHAR(20),
    correo VARCHAR(100),
    horario_atencion VARCHAR(100),
    costo NUMERIC(10,2),
    activo BOOLEAN DEFAULT TRUE
);
select * from usuarios

ALTER TABLE Centros_ayuda
ALTER COLUMN fecha_actualizacion TYPE TIMESTAMP;

ALTER TABLE Centros_ayuda
ADD COLUMN fuente VARCHAR(100) DEFAULT 'INEGI';
