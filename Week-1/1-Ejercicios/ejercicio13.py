# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.


nombre = input('Ingresa tu nombre aqui: ')
edad = int(input('Ahora ingresa tu edad aqui: '))
print(f'{nombre} dentro de 10 años vas a cumplir {(edad + 10)}')
