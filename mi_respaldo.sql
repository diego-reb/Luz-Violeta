--
-- PostgreSQL database dump
--

-- Dumped from database version 17.5
-- Dumped by pg_dump version 17.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: abogados; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.abogados (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    telefono character varying(50),
    correo character varying(100),
    costo character varying(100),
    direccion text,
    latitud numeric(10,6),
    longitud numeric(10,6)
);


--
-- Name: abogados_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.abogados_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: abogados_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.abogados_id_seq OWNED BY public.abogados.id;


--
-- Name: albergues; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.albergues (
    id integer NOT NULL,
    nombre character varying(150) NOT NULL,
    direccion text,
    telefono character varying(50),
    codigo_postal character varying(10),
    latitud numeric(10,6),
    longitud numeric(10,6),
    id_alcaldia integer,
    capacidad_total integer,
    capacidad_ocupada integer DEFAULT 0
);


--
-- Name: albergues_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.albergues_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: albergues_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.albergues_id_seq OWNED BY public.albergues.id;


--
-- Name: alcaldias; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.alcaldias (
    id integer NOT NULL,
    nombre character varying(100) NOT NULL,
    clave_inegi character varying(10)
);


--
-- Name: alcaldias_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.alcaldias_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: alcaldias_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.alcaldias_id_seq OWNED BY public.alcaldias.id;


--
-- Name: psicologos; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.psicologos (
    id integer NOT NULL,
    nombre character varying(200) NOT NULL,
    telefono_contacto character varying(50),
    correo_contacto character varying(100),
    costo character varying(100),
    direccion text,
    latitud numeric(10,6),
    longitud numeric(10,6)
);


--
-- Name: psicologos_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.psicologos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: psicologos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.psicologos_id_seq OWNED BY public.psicologos.id;


--
-- Name: roles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.usuarios (
    id_usuario integer NOT NULL,
    nombre character varying(100) NOT NULL,
    correo character varying(100) NOT NULL,
    contrasena character varying(200) NOT NULL,
    nombre_usuario character varying(100),
    activo boolean DEFAULT true,
    rol_id integer
);


--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.usuarios_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.usuarios_id_usuario_seq OWNED BY public.usuarios.id_usuario;


--
-- Name: abogados id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abogados ALTER COLUMN id SET DEFAULT nextval('public.abogados_id_seq'::regclass);


--
-- Name: albergues id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.albergues ALTER COLUMN id SET DEFAULT nextval('public.albergues_id_seq'::regclass);


--
-- Name: alcaldias id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alcaldias ALTER COLUMN id SET DEFAULT nextval('public.alcaldias_id_seq'::regclass);


--
-- Name: psicologos id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.psicologos ALTER COLUMN id SET DEFAULT nextval('public.psicologos_id_seq'::regclass);


--
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: usuarios id_usuario; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuarios_id_usuario_seq'::regclass);


--
-- Data for Name: abogados; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.abogados (id, nombre, telefono, correo, costo, direccion, latitud, longitud) FROM stdin;
1	Facultad de Derecho - Mtra. Fabiola Patricia Lambarry Garzón	DESCONOCIDO	bufetejuridico@derecho.unam.mx	GRATUITO	Bufete Jurídico Sede CU	19.332900	-99.186000
2	Fiscalía de Investigación de Delitos de Violencia de Género (FGJCDMX)	55 5200 9000	DESCONOCIDO	GRATUITO	Sede Central de la Fiscalía (varias unidades)	19.432600	-99.133200
3	Fiscalía Central de Investigación para la Atención del Delito de Trata de Personas	55 5345 5067	DESCONOCIDO	GRATUITO	Dr. Vértiz 59, Col. Doctores, Cuauhtémoc, C.P. 06720.	19.425800	-99.145800
4	Cuauhtémoc - LUNA Juana de Asbaje	55 9131 5945	DESCONOCIDO	GRATUITO	Mina 205, Buenavista (Sótano del edificio de la Alcaldía).	19.447400	-99.151000
5	Benito Juárez - Sede Eje Central	55 5160 0039	DESCONOCIDO	GRATUITO	Eje Central Lázaro Cárdenas 695, piso 1, Narvarte Poniente.	19.392700	-99.153700
6	Iztapalapa - Unidad Elena Poniatowska	55 9131 0545	DESCONOCIDO	GRATUITO	Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella s/n.	19.351800	-99.066000
7	Gustavo A. Madero - Sede La Joyita	55 5035 1300	DESCONOCIDO	GRATUITO	Camellón de Oriente 95 y Norte 50, La Joyita.	19.486800	-99.114500
\.


