# Crea una función llamada es_palindromo que tome una cadena de texto como parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso contrario.


usuario = input('Ingresa un texto: ')


def es_palindromo(texto):
    if texto == texto[::-1]:
        print('Es Palindromo')
    else:
        print('No es Palindromo')


es_palindromo(usuario)
