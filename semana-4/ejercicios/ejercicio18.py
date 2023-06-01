# Crea una función llamada calcular_mayor_diferencia que tome una lista de números como parámetro y devuelva la mayor diferencia entre el numero mas alto y el numero mas bajo en la lista.


usuario = input(
    'Ingresa una lista de numeros separados por espacio:  ').split(" ")


def calcular_mayor_diferencia(lista):
    print(f'La lista de numeros ingresada es {lista}')
    pasarAEnteros = [int(x) for x in lista]
    numeroMasAlto = max(pasarAEnteros)
    numeroMasBajo = min(pasarAEnteros)
    resultado = numeroMasAlto - numeroMasBajo
    print(
        f'La diferencia entre el numero mas alto {numeroMasAlto} y el mas bajo {numeroMasBajo} es = {resultado}')


calcular_mayor_diferencia(usuario)