--
-- Data for Name: albergues; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.albergues (id, nombre, direccion, telefono, codigo_postal, latitud, longitud, id_alcaldia, capacidad_total, capacidad_ocupada) FROM stdin;
1	Unidad Elena Poniatowska en Iztapalapa	Centro Social Villa Estrella Módulo 4, Camino Cerro de la Estrella colonia el Santuario Aculco	55 9131 0545	\N	19.351890	-99.066200	9	\N	0
2	Casa de las Siempre Vivas, antes Módulo De Atención A La Mujer	Paraje San Juan, El Vergel #24, Francisco Villa, Iztapalapa	Desconocido	\N	19.354200	-99.067900	9	\N	0
3	Centro de Atención Para Mujeres Maltratadas A.c. Muuknequi	Dr. Jimenez 114-Interior 10, Doctores, Cuauhtémoc	55 5761 9684	\N	19.425700	-99.146000	6	\N	0
4	Casa de la Mujer	Parcialidad 11, Peralvillo, Morelos, Cuauhtémoc	Desconocido	\N	19.445800	-99.134000	6	\N	0
5	Centro de Atención a la violencia Intrafamiliar C.A.V.I.	Calle Gral. Gabriel Hernández 56, Doctores, Cuauhtémoc	55 5345 5229	\N	19.425000	-99.145800	6	\N	0
6	Unión Nacional de Mujeres Mexicanas	Topacio 4, Centro Histórico de la Cdad. de México, Centro, Cuauhtémoc	55 5522 6326	\N	19.432600	-99.133200	6	\N	0
7	Ministerios De Amor Ac	Actipan 16, Insurgentes Mixcoac, Benito Juárez	55 5611 1111	\N	19.377300	-99.177400	3	\N	0
8	Luna	Camino Cerro de la Estrella s/n Centro Social Villa Estrella, Módulo 4 El Santuario, Aculco, Iztapalapa	Desconocido	\N	19.351800	-99.066000	9	\N	0
9	Unidad Benita Galeana en Benito Juárez	Eje Central Lázaro Cárdenas 695, piso 1, colonia Narvarte Poniente, alcaldía Benito Juárez	55 5160 0039‬	\N	19.392700	-99.153700	3	\N	0
10	LUNA Benita Galeana	Eje 5 Sur Ramos Millán 95, colonia Niños Héroes de Chapultepec	55 2124 4929‬	\N	19.386800	-99.148000	3	\N	0
11	Unidad Juana de Asbaje en Cuauhtémoc	Aldama, Violeta y Mina s/n, sótano edificio de la alcaldía, colonia Buenavista	5591315945	\N	19.447400	-99.151000	6	\N	0
12	LUNA Cihual in Calli – Mercado. Secretaría de las Mujeres	Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro	55 1549 1512	\N	19.192900	-99.021500	12	\N	0
13	Albergue Casa Madre Teresa	Allende 55, Rosas del Tepeyac, Gustavo A. Madero	55 5781 3647	\N	19.486800	-99.114500	7	\N	0
14	Unidad Marcela Lagarde en Azcapotzalco	Av. 22 de febrero 421, colonia Barrio de San Marcos	55 1716 0998	\N	19.481600	-99.186700	2	\N	0
15	Unidad Amparo Ochoa en Cuajimalpa	Prolongación 16 de septiembre s/n casi esquina Av. Veracruz, colonia Contadero	55 5813 5000	\N	19.358000	-99.285000	5	\N	0
16	Sede Castorena	José María Castorena 187, colonia Cuajimalpa	55 9131 9552	\N	19.360500	-99.286200	5	\N	0
17	Sede Agrícola Oriental	Av. Sur 8, s/n, casi con Av. Javier Rojo Gómez (atrás del deportivo Leandro Valle), colonia Agrícola Oriental	55 2063 2369	\N	19.395700	-99.091900	8	\N	0
18	Unidad Cristina Pacheco	Piaztic s/n (frente a secundaria 262), colonia San José Atacaxco	55 9134 7709	\N	19.327200	-99.243900	10	\N	0
19	Sede Observatorio	Av. Observatorio s/n esq. General José María Mendívil, colonia Daniel Garza	55 1715 6328	\N	19.400400	-99.200600	11	\N	0
20	Unidad Cihual in Calli	Calle Yucatán s/n esq. Calle Constitución, colonia Villa Milpa Alta Centro	55 2127 4515	\N	19.192800	-99.021400	12	\N	0
21	Sede Calmecac	Av. Puebla 250, esq. Av. Nuevo León, colonia Villa Milpa Alta (interior Casa de Cultura CALMECAC)	55 2580 7821	\N	19.192000	-99.019200	12	\N	0
22	Unidad Rosario Castellanos	Margarita 5 entre Geranio y Jacaranda, colonia Quiahuatla	55 5266 8764	\N	19.283800	-99.009900	13	\N	0
23	Unidad Yaocíhuatl	Carretera Federal a Cuernavaca 2, colonia La Joya	55 1707 6599	\N	19.282000	-99.205000	14	\N	0
24	Sede Santa Úrsula	Camino a Santa Úrsula 24, esq. Textitlán, colonia Santa Úrsula Xitla	55 1707 6591	\N	19.299800	-99.151400	14	\N	0
25	Unidad Esperanza Brito de Martí	Prolongación Lucas Alamán 11, piso 1, colonia Del Parque, Venustiano Carranza	55 1673 1905	\N	19.423200	-99.096700	15	\N	0
26	Unidad Laureana Wright González	Francisco I. Madero 11, colonia Barrio El Rosario, Xochimilco	55 2208 5517	\N	19.260200	-99.104700	16	\N	0
27	Sede San Cristóbal	Dalia s/n, Plaza San Cristóbal, colonia Barrio San Cristóbal	55 5161 6504	\N	19.257800	-99.106300	16	\N	0
\.


