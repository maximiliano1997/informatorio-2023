# Crea una función llamada es_par que tome un número como parámetro y devuelva Es par si el numero cumple con dichas condiciones y en caso contrario devuelva Es impar o No es par.


usuario = int(input('Ingresa primer numero: '))


def es_par(num):
    if num % 2 == 0:
        print('Es par')
    else:
        print('No es par')


es_par(usuario)
