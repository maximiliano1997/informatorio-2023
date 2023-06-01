# -Crea una función llamada es_anagrama que tome dos cadenas de texto como parámetros y devuelva True si son anagramas (es decir, si tienen las mismas letras pero en distinto orden), o False en caso contrario

usuario = (input('Ingresa Cadena de texto N°1: '),
           input('Ingresa cadena de texto N°2: '))


def es_anagrama(cadenas):
    if len(cadenas[0]) == len(cadenas[1]):
        lista1 = list(cadenas[0])
        lista2 = list(cadenas[1])
        lista1.sort()
        lista2.sort()
        if "".join(lista1) == "".join(lista2):
            print(True)
        else:
            print(False)
    else:
        print(False)


es_anagrama(usuario)
