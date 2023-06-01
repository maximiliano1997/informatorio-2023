# Crea una función llamada es_bisiesto que tome un año como parámetro y devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400

usuario = int(input('Ingresa una año: '))


def es_bisiesto(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return "Bisiesto"
    elif year % 4 == 0 and not year % 100 == 0:
        print("Bisiesto")
    else:
        print("No es bisiesto")


es_bisiesto(usuario)
