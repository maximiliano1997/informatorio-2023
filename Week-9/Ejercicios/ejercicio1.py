# # Ejercico 1: Pizzeria
# """ Una pizzería de la ciudad ofrece a sus clientes una amplia variedad de pizzas de
# fabricación propia, de varios tamaños (8, 10 y 12 porciones).
# Los clientes tienen a disposición un menú que describe para cada una de las
# variedades, el nombre, los ingredientes y el precio según el tamaño y el tipo (a la
# piedra, a la parrilla, de molde) de la pizza. Los clientes realizan sus pedidos en el
# mostrador. El pedido debe contener el nombre del Cliente, para llamarlo cuando
# su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, la fecha del
# pedido, la hora en la que el pedido debe entregarse y la demora estimada
# informada al cliente. El pedido va a la cocina y cuando está preparado se informa
# al que lo tomó para que se genere la factura correspondiente y se le entregue el
# pedido al cliente.
# El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la
# siguiente información:
# -Variedades y tipos de pizzas más pedidas por los clientes.
# -Ingresos (recaudaciones) por períodos de tiempo.
# -Pedidos (cantidad y monto) por períodos de tiempo.
# """


# class Pizza:
#     def __init__(self, nombre, ingredientes, precio):
#         self.nombre = nombre
#         self.ingredientes = ingredientes
#         self.precio = precio


# class Pedido:
#     def __init__(self, cliente, pizzas, tamaño, variedad, tipo, fechaDelPedido, horaAEntregarPedido, demoraEstimada):
#         self.cliente = cliente
#         self.pizzas = pizzas
#         self.tamaño = tamaño
#         self.variedad = variedad
#         self.tipo = tipo
#         self.fechaDelPedido = fechaDelPedido
#         self.horaAEntregarPedido = horaAEntregarPedido
#         self.demoraEstimada = demoraEstimada

#     def generarFactura(self):
#         precioTotal = sum(pizza.precio for pizza in self.pizzas)
#         factura = f'........Detalles del Pedido........\n'
#         factura += f'Cliente: {self.cliente} \n'
#         factura += f'Pizzas: {len(self.pizzas)} \n'
#         factura += f'Tamaño: {self.tamaño} porciones \n'
#         factura += f'variedad: {self.variedad} \n'
#         factura += f'Fecha: {self.fechaDelPedido} \n'
#         factura += f'Hora de Entrega: {self.horaAEntregarPedido} \n'
#         factura += f'Demora Estimada: {self.demoraEstimada} minutos \n'
#         factura += f'Total a pagar: ${precioTotal} \n'
#         factura += f'--------------------------------------------- \n'
#         return factura


# class Pizzeria:
#     def __init__(self):
#         self.menu = {}
#         self.pedidos = []

#     def agregarPizza(self, pizza):
#         self.menu[pizza.nombre] = pizza

#     def mostrarMenu(self):
#         print('Menu de la Pizzeria Rocola: ')
#         for variedad in self.menu:
#             pizza = self.menu[variedad]
#             print(f'- Pizza {variedad} ({pizza.tipo})')

#     def realizarPedido(self, cliente, cantidad, tamaño, variedad, tipo, fecha, horaEntrega, demoraEstimada):
#         if variedad in self.menu:
#             pizzas = [self.menu[variedad] for x in range(cantidad)]
#             pedido = Pedido(cliente, pizzas, tamaño, variedad, tipo, fecha, horaEntrega, demoraEstimada)
#             factura = pedido.generarFactura()
#             print('Pedido realizado!')
#             print(factura)
#             self.pedidos.append(self.menu[variedad])
#             print(self.pedidos)


# # Crear instancias de pizzas
# pizzaNapolitana = Pizza('Napolitana', ['Tomate', 'Mozzarella'], 25.99)
# pizzaPepperoni = Pizza('Pepperoni', ['Queso', 'Pepperoni'], 15.99)
# pizzaCaprese = Pizza('Caprese', ['Tomate', 'Pimienta'], 10.99)
# pizzaVegetariana = Pizza('Vegetariana', ['Berenjera', 'Cebolla'], 5.99)
# pizzaImanol = Pizza('Imanol', ['Leche', 'Tequila'], 1.99)

# pizzeria = Pizzeria()

# # Agregar pizzas al menu de la pizzeria
# pizzeria.agregarPizza(pizzaNapolitana)
# pizzeria.agregarPizza(pizzaPepperoni)
# pizzeria.agregarPizza(pizzaCaprese)
# pizzeria.agregarPizza(pizzaVegetariana)
# pizzeria.agregarPizza(pizzaImanol)

# # Mostrar menu al cliente para que elija:
# print(pizzeria.mostrarMenu())

# # Elegir cual pizza le gusta mas
# # def seleccionUsuario():
# #     Pizza seleccionada


# # # Realizar un pedido
# pizzeria.realizarPedido('Imanol', 5, 10, 'Napolitana', 'al molde',
#                         '19/06/2023', '23:30', 30)


class Pizza:
    def __init__(self, nombre, ingredientes, precio, tipo):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.tipo = tipo


