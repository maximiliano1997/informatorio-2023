# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e imprima su índice de masa corporal(IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).


peso = float(input('Ingresa cual es tu Peso:  '))
altura = float(input('Ingresa tu altura:  '))
indiceMasaCorporal = peso / (altura * altura)
print(
    f'Dado tu peso de {peso} y altura de {altura}, tu indice de masa corporal (IMC) es = {indiceMasaCorporal}')
