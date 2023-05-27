# 5--Escribe un programa que imprima la suma de todos los números pares del 1 al 100.


def programa():
    usuario = 100
    resultado = 0

    for i in range(2, usuario+1):
        if (i % 2 == 0):
            resultado += i

    print(f'{resultado}')
    print(resultado)


programa()
