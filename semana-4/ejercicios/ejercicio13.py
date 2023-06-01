# Crea una función llamada calcular_descuento que tome dos parámetros: precio y porcentaje_descuento. La función debe calcular y devolver el precio después de aplicar el descuento.


usuario = (float(input('Ingresa el Precio: ')),
           float(input('Ingresa la Tasa de Descuento: ')))


def calcular_descuento(args):
    descuento = args[0] * (args[1] / 100)
    resultado = args[0] - descuento
    print(
        f'El descuento de {args[1]}% sobre ${args[0]} da como resultado un precio de ${resultado}')


calcular_descuento(usuario)
