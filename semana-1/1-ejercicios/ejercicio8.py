# 8-Crea un programa que pida al usuario el radio de un círculo y muestre su diámetro, su circunferencia y su área. Supón que pi es aproximadamente 3.14159.
pi = 3.14159

radio = float(input('Ingresar Radio del Circulo:  '))
diametro = (radio * 2)
circunferencia = (radio * pi * 2)
area = (pi * radio * radio)

print(
    f'Dado que el radio del Circulo es: {radio}, entonces su diametro es: {diametro}, su circunferencia {circunferencia} y su area {area}')
