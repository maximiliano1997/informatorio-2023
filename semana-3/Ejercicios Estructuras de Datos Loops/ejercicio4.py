# 4-Escribe un programa que imprima los números pares del 1 al 100


def programa():
    usuario = 100

    for i in range(1, usuario):
        if (i % 2 == 0):
            print(i)


programa()
