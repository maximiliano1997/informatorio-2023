# -Crea una función llamada encontrar_maximo que tome una lista de números como parámetro y devuelva el número máximo de la lista.


usuario = input('Ingresa lista de numeros separados por espacio: ').split(" ")


def encontrar_maximo(data):
    listaNumeros = [int(x) for x in data]
    print(f'EL numero mas alto de la lista {data} es {max(listaNumeros)}')


encontrar_maximo(usuario)
