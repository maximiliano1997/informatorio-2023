# 9-Escribe un programa que solicite al usuario dos números y luego imprima la suma, la resta, la multiplicación y la división de los dos números.

num1 = input(int)
num2 = input(int)


print(f'Dado los 2 numeros ingresados')
suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = int(num1 * num2)
division = int(num1 / num2)

print(f'La Suma entre {num1} y {num2} es = {suma}')
print(f'La Resta entre {num1} y {num2} es = {resta}')
print(f'La Multiplicacion entre {num1} y {num2} es = {multiplicacion}')
print(f'La Division entre {num1} y {num2} es = {division}')
