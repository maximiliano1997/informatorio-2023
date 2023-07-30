# Crea una función llamada imprimir_pares que tome un número entero como parámetro y imprima todos los números pares desde 1 hasta ese número.

usuario = int(input('Ingresa un numero entero: '))


def imprimir_pares(num):
    for i in range(2, num):
        if i % 2 == 0:
            print(i)


imprimir_pares(usuario)
