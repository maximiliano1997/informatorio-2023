
-- Punto 1
-- lista las asignaturas del tipo "optativa"

SELECT * FROM asignatura WHERE tipo = 'optativa';

-- Punto 2
-- Lista los nombres de Departamento de la Universidad.  
SELECT nombre FROM departamento;

-- Punto 3
-- Listar apellidos y nombre de las Personas, convirtiendo ambos elementos a mayusculas.   
SELECT UPPER(apellido1) AS apellido, UPPER(nombre) AS nombre FROM persona;



-- Punto 4
-- Listar apellidos y nombres de Profesores mayores a 40 años en la Universidad.  
SELECT UPPER(apellido1) AS apellido, UPPER(nombre) AS nombre FROM persona WHERE tipo = 'profesor';


