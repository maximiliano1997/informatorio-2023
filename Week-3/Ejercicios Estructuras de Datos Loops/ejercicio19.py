# 19-Escribe un programa que pida al usuario un número y luego imprima si ese número es un número perfecto o no. Un número perfecto es aquel que es igual a la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6


def programa():
    usuario = int(input('Ingrese un numero cualquiera: '))

    divisores = 0
    for i in range(1, usuario):
        if usuario % i == 0:
            divisores += 1

    if divisores == usuario:
        print(f'{usuario} es un numero perfecto.')
    else:
        print(f'{usuario} no es un numero perfecto.')


programa()