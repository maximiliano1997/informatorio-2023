# -Escribe un programa que pida al usuario un número y luego imprima la secuencia de Fibonacci correspondiente a ese número


def programa():
    usuario = int(input('Ingresa un numero: '))

    a, b = 0, 1

    for i in range(0, usuario):
        print(a)
        a, b = b, a+b


programa()
