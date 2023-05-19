# 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
# mayor de edad (18 años o más) o no.


usuario = int(input('Ingresa tu edad: '))
if usuario >= 18:
    print('Eres Mayor de Edad (+18)')
else:
    print('No eres mayor de Edad, eres Menor (-18)')


# Primero, utilizamos la función input() para pedir al usuario que ingrese su edad, y guardamos la entrada como un entero en la variable usuario mediante la función int().

# Luego, utilizamos una estructura de control if -else para determinar si el usuario es mayor de edad o no. Si el valor de la variable usuario es mayor o igual a 18, lo que significa que el usuario tiene 18 años o más, se imprimirá el mensaje "Eres Mayor de Edad (+18)" utilizando la función print(). De lo contrario, si el valor de la variable usuario es menor a 18, lo que significa que el usuario es menor de edad, se imprimirá el mensaje "No eres mayor de Edad, eres Menor (-18)" utilizando también la función print().

# Es importante tener en cuenta que este programa asume que el usuario ingresará un valor numérico entero para su edad. Si se espera que el usuario pueda ingresar cualquier valor, se deberá incluir una verificación adicional para asegurarse de que la entrada sea un valor numérico válido.
