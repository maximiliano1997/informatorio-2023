# Crea una función llamada contar_palabras que tome una cadena de texto como parámetro y devuelva el número de palabras que contiene. Se considera que las palabras están separadas por espacios


usuario = input('Ingresa cadena de texto: ').split(" ")


def contar_palabras(data):
    resultado = len(data)
    print(
        f'La cantidad de palabras en el texto otorgado es de {resultado} palabras en total')


contar_palabras(usuario)
