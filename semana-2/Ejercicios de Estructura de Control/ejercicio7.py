# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial



usuario = input('Ingresa un Caracter cualquiera:  ')

if usuario.isupper():
    print('El caracter es Mayuscula')
elif usuario.islower():
    print('El Caracter es Minuscula')
elif usuario.isnumeric():
    print('El Caracter es un Numero')
else:
    print('Es un Caracter Especial')


#     Este programa solicita al usuario un carácter y evalúa si es una letra mayúscula, una letra minúscula, un número o un carácter especial utilizando los métodos isupper(), islower() e isnumeric() en una estructura condicional if -elif-else.

# Si el carácter es una letra mayúscula, el método isupper() devuelve True y se imprime el mensaje "El caracter es Mayuscula". Si es una letra minúscula, el método islower() devuelve True y se imprime el mensaje "El caracter es Minuscula". Si el carácter es un número, el método isnumeric() devuelve True y se imprime el mensaje "El caracter es un Numero". Si no es ninguna de las opciones anteriores, se imprime el mensaje "Es un Caracter Especial".
