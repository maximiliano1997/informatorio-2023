# Ejercicio 2: Supermercado


# Catalogo > productos > vender
# c/producto > nombre, precio, etc


# supermercado > nombre, direccion, etc
# saber cantidad total de productos y suma total de precios

class Supermercado:
    def __init__(self, nombreSuper, direccionSuper):
        self.nombreSuper = nombreSuper
        self.direccionSuper = direccionSuper


class Catalogo(Supermercado):
    def __init__(self, nombreSuper, direccionSuper):
        Supermercado.__init__(self, nombreSuper, direccionSuper)
        self.productos = []
        self.precioProductos = []

    def addToCatalogo(self, producto):
        # Aplicamos descuento del 10% Programa PRECIOS CUIDADOS antes de añadir al Catalogo
        if producto.preciosCuidados == 'Si':
            print(f'{producto.nombre} es parte del Programa de Precios Cuidados')
            descuentoPC = float(input(
                f'Ingrese el Numero de descuento del producto {producto.nombre}: '))
            producto.precio = producto.precio * descuentoPC
        self.productos.append(producto)
        self.precioProductos.append(producto.precio)

    # def productosProgramaPreciosCuidados(self):
    #     if producto.preciosCuidados == 'Si':
    #         return f'{producto}'

    def calCantidadProductos(self):
        return f' El Supermercado {self.nombreSuper} tiene {len(self.productos)} productos en el su Catalogo con un valor total de ${sum(self.precioProductos)}'


class Producto:
    def __init__(self, nombre, precio, preciosCuidados=None):
        self.nombre = nombre
        self.precio = precio
        self.preciosCuidados = preciosCuidados

    def verInfoProducto(self):
        producto = f'Nombre: {self.nombre} \n'
        producto += f'Precio: {self.precio} \n'
        producto += f'Precio Cuidados: {self.preciosCuidados} \n'
        producto += f'----------------------------------------------'
        print(producto)

########################################################################


# Catalogo
a = Catalogo('MaxiChinok', 'Almirante Brown 3665')
# p = Producto('lol', 444)


# Productos
listaDeProductos = [
    Producto('Pan', 450, 'Si'),
    Producto('Carne Vaca', 1450, 'Si'),
    Producto('Leche', 250, 'Si'),
    Producto('Agua Mineral', 600),
    Producto('Papa', 400, 'Si'),
]

contador = 0
for producto in listaDeProductos:
    contador += 1
    a.addToCatalogo(producto)
    print(f'Informacion del PRODUCTO N°{contador} \n')
    producto.verInfoProducto()

# p.verInfoProducto()
print(a.calCantidadProductos())
