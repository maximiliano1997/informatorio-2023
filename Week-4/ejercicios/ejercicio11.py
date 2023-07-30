# Crea una función llamada contar_vocales que tome una cadena de texto como parámetro y devuelva el número de vocales que contiene.

usuario = input('Ingresa una cadena de texto: ')


def contar_vocales(texto):
    counter = 0
    for i in texto:
        if i in "aeiouAEIOU":
            counter += 1
    print(counter)


contar_vocales(usuario)