--
-- Data for Name: alcaldias; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.alcaldias (id, nombre, clave_inegi) FROM stdin;
1	Álvaro Obregón	09010
2	Azcapotzalco	09020
3	Benito Juárez	09030
4	Coyoacán	09040
5	Cuajimalpa de Morelos	09050
6	Cuauhtémoc	09060
7	Gustavo A. Madero	09070
8	Iztacalco	09080
9	Iztapalapa	09090
10	La Magdalena Contreras	09100
11	Miguel Hidalgo	09110
12	Milpa Alta	09120
13	Tláhuac	09130
14	Tlalpan	09140
15	Venustiano Carranza	09150
16	Xochimilco	09160
\.


--
-- Data for Name: psicologos; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.psicologos (id, nombre, telefono_contacto, correo_contacto, costo, direccion, latitud, longitud) FROM stdin;
1	Centros de Formación y Servicios Psicológicos (CFSP)	DESCONOCIDO	DESCONOCIDO	Cuotas de recuperación (sujeto a valoración socioeconómica)	Circuito Ciudad Universitaria, C.U., 04510 Ciudad de México, CDMX	19.332700	-99.186800
2	Programa de Atención Psicológica a Distancia (UNAM)	55 5025 0855	DESCONOCIDO	GRATUITO	Servicio telefónico a distancia (No es exclusivo de CU)	19.333300	-99.184500
3	Clínica Comunitaria Eleia	5556612177	DESCONOCIDO	Cuotas ajustadas al ingreso (accesibles)	Av. Insurgentes Sur 1971, Plaza Inn, Álvaro Obregón, 01020 Ciudad de México	19.361800	-99.186200
4	Centro Mexicano de Psicología Integrativa (CEMEPI)	5595069766	DESCONOCIDO	$450 a $500 MXN	Av. Insurgentes Sur 1677-Piso 8, Guadalupe Inn, Álvaro Obregón	19.361000	-99.184500
5	Centro de Atención Psicológica Integral (CEPASI)	55 2643 1318	contacto@ceapsi.mx	Individual/Infantil: $400 MXN. Pareja: $500 MXN.	C. Ote. 158 332, Moctezuma 2da Secc, Venustiano Carranza	19.429800	-99.097300
6	Centros de Integración Juvenil (CIJ)	5556133794	DESCONOCIDO	Especializados en adicciones y orientación general	Eje Vial 8 Sur, Ermita Iztapalapa 2206, Constitución de 1917, Iztapalapa	19.358100	-99.071800
7	Línea SOS Mujeres CDMX	*765	DESCONOCIDO	GRATUITO (Crisis inmediata 24/7)	DESCONOCIDO	\N	\N
8	Red Nacional de Refugios (RNR)	800 822 4460	DESCONOCIDO	GRATUITO (Línea nacional)	DESCONOCIDO	\N	\N
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.roles (id, nombre) FROM stdin;
1	Administrador
2	Usuaria
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.usuarios (id_usuario, nombre, correo, contrasena, nombre_usuario, activo, rol_id) FROM stdin;
2	Diego Zaid Garcia Rebollo 	dzgarcia10@gmail.com	scrypt:32768:8:1$skw6icU0aTBlxd4U$56c4db7e42851b7875570e2a62c7a67ced6c4944d73cd38fb6d738fdffcd76e89e7b9521fad2775c4936ea9eec3e238fa5b14fc018c80ca9d11d6af63a901589	diego-reb	t	1
3	Diego Zaid Garcia Rebollo 	dzgr@gmail.com	scrypt:32768:8:1$wZn1ZZFqZxnhE4eo$153e1e155da09502e56aa637358b71faf766e777297a4191972203ab164cdf187e3d5c9f52b26de40073881fa07e85b48073026108379ab16e548b3f19f45a0e	diegoreb	t	1
4	norma	norma@gmail.com	scrypt:32768:8:1$S8gVOsBDPq6PSgH9$6dc464ec1018d2dd0528ed584c8768cfd4536f2b82206e860d3528642da03d0fb8d09992e47ee011d6df682a02b43a00f0962610c30b361b4705323a29914da4	norma	t	1
5	norma	normajimenezmartinez04@gmail.com	scrypt:32768:8:1$STlO0apsAYuzUcZK$f7d880413dea8c58299caace9803c4f258266a8c36fd2d41cc41b8a281c358d70129d96d1245ead3d2940efdd4598f9e26539835df9964e84d8f8286f12b3eed	norma2	t	2
6	Fabiola	fabigante@gmail.com	scrypt:32768:8:1$639w16HKa1gPVsBr$bf2efacf16e94b3250241062ed78162774590a7d291f05c7b6da0250335684e9f0d1856ab2d3cfec8d12950dcc43f4573c0cb9020f037c92aeb0d1bfd1beb43c	fabis	t	1
1	Diego Zaid García Rebollo	dzgarciar10@gmail.com	scrypt:32768:8:1$ZoOoxYt7xF1UyLsm$8c474a193cfd8b080247b57054a6bb856b3aa0556fbfc07a45b559b292c97a89f1b07016cc9e5130b8bb9f343cf8e035fa25040e83e420a6df237120bd7c6970	diego_reb	t	2
\.


