# Crea una función llamada calcular_factorial que tome un número entero como parámetro y devuelva el factorial de ese número. El factorial de un número entero positivo n se define como el producto de todos los números enteros positivos desde 1 hasta n.


usuario = int(input('Ingresar numero entero: '))


def calcular_factorial(numero):
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    print(f'El factoroial de {numero} es {resultado}')


calcular_factorial(usuario)
