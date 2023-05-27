# 12-Escribe un programa que pida al usuario una lista de números separados por comas y calcule su promedio


def programa():
    usuario = input(
        'Ingresa una lista de numeros separados por coma "," ').split(",")

    lista = [int(num) for num in usuario]

    # for i in usuario:
    resultado = sum(lista) / len(lista)
    print(resultado)


programa()
