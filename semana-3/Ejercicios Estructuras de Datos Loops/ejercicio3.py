# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10


def programa():
    usuario = int(input('Ingresa un numero: '))
    lista = []
    tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in tabla:
        lista.append(usuario * i)

    print(
        f'La tabla de multiplicar de {usuario} de los numeros del 1 al 10')
    print(lista)


programa()
