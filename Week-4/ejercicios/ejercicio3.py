# Crea una función llamada invertir_cadena que tome una cadena de texto como parámetro y devuelva la cadena invertida.

usuario = input('Ingrese un texto corto: ')


def invertir_cadena(texto):
    texto_invertido = texto[::-1]
    print(f'{texto_invertido}')


invertir_cadena(usuario)
