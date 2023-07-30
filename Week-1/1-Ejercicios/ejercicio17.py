# 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso.
# Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir "mundo hola".
# Importante!!! Utiliza un solo print() 😈

palabras = input('Ingresa 2 palabras:  ').split(" ")

print(f'{palabras[1]} {palabras[0]}')
