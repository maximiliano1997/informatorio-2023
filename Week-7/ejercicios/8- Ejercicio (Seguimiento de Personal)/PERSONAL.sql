-- Ejercicio 8: Seguimiento de Personal

CREATE DATABASE Personal;
USE Personal;

-- Para trabajar con este caso debes descargar los scripts de SQL:
-- Paso 1: Creata Tablas en la base de datos Personal:

-- Creación de la tabla Departamento 
CREATE TABLE  Departamento ( 
	codDepto varchar (4)  PRIMARY KEY, 
	nombreDpto   varchar (20) NOT NULL, 
	ciudad      varchar (15), 
	codDirector  varchar (12) );

-- Creación de la tabla Empleado 
CREATE TABLE  Empleado ( 
	nDIEmp VARCHAR( 12 ) NOT NULL PRIMARY KEY, 
	nomEmp VARCHAR( 30 ) NOT NULL , 
	sexEmp CHAR( 1 ) NOT NULL CHECK (sexEmp  IN ('F', 'M') ), 
	fecNac DATE NOT NULL , 
	fecIncorporacion DATE NOT NULL, 
	salEmp FLOAT NOT NULL, 
	comisionE FLOAT NOT NULL, 
	cargoE VARCHAR( 15 ) NOT NULL, 
	jefeID VARCHAR( 12 ), 
	codDepto VARCHAR( 4 ) NOT NULL
    );

-- Cada frase desde -- hasta el final de la línea es ignorado (es un comentario) 
-- SQL es insensible a los espacios en blanco 
-- SQL NO es sensible a las mayúsculas (ejemplo:...Empleado... es equivalente a  -- ...EMPLEADO...)

-- PASO 2: Insertar datos en las tablas.

INSERT INTO Departamento (codDepto, nombreDpto, ciudad, coddirector) VALUES
('1000', 'GERENCIA', 'CALI', '31.840.269'),  
('1500', 'PRODUCCIÓN', 'CALI', '16.211.383'), 
('2000', 'VENTAS', 'CALI', '31.178.144'), 
('3000', 'INVESTIGACIÓN', 'CALI', '16.759.060'),  
('3500', 'MERCADEO', 'CALI', '22.222.222'), 
('2100', 'VENTAS', 'POPAYAN', '31.751.219'), 
('2200', 'VENTAS', 'BUGA', '768.782'), 
('2300', 'VENTAS', 'CARTAGO', '737.689'), 
('4000', 'MANTENIMIENTO', 'CALI', '333.333.333'), 
('4100', 'MANTENIMIENTO', 'POPAYAN', '888.888'), 
('4200', 'MANTENIMIENTO', 'BUGA', '11.111.111'), 
('4300', 'MANTENIMIENTO', 'CARTAGO', '444.444');

INSERT INTO Empleado (nDIEmp, nomEmp, sexEmp, fecNac, fecIncorporacion, salEmp, comisionE, cargoE, jefeID, codDepto) VALUES 
('31.840.269', 'María Rojas', 'F', '1959-01-15', '1997-05-16', 6250000, 1500000, 'Gerente', NULL, '1000'), 
('16.211.383', 'Luis Pérez', 'M', '1956-02-25', '2000-01-01', 5050000, 0, 'Director', '31.840.269', '1500'), 
('31.178.144', 'Rosa Angulo', 'F',  '1957-03-15', '1998-08-16', 3250000, 3500000, 'Jefe Ventas', '31.840.269', '2000'), 
('16.759.060', 'Darío Casas', 'M', '1960-04-05', '1992-11-01', 4500000, 500000, 'Investigador', '31.840.269', '3000'), 
('22.222.222', 'Carla López', 'F', '1975-05-11', '2005-07-16',  4500000, 500000, 'Jefe Mercadeo', '31.840.269', '3500'), 
('22.222.333', 'Carlos Rozo', 'M', '1975-05-11', '2001-09-16',  750000, 500000, 'Vigilante', '31.840.269', '3500') , 
('1.751.219', 'Melissa Roa', 'F', '1960-06-19', '2001-03-16', 2250000, 2500000, 'Vendedor', '31.178.144', '2100'), 
('768.782', 'Joaquín Rosas', 'M', '1947-07-07', '1990-05-16', 2250000, 2500000, 'Vendedor', '31.178.144', '2200'), 
('737.689', 'Mario Llano', 'M', '1945-08-30', '1990-05-16', 2250000, 2500000, 'Vendedor', '31.178.144', '2300'),
('333.333.333', 'Elisa Rojas', 'F', '1979-09-28', '2004-06-01', 3000000, 1000000, 'Jefe Mecánicos', '31.840.269', '4000'), 
('888.888', 'Iván Duarte', 'M', '1955-08-12',  '1998-05-16',  1050000, 200000, 'Mecánico', '333.333.333', '4100'), 
('11.111.111', 'Irene Díaz', 'F', '1979-09-28', '2004-06-01', 1050000, 200000, 'Mecánico', '333.333.333', '4200'), 
('444.444', 'Abel Gómez', 'M', '1939-12-24', '2000-10-01', 1050000, 200000, 'Mecánico', '333.333.333', '4300'), 
('1.130.222', 'José Giraldo', 'M', '1985-01-20', '2000-11-01', 1200000, 400000, 'Asesor', '22.222.222', '3500'), 
('19.709.802', 'William Daza', 'M', '1982-10-09', '1999-12-16', 2250000, 1000000,'Investigador', '16.759.060', '3000'), 
('31.174.099', 'Diana Solarte', 'F', '1957-11-19', '1990-05-16', 1250000, 500000, 'Secretaria', '31.840.269', '1000'), 
('1.130.777', 'Marcos Cortez', 'M', '1986-06-23', '2000-04-16',  2550000, 500000, 'Mecánico', '333.333.333', '4000'), 
('1.130.782', 'Antonio Gil', 'M', '1980-01-23', '2010-04-16', 850000, 1500000, 'Técnico', '16.211.383', '1500'), 
('333.333.334', 'Marisol Pulido', 'F', '1979-10-01', '1990-05-16', 3250000, 1000000, 'Investigador', '16.759.060', '3000'), 
('333.333.335', 'Ana Moreno', 'F', '1992-01-05', '2004-06-01', 1200000, 400000, 'Secretaria', '16.759.060', '3000'), 
('1.130.333', 'Pedro Blanco', 'M', '1987-10-28', '2000-10-01', 800000, 3000000, 'Vendedor', '31.178.144', '2000'), 
('1.130.444', 'Jesús Alfonso', 'M', '1988-03-14', '2000-10-01', 800000, 3500000, 'Vendedor', '31.178.144', '2000'), 
('333.333.336', 'Carolina Ríos', 'F', '1992-02-15', '2000-10-01', 1250000, 500000, 'Secretaria', '16.211.383', '1500'), ('333.333.337', 'Edith Muñoz', 'F', '1992-03-31', '2000-10-01', 800000, 3600000, 'Vendedor', '31.178.144', '2100'), 
('1.130.555', 'Julián Mora', 'M', '1989-07-03', '2000-10-01', 800000, 3100000, 'Vendedor', '31.178.144', '2200'), 
('1.130.666', 'Manuel Millán', 'M', '1990-12-08', '2004-06-01', 800000, 3700000, 'Vendedor', '31.178.144', '2300');

