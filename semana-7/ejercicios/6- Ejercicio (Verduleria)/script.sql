
 SELECT * FROM grupos;
 SELECT * FROM productos;
 SELECT * FROM vendedores;
 SELECT * FROM ventas;
 
 
 -- Ejecicio 8: Verduleria
 -- Ejecuta consultas SQL que permita dar respuestas a:
 
 
 
 -- Punto 1:
 -- Obtener la lista de las ventas, pero con el nombre de la persona que lo vende en lugar de su identificador.

SELECT NombreVendedor, Producto, Kilos FROM vendedores
INNER JOIN ventas ON  ventas.Vendedor = vendedores.IdVendedor;


 -- Punto 2:
 -- Obtener la lista de las ventas pero con el nombre del producto en lugar del código.

SELECT NomProducto, Vendedor, Kilos FROM productos
INNER JOIN ventas ON ventas.Producto = productos.IdProducto;

 -- Punto 3:
 -- Obtener la lista de las ventas pero con el nombre del producto y quién lo vendió.

SELECT DISTINCT ve.NombreVendedor, p.NomProducto, v.Kilos 
FROM ventas v
INNER JOIN productos p ON v.Producto = p.IdProducto
INNER JOIN vendedores ve ON ve.IdVendedor = v.Vendedor;

-- Punto 4
-- Obtener el nombre de quien más kilos vendió.

SELECT NombreVendedor, Kilos
FROM vendedores
INNER JOIN ventas ON vendedores.IdVendedor = ventas.Vendedor
ORDER BY Kilos DESC
LIMIT 1;

-- Punto 5
-- Cuántos Kilos de Tomates se han vendido.
SELECT SUM(Kilos) AS Kilos_totales 
FROM ventas
WHERE ventas.Producto = (SELECT IdProducto FROM productos WHERE NomProducto = 'Naranjas');



-- Punto 6
-- Obtener todos los datos de cada venta, que haya superado el promedio de kilos vendidos en total.

SELECT * FROM ventas
WHERE ventas.Kilos > (SELECT AVG(Kilos) FROM ventas);

-- Punto 7
-- Obtener cuál fue el producto más vendido del grupo de "Hortalizas".

SELECT NomProducto, SUM(Kilos) AS kilos_totales
FROM productos
INNER JOIN ventas ON productos.IdProducto = ventas.Producto
INNER JOIN grupos ON productos.IdGrupo = grupos.IdGrupo
WHERE grupos.NombreGrupo = 'Hortalizas'
GROUP BY productos.NomProducto
ORDER BY kilos_totales DESC
LIMIT 1;


-- Punto 8
-- Obtener los datos de la persona que menos kilos vendió, e informar el nombre del producto y del grupo al que corresponde esa venta.

SELECT NombreVendedor, NomProducto, NombreGrupo, MIN(Kilos) AS kilostotales
FROM ventas
INNER JOIN vendedores ON ventas.Vendedor = vendedores.IdVendedor
INNER JOIN productos ON ventas.Producto = productos.IdProducto
INNER JOIN grupos ON productos.IdGrupo = grupos.IdGrupo
GROUP BY NombreVendedor, NomProducto, NombreGrupo
ORDER BY MIN(Kilos) ASC
LIMIT 1;


-- Punto 9
-- Obtener los totales de ventas por producto.


 SELECT * FROM grupos;
 SELECT * FROM productos;
 SELECT * FROM vendedores;
 SELECT * FROM ventas;
 