# Escribe un programa que pida al usuario una palabra y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

def program():
    usuario = input('Ingresa una palabra: ')

    if usuario == usuario[::-1]:
        print('Es un palindromo')
    else:
        print('No es un palindromo')


program()
