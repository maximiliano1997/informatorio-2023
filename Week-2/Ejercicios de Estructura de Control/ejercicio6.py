# 6-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es múltiplo de 2 y de 3 a la vez.



usuario = int(input('Ingresa un numero entero:  '))

if usuario % 2 == 0 & usuario % 3 == 0:
    print(f'El numero {usuario} es multiplo de 2 y 3')
else:
    print(f'El numero {usuario} no es multiplo de 2 y 3')


# Primero, se utiliza la función input() para pedir al usuario que ingrese un número entero, y se guarda la entrada como un entero en la variable usuario mediante la función int().

# Luego, se utiliza una estructura de control if -else para verificar si el número ingresado por el usuario es divisible por 2 y 3 al mismo tiempo. Para hacer esto, se utiliza el operador de módulo % para determinar si el número es divisible por 2 y 3 (si el resto de la división por ambos es 0, entonces el número es múltiplo de 2 y 3 al mismo tiempo). Si el número es divisible por 2 y 3 al mismo tiempo, el programa imprime el mensaje "El número {usuario} es múltiplo de 2 y 3". De lo contrario, el programa imprime el mensaje "El número {usuario} no es múltiplo de 2 y 3".

# Es importante tener en cuenta que al utilizar los operadores lógicos & para combinar las condiciones, se deben usar paréntesis para agrupar las operaciones de módulo, de lo contrario, el resultado puede ser inesperado. Entonces, la condición correcta sería(usuario % 2 == 0) and (usuario % 3 == 0).
