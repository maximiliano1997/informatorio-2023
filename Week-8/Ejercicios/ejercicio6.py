

class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return f'Titular de la Cuenta: {self.titular}\nCantidad disponible: ${self.cantidad}'

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f'  ${cantidad} Fueron ingresados correctamente!')
            print(f'Ahora tienes en tu cuenta: ${self.cantidad}\n')

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
            print(f'Fueron retirados -${cantidad}')
            print(f'Ahora te quedan: ${self.cantidad}\n')


c = Cuenta('imanol', 3500.25)

c.ingresar(50000)
# print(c.mostrar())
# c.retirar(50000)
# print(c.mostrar())
