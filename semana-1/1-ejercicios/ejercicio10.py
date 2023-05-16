# -Crea un programa que pida al usuario una cantidad en dólares y la convierta a euros. Supón que el tipo de cambio es de 0.84 euros por dólar


print('Conversor de Dolares a Euros')
cantidadDolares = float(input('Ingresa el monto en Dolares:  '))
conversorEuros = float(cantidadDolares * 0.84)
print(f'{cantidadDolares} Dolares son {conversorEuros} Euros')
