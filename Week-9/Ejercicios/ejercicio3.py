# Ejercicio 3: Barajas
"""
Vamos a crear una baraja de cartas españolas orientado a objetos.
Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo
(espadas, bastos, oros y copas)
La baraja estará compuesta por un conjunto de cartas, 40 exactamente.
Las operaciones que podrá realizar la baraja son:
-barajar: cambia de posición todas las cartas aleatoriamente
-siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no
haya más o se haya llegado al final, se indica al usuario que no hay más
cartas.
-cartasDisponibles: indica el número de cartas que aún puede repartir
-darCartas: dado un número de cartas que nos pidan, le devolveremos ese
número de cartas (piensa que puedes devolver). En caso de que haya menos
cartas que las pedidas, no devolveremos nada pero debemos indicárselo al
usuario.
-cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido
ninguna indicárselo al usuario
-mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una
carta y luego se llama al método, este no mostrara esa primera carta
"""
import random


class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return f'Carta: {self.numero} de {self.palo}'


class Baraja():
    def __init__(self):
        self.barajaDeCartas = []
        self.indiceCartaActual = 0

    def agregarCartas(self, carta):
        self.barajaDeCartas.append(carta)

    def barajar(self):
        random.shuffle(self.barajaDeCartas)
        self.indiceCartaActual = 0
        return '\n Cartas Barajadas Exitosamente! \n   '

    def siguienteCarta(self):
        if self.indiceCartaActual < len(self.barajaDeCartas):
            carta = self.barajaDeCartas[self.indiceCartaActual]
            self.indiceCartaActual += 1
            return carta
        else:
            print('Perdon,No hay mas cartas en la Baraja!')
            return None

    def cartasDisponibles(self):
        resultado = len(self.barajaDeCartas) - self.indiceCartaActual
        return f'Las cantidad de Cartas diponibles son: {resultado}'

    def darCartas(self, cantidad):
        print(f'\n Cartas recibidas con darCartas({cantidad})')
        if self.indiceCartaActual + cantidad <= len(self.barajaDeCartas):
            cartasEntregadas = self.barajaDeCartas[self.indiceCartaActual:self.indiceCartaActual+cantidad]
            self.indiceCartaActual += cantidad
            return cartasEntregadas
        else:
            print('No hay  suficientes cartas disponibles.')
            return []

    def cartasMonton(self):
        print(f'---------------CartasMonton--------------------')
        if self.indiceCartaActual > 0:
            cartasMonton = self.barajaDeCartas[:self.indiceCartaActual]
            for carta in cartasMonton:
                print(carta)
        else:
            print('Aun no se han repatido ninguna carta.')

    def mostrarBaraja(self):
        mostrarBaraja = self.barajaDeCartas[self.indiceCartaActual:]
        contador = 1
        for carta in self.barajaDeCartas:
            print(f'{carta} + N°{contador}')
            contador += 1


# a = Carta()
b = Baraja()

numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['Espadas', 'Bastos', 'Oros', 'Copas']

listaDeCartas = [
]


# agregamos las carlas a la listaDeCartas:
contador = 0
while 0 < 40:
    print(contador)
    random.shuffle(numeros)
    random.shuffle(palos)
    listaDeCartas.append(Carta(numeros[0], palos[0]))
    contador += 1
    if contador == 40:
        break

# agregamos las cartas a la baraja:
for carta in listaDeCartas:
    b.agregarCartas(carta)

# Metodo barajar
print(b.barajar())

# Metodo siguienteCarta para devolver una carta
print(b.siguienteCarta())
print(b.siguienteCarta())
print(b.siguienteCarta())

# Metodo para ver la cantidad de cartas aun disponibles...
print(b.cartasDisponibles())


cartasRecibidas = b.darCartas(3)
for carta in cartasRecibidas:
    print(carta)


# Mostrar las cartas que ya han salido
print(b.cartasMonton())

#
print(b.mostrarBaraja())
