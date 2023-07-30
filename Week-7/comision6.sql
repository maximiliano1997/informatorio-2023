CREATE DATABASE comision6;

USE comision6;

CREATE TABLE nombreTabla(
	id_tabla INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20),
	apellido VARCHAR(20),
    fecha_de_nacimiento DATE,
    KEY (id_tabla)
);


INSERT INTO nombreTabla(nombre, apellido, fecha_de_nacimiento)
VALUES ('Ramiro', 'Alves', '1997-09-13'),
	   ('Micaela', 'Calvente', '1997-09-23'),
       ('Cristian', 'Bufalini', '1994-12-16');


SELECT * FROM nombreTabla;

DELETE FROM nombreTabla WHERE id_tabla > 3;