-- Resolver las siguientes consultas SQL:

-- Punto 1: Obtener los datos completos del Personal.

Select * from empleado;

-- Punto 2: Obtener los datos completos de los departamentos

Select * from departamento;

-- Punto 3: Obtener los datos de personal con cargo 'Secretaria'.

Select * from empleado where cargoE = 'Secretaria';

-- Punto 4: Obtener el nombre y salario de los/las empleados/as.

Select nomEmp, salEmp from empleado;

-- Punto 5: Obtener los datos de vendedores, ordenado por nombre.

Select * from empleado where cargoE = 'Vendedor'
order by nomEmp;

-- Punto 6: Listar el nombre de los departamento. 

Select nombreDpto from departamento;

-- Punto 7: Listar el nombre de los departamentos, ordenado por nombre

Select nombreDpto from departamento
order by nombreDpto;

-- Punto 8: Listar el nombre de los departamentos, ordenado por ciudad.

Select nombreDpto from departamento
order by ciudad;


-- Punto 9: Listar el nombre de los departamentos, ordenado por ciudad, en orden inverso.

Select nombreDpto from departamento
order by ciudad DESC;

-- Punto 10: Obtener el nombre y cargo del personal, ordenado por salario

Select nomEmp, CargoE from empleado
order by salEmp;

-- Punto 11: Listar los salarios y comisiones del personal del departamento 2000. 

Select salEmp, comisionE, codDepto from empleado WHERE empleado.codDepto = (select codDepto from departamento where codDepto = 2000);



-- Punto 12: Listar los salarios y comisiones del personal del departamento 2000, ordenado por comisión

Select salEmp, comisionE from empleado where empleado.codDepto = (select codDepto from departamento where codDepto = 2000)
order by comisionE;

-- Punto 13: Listar todas las comisiones

Select comisionE from empleado;


-- Punto 14: Obtener el valor total a pagar que resulta de sumar al personal del departamento 3000 una bonificación de $500.000, en orden alfabético por nombre.

Select SUM(salEmp) AS total_pago from empleado where empleado.codDepto = (Select codDepto from departamento where codDepto = 3000)
order by nomEmp;

-- Punto 15: Listar los empleados cuya comisión es menor o igual que el 30% de su sueldo.

Select * from empleado where comisionE <= (salEmp * 0.30);

-- Punto 16:Elabore un listado donde para cada fila, figure ‘Nombre’ y ‘Cargo’ antes del valor respectivo para cada persona

Select CONCAT('Nombre: ', nomEmp) AS Nombre, CONCAT('Cargo: ', cargoE) AS Cargo from empleado;
-- Punto 17: Hallar el salario y la comisión de aquellas personas cuyo número de documento de identidad superior al '19.709.802' Genere un grupo de personas, incluyendo aquéllas cuyo nombre inicie por la letra J. Emita un listado con nombre y su cargo por orden alfabético.

Select nomEmp, cargoE, salEmp, comisionE, nDIEmp from empleado where nDIEmp > 19709802 AND nomEmp LIKE 'J%'
order by nomEmp ASC;



-- Punto 18: Listar el salario, la comisión, el salario total (salario + comisión), documento de identidad de la persona y nombre, de quienes tienen comisión superior a $1.000.000, ordenar el informe por el número del documento de identidad

Select salEmp, comisionE, (salEmp + comisionE) AS salario_total, nDIEmp, nomEmp from empleado 
where comisionE > 1000000
order by nDIEmp;

-- Punto 19: Hallar el nombre de empleados/as que tienen un salario superior a $1.000.000, y tienen como jefe/a a alguien con documento de identidad '31.840.269'

Select nomEmp from empleado where salEmp > 1000000 AND nomEmp = (select nomEmp from empleado where nDIEmp = '31.840.269');

Select * from departamento;

-- Punto 20: Obtener los nombres de los departamentos que no sean “Ventas” ni “Investigación” ni ‘MANTENIMIENTO’, ordenados por ciudad.

Select nombreDpto from departamento where nombreDpto != 'VENTAS' and nombreDpto != 'INVESTIGACION';