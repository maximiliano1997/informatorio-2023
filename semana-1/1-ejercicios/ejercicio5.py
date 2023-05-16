# 5-Crea un programa que pida al usuario dos números enteros y muestre en pantalla su cociente y su resto.


print('Division de numeros...')
num1 = int(input('Ingresa primer numero: '))
num2 = int(input('Ingresa segundo numero: '))
cociente = int(num1 / num2)
resto = num1 % num2
print(f'El cociente es: {cociente} y el resto es {resto}')