--
-- Name: abogados_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.abogados_id_seq', 7, true);


--
-- Name: albergues_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.albergues_id_seq', 27, true);


--
-- Name: alcaldias_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.alcaldias_id_seq', 16, true);


--
-- Name: psicologos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.psicologos_id_seq', 8, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.roles_id_seq', 2, true);


--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.usuarios_id_usuario_seq', 6, true);


--
-- Name: abogados abogados_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.abogados
    ADD CONSTRAINT abogados_pkey PRIMARY KEY (id);


--
-- Name: albergues albergues_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.albergues
    ADD CONSTRAINT albergues_pkey PRIMARY KEY (id);


--
-- Name: alcaldias alcaldias_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.alcaldias
    ADD CONSTRAINT alcaldias_pkey PRIMARY KEY (id);


--
-- Name: psicologos psicologos_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.psicologos
    ADD CONSTRAINT psicologos_pkey PRIMARY KEY (id);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: usuarios usuarios_correo_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_correo_key UNIQUE (correo);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario);


--
-- Name: albergues albergues_id_alcaldia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.albergues
    ADD CONSTRAINT albergues_id_alcaldia_fkey FOREIGN KEY (id_alcaldia) REFERENCES public.alcaldias(id);


--
-- Name: usuarios usuarios_rol_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_rol_id_fkey FOREIGN KEY (rol_id) REFERENCES public.roles(id);


--
-- PostgreSQL database dump complete
--

