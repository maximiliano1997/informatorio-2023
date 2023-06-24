# Herencia ejemplo practico


class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresarDato(self):
        self.datos = [int(input('Ingresar Dato '+str(i+1) + ' = '))
                      for i in range(self.n)]


class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b = self.datos
        s = a + b
        print(f'El resultado es {s}')

    def resta(self):
        a, b = self.datos
        r = a - b
        print(f'El resultado es: {r}')


class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a = self.datos
        print(f'El resultado es: {(math.sqrt(a))}')


ejemplo = Calculadora(5)

print(ejemplo.ingresarDato())
print(ejemplo.datos)
# print(ejemplo.resta())
