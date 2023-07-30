# Crea una función llamada es_capicua que tome un número como parámetro y devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda) y False en caso contrario.

usuario = input('Ingresa numero: ')


def es_capicua(numero):
    numeroNormal = int(numero)
    numeroReverse = int(numero[::-1])
    if numeroReverse == numeroNormal:
        print(f'Es capicua!!')
    else:
        print('No es Capicua')


es_capicua(usuario)
