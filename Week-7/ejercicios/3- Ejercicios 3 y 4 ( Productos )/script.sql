-- Ejercicio 3:
-- Dado el siguiente diseño de BD "Productos"



-- Punto 1
-- Crear la BD con el esquema establecido....
CREATE DATABASE Productos;
USE Productos;

CREATE TABLE fabricante(
  codigo_fabricante INT(10) PRIMARY KEY,
  nombre VARCHAR(50)
);

CREATE TABLE producto(
  codigo_producto INT (10) NOT NULL PRIMARY KEY,
  nombre VARCHAR(50),
  precio INT,
  codigo_fabricante INT (10) NOT NULL,
  FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo_fabricante)
);

-- Punto 2
-- Insertar datos a las tablas utilizando estas sentencias.
INSERT INTO fabricante VALUES(1, 'Asus');
INSERT INTO fabricante VALUES(2, 'Lenovo');
INSERT INTO fabricante VALUES(3, 'Hewlett-Packard');
INSERT INTO fabricante VALUES(4, 'Samsung');
INSERT INTO fabricante VALUES(5, 'Seagate');
INSERT INTO fabricante VALUES(6, 'Crucial');
INSERT INTO fabricante VALUES(7, 'Gigabyte');
INSERT INTO fabricante VALUES(8, 'Huawei');
INSERT INTO fabricante VALUES(9, 'Xiaomi');

INSERT INTO producto VALUES(1, 'Disco duro SATA3 1TB', 86.99, 5);
INSERT INTO producto VALUES(2, 'Memoria RAM DDR4 8GB', 120, 6);
INSERT INTO producto VALUES(3, 'Disco SSD 1 TB', 150.99, 4);
INSERT INTO producto VALUES(4, 'GeForce GTX 1050Ti', 185, 7);
INSERT INTO producto VALUES(5, 'GeForce GTX 1080 Xtreme', 755, 6);
INSERT INTO producto VALUES(6, 'Monitor 24 LED Full HD', 202, 1);
INSERT INTO producto VALUES(7, 'Monitor 27 LED Full HD', 245.99, 1);
INSERT INTO producto VALUES(8, 'Portátil Yoga 520', 559, 2);
INSERT INTO producto VALUES(9, 'Portátil Ideapd 320', 444, 2);
INSERT INTO producto VALUES(10, 'Impresora HP Deskjet 3720', 59.99, 3);
INSERT INTO producto VALUES(11, 'Impresora HP Laserjet Pro M26nw', 180, 3);


-- Ejercicio 4: Productos
-- Teniendo en cuenta la BD creada, denominada "Productos", resolver las siguientes cuestiones:

-- Punto 1:
-- Lista el nombre de todos los productos que hay en la tabla producto.

SELECT nombre FROM producto;


-- Punto 2:
-- Lista todas las columnas de la tabla producto.

SELECT * FROM producto;


-- Punto 3:
-- Lista el nombre de los productos y el precio en USD.

SELECT nombre, precio as U$D_Precio FROM producto;

-- Punto 4:
-- Lista los nombres y los precios de todos los productos de la tabla producto, convirtiendo los nombres a mayúscula.

SELECT UPPER(nombre) as nombre, precio FROM producto;

-- Punto 5:
-- Lista los nombres y los precios de todos los productos de la tabla producto, redondeando el valor del precio.

SELECT nombre, ROUND(precio) FROM producto;


-- Punto 6:
-- Lista el código de los fabricantes que tienen productos en la tabla producto.

SELECT codigo_fabricante 
FROM producto 
WHERE codigo_fabricante IN (SELECT codigo_fabricante FROM fabricante);

-- Punto 7:
-- Lista el código de los fabricantes que tienen productos en la tabla producto, eliminando los códigos que aparecen repetidos

SELECT DISTINCT codigo_fabricante 
FROM producto 
WHERE codigo_fabricante IN (SELECT codigo_fabricante FROM fabricante);


-- Punto 8:
-- Lista los nombres de los fabricantes ordenados de forma ascendente.

SELECT nombre FROM fabricante
ORDER by nombre ASC;

-- Punto 9:
-- Lista los nombres de los productos ordenados en primer lugar por el nombre de forma ascendente y en segundo lugar por el precio de forma descendente.

SELECT nombre,precio FROM producto
ORDER by nombre ASC, precio DESC;


-- Punto 10:
-- Devuelve una lista con las 5 primeras filas de la tabla fabricante.

SELECT * FROM fabricante WHERE codigo_fabricante < 6;



-- Punto 11:
-- Lista el nombre de todos los productos del fabricante cuyo código de fabricante es igual a 2.

SELECT nombre FROM producto WHERE codigo_fabricante = 2;

-- Punto 12:
-- Lista el nombre de los productos que tienen un precio menor o igual a 120USD. 

SELECT nombre, precio FROM producto WHERE precio >= 120; 


-- Punto 13:
-- Devuelve todos los productos del fabricante Lenovo. (Sin utilizar INNER JOIN).

SELECT * FROM producto WHERE codigo_fabricante = 2;


-- Punto 14:
-- Devuelve todos los datos de los productos que tienen el mismo precio que el producto más caro del fabricante Lenovo. (Sin utilizar INNER JOIN).

SELECT * 
FROM producto 
WHERE precio = (
  SELECT MAX(precio)
  FROM producto 
  WHERE codigo_fabricante = (
    SELECT codigo_fabricante
    FROM fabricante
    WHERE nombre = 'Lenovo'
  )
);


-- Punto 15:
-- Lista el nombre del producto más caro del fabricante Lenovo. 

SELECT * FROM producto WHERE precio = (
  SELECT MAX(precio) FROM producto
  WHERE codigo_fabricante = (
    SELECT codigo_fabricante FROM fabricante 
    WHERE nombre = 'Lenovo' 
  )
);


-- Punto 16:
-- Devuelve los nombres de los fabricantes que tienen productos asociados. (Utilizando ALL o ANY).

SELECT * FROM fabricante WHERE codigo_fabricante = 5;

SELECT nombre FROM fabricante 
WHERE codigo_fabricante = ANY (
  SELECT codigo_fabricante
  FROM producto
);