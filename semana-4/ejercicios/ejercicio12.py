# Crea una función llamada convertir_temperatura que tome una temperatura en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión es: Fahrenheit = (Celsius * 9/5) + 32


usuario = int(input('Ingresa Temperatura en ° Celsius: '))


def convertir_temperatura(temp):
    resultado = (temp * 9 / 5) + 32
    print(
        f' La temperadura de {temp}° Celsius es igual a  {resultado}° Farenheit')


convertir_temperatura(usuario)
