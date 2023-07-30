# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.

print('Ingrese 2 numeros: ')
usuario = (int(input('Ingrese el primer numero: ')),
           int(input('Ingrese el segundo numero: ')))

if usuario[0] > usuario[1]:
    print(f'{usuario[0]} es mayor a {usuario[1]}')
elif usuario[0] == usuario[1]:
    print('Esos 2 numeros son iguales camarada')
else:
    print(f'{usuario[1]} es mayor a {usuario[0]}')


# Primero, utilizamos la función print() para imprimir un mensaje pidiendo al usuario que ingrese dos números.

# Luego, utilizamos la función input() para pedir al usuario que ingrese dos números, y guardamos cada número como un entero en la tupla usuario mediante la función int(). La tupla usuario contiene los dos números ingresados por el usuario.

# Después, utilizamos una estructura de control if -elif para determinar cuál de los dos números es mayor. Si el primer número ingresado por el usuario (usuario[0]) es mayor que el segundo (usuario[1]), se imprimirá el mensaje "x es mayor a y", donde x es el valor del primer número y y es el valor del segundo número, utilizando la función print(). Si ambos números son iguales, se imprimirá el mensaje "Esos 2 numeros son iguales camarada" utilizando también la función print(). Y si el segundo número ingresado por el usuario (usuario[1]) es mayor que el primero (usuario[0]), se imprimirá el mensaje "y es mayor a x", donde Y es el valor del segundo número y X es el valor del primer número, utilizando también la función print().

# Es importante tener en cuenta que este programa asume que el usuario ingresará dos valores numéricos enteros. Si se espera que el usuario pueda ingresar cualquier valor, se deberá incluir float() para asegurarse de que las entradas sean valores numéricos válidos.


# Investigar que es una Tupla en Google: "Que es una Tupla en Python"