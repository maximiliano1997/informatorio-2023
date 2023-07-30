# 19-Escribe un programa que solicite al usuario un número decimal y luego imprima la parte entera y decimal por separado


numero = input('Ingresa un Numero decimal:  ').split(".")
print(f'Entero = {numero[0]} y Decimal = {numero[1]}')
