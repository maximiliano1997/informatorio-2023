# 5-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es par o impar




usuario = int(input('Ingresa un numero entero:  '))
if usuario % 2 == 0:
    print(f'El Numero {usuario} es Par')
else:
    print(f'El Numero {usuario} es Impar')


#     Primero, se utiliza la función input() para pedir al usuario que ingrese un número entero, y se guarda la entrada como un entero en la variable usuario mediante la función int().

# Luego, se utiliza una estructura de control if -else para verificar si el número ingresado por el usuario es par o impar. Para hacer esto, se utiliza el operador de módulo % para determinar si el número es divisible por 2 (si el resto de la división es 0, entonces el número es par). Si el número es divisible por 2, el programa imprime el mensaje "El Numero {usuario} es Par" utilizando la función print(). De lo contrario, el programa imprime el mensaje "El Numero {usuario} es Impar".

# Es importante tener en cuenta que este programa asume que el usuario ingresará un valor numérico entero. Si se espera que el usuario pueda ingresar cualquier valor, se deberá incluir una verificación adicional para asegurarse de que la entrada sea un valor numérico válido.
