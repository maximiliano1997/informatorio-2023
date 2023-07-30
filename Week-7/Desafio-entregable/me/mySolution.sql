
CREATE DATABASE blog;
USE blog;

-- Creamos la tabla usuario
CREATE TABLE usuario(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    telefono INT,
    email VARCHAR(50) NOT NULL,
    contraseña VARCHAR(50) NOT NULL,
    estado BOOLEAN NOT NULL,
    fecha_creacion VARCHAR(50) NOT null,
    avatar BLOB NULL,
    es_publico BOOLEAN NOT NULL,
    es_colaborador BOOLEAN NOT NULL,
    es_admin BOOLEAN NOT NULL
);

-- Creamos la tabla ARTICULO
CREATE TABLE articulo (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usuario INT NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    resumen VARCHAR(100) NOT NULL,
    contenido TEXT NOT NULL,
    fecha_publicacion DATE NOT NULL,
    estado BOOLEAN,
    imagen BLOB NULL,
    FOREIGN KEY(id_usuario) REFERENCES usuario(id)
);


-- Creamos la tabla COMENTARIO

CREATE TABLE comentario (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_articulo INT NOT NULL,
    id_usuario INT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_hora DATETIME,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY(id_articulo) REFERENCES articulo(id),
    FOREIGN KEY(id_usuario) REFERENCES usuario(id)
);

-- Creamos la tabla CATEGORIA
CREATE TABLE categoria (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_categoria INT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    imagen BLOB NULL,
    estado BOOLEAN NOT NULL,
    FOREIGN KEY(id_categoria) REFERENCES categoria(id)
);


-- Creamos la tabla CATEGORIA_ARTICULO
CREATE TABLE categoria_articulo (
    id_articulo INT,
    id_categoria INT,
    FOREIGN KEY(id_articulo) REFERENCES articulo(id),
    FOREIGN KEY(id_categoria) REFERENCES categoria(id)
);


-- 1) Agregar el comando necesario que introduzca en la tabla usuario, 1 usuario con rol  de admin, 4 con rol de colaborador y 5 con rol de público. Donde los campos: es_publico, es_colaborador y es_admin son booleanos.

INSERT INTO usuario (nombre, telefono, email, contraseña, estado, fecha_creacion, avatar, es_publico, es_colaborador, es_admin)
VALUES ('Imanol', 3624701651, 'imanolaguer1@gmail.com', 'lol1997', True, '12/03/12', NULL, False, False, True),
('Maximo', 3624987565, 'maximo3ro@hotmail.com', 'mxi000', False, '12/05/15', NULL, False, True, False),
('Santino', 3624666162, 'santi666@gmail.com', 'sanso96', True, '02/12/21', NULL, False, True, False),
('Lucas', 3624055596, 'luquita@gmail.com', 'luca12', False, '05/03/22', NULL, False, True, False),
('Patricio', 362488020, 'patriloco@gmail.com', 'ptmloco', False, '05/07/22', NULL, False, True, False),
('Alejandro', 3624005577, 'ale12@gmail.com', 'alej12', False, '05/12/22', NULL, True, False, False),
('Mariela', 3725769625, 'mariSGO@gmail.com', 'mariela1990', False, '05/02/23', NULL, True, False, False),
('Ana', 3725769625, 'anasol@gmail.com', 'anasolicia0', False, '05/03/23', NULL, True, False, False),
('Maximiliano', 3624701651, 'imanolaguer2010@hotmail.com', 'aguero99', False, '05/03/23', NULL, True, False, False),
('Graciela', 3624701651, 'gracielasss@hotmail.com', 'chela87', False, '05/05/23', NULL, True, False, False);

SELECT * FROM usuario;

-- 2) Agregar el comando necesario para actualizar el rol a admin de uno de los usuarios agregado con rol de colaborador

UPDATE usuario
SET es_colaborador = False,es_admin = True
WHERE id = 3;

SELECT * FROM usuario;

-- 3) Agregar el comando necesario que introduzca en la tabla articulo, 3 articulos con estado TRUE y uno con estado FALSE. Donde el campo estado en todas las tablas es Booleano.

INSERT INTO articulo(id_usuario, titulo, resumen, contenido, fecha_publicacion, estado, imagen)
VALUES (2, 'Cadena De Oro', 'Resumen....1', 'contenido1', '12-02-22', True, NULL), 
       (3, 'Pajaros Locos', 'Resumen....2', 'contenido2', '12-02-22', True, NULL),
       (4, 'Amazonas', 'Resumen....3', 'contenido3', '12-02-22', True, NULL),
       (5, 'Kendra Lust', 'Resumen....4', 'contenido4', '12-02-22', False, NULL);


-- 3) Agregar el comando necesario para eliminar el articulo que tenga estado FALSE.

SET SQL_SAFE_UPDATES=0;

DELETE FROM articulo 
WHERE estado = False;

SELECT * FROM articulo;

-- 4) Agregar el comando necesario que introduzca 3 comentarios al primar articulo

INSERT INTO comentario (id_articulo, id_usuario, contenido, fecha_hora, estado)
VALUES (1, 2, 'Comentario1', '2022-06-24 09:15:00', True),
       (1, 3, 'Comentario2', '2022-11-15 14:30:45', True),
       (1, 2, 'Comentario2', '2022-12-02 18:20:30', True),
       (2, 4, 'Comentario2', '2023-08-10 11:45:15', True),
       (2, 5, 'Comentario2', '2023-12-31 23:59:59', True);

SELECT * FROM COMENTARIO;

-- 5) Agregar el comando necesario para listar todos los articulos que tengan comentarios, mostrando el titulo del articulo, la fecha_publicacion del articulo, el nombre del usuario que realizo el comentario y la fecha_hora que realizo dicho comentario, agrupados por articulos.

SELECT art.titulo, art.fecha_publicacion AS fechaDePublicacion, us.nombre AS nombreUsuario, cto.fecha_hora AS fechaHora FROM articulo as art
INNER JOIN comentario AS cto ON art.id = cto.id_articulo
INNER JOIN usuario AS us ON us.id = cto.id_usuario
ORDER BY art.id;

-- SELECT titulo, fecha_publicacion, usuario.nombre as nombreUsuario, fecha_hora FROM articulo, usuario, comentario
-- WHERE (articulo.id = comentario.id_articulo) and (articulo.id_usuario = usuario.id)
-- GROUP BY articulo.id