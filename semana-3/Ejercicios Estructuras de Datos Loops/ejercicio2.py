# 2- Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.


def programa():
    usuario = int(input('Ingresa un numero: '))
    lista = []

    for i in range(1, usuario+1):
        lista.append(i)

    print(f'La suma de los numeros del 1 al {usuario} es: {sum(lista)}')
    print(lista)


programa()
