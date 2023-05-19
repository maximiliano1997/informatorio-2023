# 2-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es positivo, negativo o cero


usuario = int(input('Ingrese un numero entero:  '))

if usuario > 0:
    print('Positivo')
elif usuario == 0:
    print('Cero')
if usuario < 0:
    print('Negativo')


# Primero, utilizamos la función input() para pedir al usuario que ingrese un número entero, y guardamos la entrada como un entero en la variable usuario mediante la función int().

# Luego, utilizamos una estructura de control if -elif para determinar si el valor de usuario es positivo, negativo o cero. Si el valor de usuario es mayor que cero, se imprimirá el mensaje "Positivo" utilizando la función print(). Si el valor de usuario es igual a cero, se imprimirá el mensaje "Cero" utilizando también la función print(). Y si el valor de usuario es menor que cero, se imprimirá el mensaje "Negativo" utilizando también la función print().

# Es importante tener en cuenta que este programa asume que el usuario ingresará un valor numérico entero. Si se espera que el usuario pueda ingresar cualquier valor, se deberá incluir una verificación adicional para asegurarse de que la entrada sea un valor numérico válido.
