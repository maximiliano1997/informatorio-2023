# Crea un programa en python que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
# Supongamos que pi = 3.1416

pi = 3.1416
radio = float(input('Inserta radio de un circulo: '))
area = pi * (radio*2)

print(f'El Area del circulo es: {area}')
