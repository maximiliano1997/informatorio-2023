# Crea una función llamada promedio que tome una lista de números como parámetro y devuelva el promedio de esos números.


usuario = input(
    'Ingresa un una lista de numeros separados por coma "," : ').split(",")


def promedio(args):
    acumulador = 0
    cantidad = len(args)
    for i in args:
        acumulador += int(i)
    resultado = acumulador / cantidad
    print(resultado)


promedio(usuario)
