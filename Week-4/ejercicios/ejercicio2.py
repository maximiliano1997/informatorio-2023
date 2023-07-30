# Crea una función llamada saludo que tome el nombre de una persona como parámetro e imprima un saludo personalizado.

nombreUsuario = input('Ingresa tu nombre: ')


def saludo(nombre):
    print(f'Bienvenido {nombre}, hoy es un buen dia para usted.')


saludo(nombreUsuario)
