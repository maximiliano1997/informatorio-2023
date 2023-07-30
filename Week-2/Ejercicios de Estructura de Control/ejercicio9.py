# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos






usuario = (
    int(input('Ingrese primer numero:')),
    int(input('Ingrese segundo numero:')),
    int(input('Ingrese tercer numero:')),
           )

if (usuario[0] > usuario[2] and usuario[0] > usuario[1]):
    print(
        f'El Primer Numero es Mayor a los otros dos: ')
elif (usuario[1] > usuario[2] and usuario[1] > usuario[0]):
    print(
        f'El Segundo Numero es Mayor a los otros dos: ')
else:
    print(f'El Tercer Numero es Mayor a los otros dos:')


# Primero, el programa utiliza la función input() para solicitar al usuario que ingrese tres números. Luego, se utilizan los paréntesis para agrupar los tres números en una tupla y asignarlos a la variable usuario.

# Luego, el programa utiliza una serie de comparaciones para determinar cuál de los tres números es el mayor. Si el primer número ingresado(usuario[0]) es mayor que los otros dos(usuario[1] y usuario[2]), entonces se imprime un mensaje indicando que el primer número es el mayor. Si el segundo número(usuario[1]) es mayor que los otros dos(usuario[0] y usuario[2]), entonces se imprime un mensaje indicando que el segundo número es el mayor. De lo contrario, se imprime un mensaje indicando que el tercer número(usuario[2]) es el mayor.

# Este programa asume que el usuario ingresa números enteros. Si el usuario ingresa algo que no sea un número entero, el programa puede producir un error.