class Pedido:
    def __init__(self, cliente, pizzas, tamaño, variedad, fechaDelPedido, horaAEntregarPedido, demoraEstimada):
        self.cliente = cliente
        self.pizzas = pizzas
        self.tamaño = tamaño
        self.variedad = variedad
        self.fechaDelPedido = fechaDelPedido
        self.horaAEntregarPedido = horaAEntregarPedido
        self.demoraEstimada = demoraEstimada

    def generarFactura(self):
        precioTotal = sum(pizza.precio for pizza in self.pizzas)
        factura = '........Detalles del Pedido........\n'
        factura += f'Cliente: {self.cliente} \n'
        factura += f'Pizzas: {len(self.pizzas)} \n'
        factura += f'Tamaño: {self.tamaño} porciones \n'
        factura += f'Variedad: {self.variedad} \n'
        factura += f'Fecha: {self.fechaDelPedido} \n'
        factura += f'Hora de Entrega: {self.horaAEntregarPedido} \n'
        factura += f'Demora Estimada: {self.demoraEstimada} minutos \n'
        factura += f'Total a pagar: ${precioTotal} \n'
        factura += '--------------------------------------------- \n'
        return factura


class Pizzeria:
    def __init__(self):
        self.menu = {}
        self.pedidos = []
        self.pizzas_mas_pedidas = {}
        self.ingresos = {}

    def agregarPizza(self, pizza):
        self.menu[pizza.nombre] = pizza

    def mostrarMenu(self):
        print('Menu de la Pizzeria Rocola:')
        for variedad in self.menu:
            pizza = self.menu[variedad]
            print(f'- Pizza {variedad} ({pizza.tipo})')

    def realizarPedido(self, cliente, cantidad, tamaño, variedad, fecha, horaEntrega, demoraEstimada):
        if variedad in self.menu:
            pizzas = [self.menu[variedad] for _ in range(cantidad)]
            pedido = Pedido(cliente, pizzas, tamaño, variedad, fecha, horaEntrega, demoraEstimada)
            factura = pedido.generarFactura()
            print('Pedido realizado!')
            print(factura)
            self.pedidos.append(pedido)

            # Actualizar contador de pizzas más pedidas
            if variedad in self.pizzas_mas_pedidas:
                self.pizzas_mas_pedidas[variedad] += cantidad
            else:
                self.pizzas_mas_pedidas[variedad] = cantidad

            # Actualizar registro de ingresos
            if fecha in self.ingresos:
                self.ingresos[fecha] += sum(pizza.precio for pizza in pizzas)
            else:
                self.ingresos[fecha] = sum(pizza.precio for pizza in pizzas)

    def mostrarPizzasMasPedidas(self):
        print('Pizzas más pedidas por los clientes:')
        if self.pizzas_mas_pedidas:
            sorted_pizzas = sorted(
                self.pizzas_mas_pedidas.items(), key=lambda x: x[1], reverse=True)
            for pizza, cantidad in sorted_pizzas:
                print(
                    f'- Pizza {pizza} ({self.menu[pizza].tipo}): {cantidad} pedidos')
        else:
            print('No hay registros de pedidos.')

    def mostrarIngresosPorPeriodo(self, fechaInicio, fechaFin):
        print('Ingresos por período de tiempo:')
        total = 0
        for fecha, ingreso in self.ingresos.items():
            if fechaInicio <= fecha <= fechaFin:
                print(f'- Fecha: {fecha}, Ingresos: ${ingreso}')
                total += ingreso
        print(f'Total de ingresos en el período: ${total}')

    def contarPedidosPorPeriodo(self, fechaInicio, fechaFin):
        cantidad_pedidos = 1
        for pedido in self.pedidos:
            if fechaInicio <= pedido.fechaDelPedido <= fechaFin:
                cantidad_pedidos += 1
        return cantidad_pedidos

    def calcularMontoPedidosPorPeriodo(self, fechaInicio, fechaFin):
        monto_total = 0
        for pedido in self.pedidos:
            if fechaInicio <= pedido.fechaDelPedido <= fechaFin:
                monto_total += sum(pizza.precio for pizza in pedido.pizzas)
        return monto_total


# Crear una instancia de la pizzería
pizzeria = Pizzeria()

# Agregar pizzas al menú
pizzaNapolitana = Pizza(
    'Napolitana', ['Tomate', 'Mozzarella'], 25.99, 'a la piedra')
pizzaPepperoni = Pizza(
    'Pepperoni', ['Queso', 'Pepperoni'], 15.99, 'a la parrilla')
pizzaCaprese = Pizza('Caprese', ['Tomate', 'Pimienta'], 10.99, 'de molde')

pizzeria.agregarPizza(pizzaNapolitana)
pizzeria.agregarPizza(pizzaPepperoni)
pizzeria.agregarPizza(pizzaCaprese)

# Mostrar el menú al cliente
pizzeria.mostrarMenu()

# Realizar un pedido
pizzeria.realizarPedido('Imanol', 2, 8, 'Napolitana',
                        '19/06/2023', '23:30', 30)
pizzeria.realizarPedido('Lucía', 1, 12, 'Pepperoni',
                        '20/06/2023', '20:00', 45)
pizzeria.realizarPedido('Carlos', 3, 10, 'Caprese', '21/06/2023', '19:30', 35)
pizzeria.realizarPedido('Imanol', 2, 8, 'Pepperoni', '22/06/2023', '21:00', 40)
pizzeria.realizarPedido('Lucía', 1, 12, 'Napolitana',
                        '23/06/2023', '22:30', 25)

# Mostrar las pizzas más pedidas
pizzeria.mostrarPizzasMasPedidas()

# Mostrar ingresos por período de tiempo
pizzeria.mostrarIngresosPorPeriodo('20/06/2023', '23/06/2023')

# Contar pedidos y monto de pedidos por período de tiempo
cantidad_pedidos = pizzeria.contarPedidosPorPeriodo('20/06/2023', '23/06/2023')
monto_pedidos = pizzeria.calcularMontoPedidosPorPeriodo(
    '20/06/2023', '23/06/2023')

print(f'Cantidad de pedidos: {cantidad_pedidos}')
print(f'Monto total de los pedidos: ${monto_pedidos}')
