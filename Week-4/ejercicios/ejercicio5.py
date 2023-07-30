# Crea una función llamada es_divisible que tome dos números enteros como parámetros y devuelva Es divisible si el primer número es divisible por el segundo número, o No es divisible en caso contrario

usuario = (int(input('Ingresa primer numero: ')),
           int(input('Ingresa segundo numer: ')))


def es_divisible(nums):
    if nums[0] % nums[1] == 0:
        print(f'{nums[0]} es divisible por {nums[1]}')


es_divisible(usuario)
