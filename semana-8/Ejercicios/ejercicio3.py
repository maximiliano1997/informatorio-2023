

class Triangulo:
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0
        self.ladoC = 0

    def __str__(self):
        return f'Lado A: {self.ladoA}, Lado B: {self.ladoB}, Lado C: {self.ladoC}'

    def ingresarAtributos(self):
        self.ladoA = int(input('Ingresar Lado A: '))
        self.ladoB = int(input('Ingresar Lado B: '))
        self.ladoC = int(input('Ingresar Lado C: '))

    def ladoMayor(self):
        listaDeLados = [self.ladoA, self.ladoB, self.ladoC]
        print()

        for numero in listaDeLados:
            ladoMayor = 0
            if numero > ladoMayor:
                ladoMayor = numero
            print(f'El lado Mayor es el lado {ladoMayor}')
            return '---------------------------------------'

    def tipoDeTriangulo(self):
        if (self.ladoA == self.ladoB and self.ladoB == self.ladoC) and (self.ladoC == self.ladoA):
            print('Es un triangulo Equilatero')
            return ('-------------------------')

        elif (self.ladoA == self.ladoB or self.ladoA == self.ladoC) or (self.ladoC == self.ladoB):
            print('Es un triangulo Isosceles')
            return ('-------------------------')

        elif (self.ladoA != self.ladoB and self.ladoB != self.ladoC) and (self.ladoA != self.ladoC):
            print('Es un triangulo Escaleno')
            return ('-------------------------')


a = Triangulo()

print(a.ingresarAtributos())
print(a.ladoMayor())
print(a.tipoDeTriangulo())
print(a)
