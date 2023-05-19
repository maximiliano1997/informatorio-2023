# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no


usuario = int(input('Ingresa una Nota del 1 al 10:  '))
if usuario >= 5:
    print('Aprobado')
else:
    print('Desaprobado')


# Primero, utilizamos la función input() para pedir al usuario que ingrese una nota del 0 al 10, y guardamos la entrada como un entero en la variable usuario mediante la función int().

# Luego, utilizamos una estructura de control if -else para determinar si la nota ingresada por el usuario es mayor o igual a 5. Si la nota es mayor o igual a 5, se imprimirá el mensaje "Aprobado" utilizando la función print(). Si la nota es menor que 5, se imprimirá el mensaje "Desaprobado" utilizando también la función print().

# Es importante tener en cuenta que este programa asume que el usuario ingresará un valor numérico entero del 0 al 10. Si se espera que el usuario pueda ingresar cualquier valor, se deberá incluir una verificación adicional para asegurarse de que la entrada sea un valor numérico válido dentro del rango especificado.
