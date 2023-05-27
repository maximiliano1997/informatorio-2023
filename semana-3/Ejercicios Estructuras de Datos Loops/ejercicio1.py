# 1-Escribe un programa que pida al usuario una palabra y luego imprima cada
# letra de la palabra en una línea separada


def programa():

    usuario = list(input('Ingresa una palabra: '))

    contador = 0
    while len(usuario) > contador:
        print(usuario[contador])
        contador += 1


programa()
