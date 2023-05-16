# 15-Escribe un programa que solicite al usuario una temperatura en grados Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.


celsius = float(input('Ingrese Temperatura en Grados Celsius:  '))
fahrenheit = (celsius * 1.8) + 32
print(
    f'Si la temperatura en grados Celsius es {celsius}, en Fahrenheit son = {fahrenheit}'
)
