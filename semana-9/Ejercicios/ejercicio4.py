class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esTitularValido(self):
        return 18 < self.edad < 25


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


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def mostrar(self):
        resultado = f'Tipo de cuenta: Cuenta Joven! \n'
        resultado += f'Titular de la Cuenta: {self.titular.nombre}\n'
        resultado += f'Cantidad Disponible: ${self.cantidad} \n'
        resultado += f'Bonificacion: {self.bonificacion}% \n'
        resultado += f'----------------------------------------'
        return resultado

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
            print(f' ${cantidad} fueron ingresados a la Cuenta Joven')
            print(f'Ahora la Cuenta Joven tiene: ${self.cantidad}')
            return f'-----------------------------------------------'

    def retirar(self, cantidad):
        if self.titular.esTitularValido():
            super().retirar(cantidad)
        else:
            print(f'No se puede retirar dinero. TITULAR NO VALIDO.')


# EJEMPLOS DE USO


# Crear una instancia de Persona con la edad del titular
edad_titular = 20
titular = Persona('Imanol', edad_titular)


# Crear una instancia de CuentaJoven con el titular y otros detalles
cuenta_joven = CuentaJoven(titular, 120000, 5)


# Mostrar la informacion de la cuenta
print(cuenta_joven.mostrar())


# Retirar dinero
retirar = float(input('Ingrese el monto a retirar:  '))
print(cuenta_joven.retirar(retirar))
print(cuenta_joven.mostrar())


# ingresar dinero
ingresar = float(input('Ingrese el monto a cargar en su cuenta: '))
print(cuenta_joven.ingresar(ingresar))
print(cuenta_joven.mostrar())
