# Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene.


def programa():
    usuario = input('Ingresa un texto corto: ').split(" ")

    print(f'El texto contiene {len(usuario)} palabras en total.')


programa()
