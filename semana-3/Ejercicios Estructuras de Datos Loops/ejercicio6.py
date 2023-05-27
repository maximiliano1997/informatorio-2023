# Escribe un programa que pida al usuario una palabra y luego imprima la misma palabra pero con las letras en orden inverso.


def programa():
    usuario = input('Escribe una palabra:  ')

    resultado = usuario[::-1]

    print(resultado)


programa()
