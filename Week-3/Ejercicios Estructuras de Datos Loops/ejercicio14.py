# 4-Escribe un programa que pida al usuario un número y luego imprima un triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


def programa():
    usuario = int(input('Ingresa un numero: '))
    for f in range(usuario):
        for c in range(f):
            print(usuario, end=" ")

        usuario + 1
        print()


programa()
