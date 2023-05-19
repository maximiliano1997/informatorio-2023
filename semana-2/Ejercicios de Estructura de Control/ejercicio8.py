# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a".


usuario = input('Ingrese una palabra cualquiera:  ').lower()
if 'a' in usuario:
    print(f'La palabra ingresada contiene la Letra "a" ')
else:
    print(f'La palabra ingresada no continene la letra "a')

    # El programa solicita al usuario que ingrese una cadena de caracteres a través de la función input(). Luego, se verifica si la letra 'a' (tanto en minúscula como en mayúscula) está presente en la cadena utilizando el operador in. Si la letra 'a' está presente en la cadena, se imprime el mensaje "La palabra ingresada contiene la letra 'a'", de lo contrario, se imprime "La palabra ingresada no contiene la letra 'a'"
