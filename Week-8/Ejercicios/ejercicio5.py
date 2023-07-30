# Gestion de Donaciones


# class Donaciones():


class Producto():
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self.listaProductos = []

    # def calcular(self, producto, entidad):
    #     if not isinstance(producto, Perecedero) and not isinstance(producto, NoPerecedero):
    #         print('Producto no valido')
    #     if isinstance(producto, Perecedero):
    #         self.listaProductos.append(producto)


class Perecedero(Producto):
    def __init__(self, nombre, cantidad, diasACaducar):
        super().__init__(nombre, cantidad)
        self.diasACaducar = diasACaducar

    def calcular(self, entidades):
        # hoy = datetime.now()
        entrega_inmediata = []
        entrega_semana = []
        almacenar = []

        for entidad in entidades:
            if self.diasACaducar < 10:
                entrega_inmediata.append(self.cantidad // len(entidades))
            elif self.diasACaducar <= 30:
                entrega_semana.append(self.cantidad // len(entidades))
            else:
                almacenar.append(self.cantidad // len(entidades))

        if not entrega_inmediata:
            entrega_inmediata = [0] * len(entidades)

        return entrega_inmediata, entrega_semana, almacenar


class NoPerecedero(Producto):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo

    def calcular(self, entidades):
        entrega = self.cantidad // len(entidades)
        almacenar = self.cantidad % len(entidades)
        return entrega * len(entidades), almacenar


while True:
    productos = [
        Perecedero('Manzanas', 980, 5),
        Perecedero('Leche', 500, 20),
        NoPerecedero('Arroz', 1500, 'Grano'),
        NoPerecedero('Aceite', 200, 'Vegetal')
    ]

    entidades = ['Entidad A', 'Entidad B', 'Entidad C']

    for producto in productos:
        if isinstance(producto, Perecedero):
            entrega_inmediata, entrega_semana, almacenar = producto.calcular(
                entidades)
            print(f'Producto perecedero: {producto.nombre}')
            print(f'Entrega inmediata: {entrega_inmediata}')
            print(f'Entrega en una semana: {entrega_semana}')
            print(f'Almacenar: {almacenar}')
        elif isinstance(producto, NoPerecedero):
            entrega, almacenar = producto.calcular(entidades)
            print(f'Productos No Perecederos: {producto.nombre}')
            print(f'Entrega: {entrega}')
            print(f'Almacenar: {almacenar}')
        print('-----------------------------------')

    break
