# 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# *Recuerda el print() del ejercicio anterior


ciudadano = input('Ingresa tu nombre, edad y ciudad de residencia (separados por comas):  ').split(",")
print(f'Nombre: {ciudadano[0]}, Edad: {ciudadano[1]}, Ciudad de Residencia: {ciudadano[2]}')
