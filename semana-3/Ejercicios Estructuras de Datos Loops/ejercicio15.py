# 15- Escribe un programa que pida al usuario una cadena de texto y determine cuántas veces aparece cada letra en la cadena


def programa():
    usuario = input('Ingresa una oracion corta: \n').replace(" ", "")
    # textoUnido = "".join(usuario)
    diccionario = {}

    for letra in usuario:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1

    for letra, cantidad in diccionario.items():
        print(f'\nLa letra {letra} aparece {cantidad} de veces en el texto')

    print(f'\n{diccionario}')


programa()


"""  EXPLICACION 
Claro, te puedo explicar la idea general detrás de este programa sin darte directamente la respuesta.

En general, para resolver este problema, necesitamos recorrer la cadena de texto que ingresa el usuario letra por letra y llevar un registro de cuántas veces aparece cada letra. Podemos hacer esto utilizando un diccionario, donde las claves son las letras y los valores son el número de veces que aparecen.

Un enfoque posible para este programa podría ser el siguiente:

1- Pedir al usuario que ingrese una cadena de texto.
2- Inicializar un diccionario vacío para llevar un registro del número de veces que aparece cada letra.
3- Recorrer la cadena de texto letra por letra utilizando un bucle.
4- Para cada letra, comprobar si ya está en el diccionario. Si no está, añadir la letra como clave con un valor de 1. Si ya está, incrementar el valor correspondiente en 1.
5- Una vez que hayamos recorrido toda la cadena de texto, imprimir los resultados.

Es importante tener en cuenta que este es solo uno de los muchos enfoques posibles para resolver este problema y que puede haber diferentes formas de implementar cada uno de los pasos anteriores. Sin embargo, espero que esta explicación general te ayude a entender cómo puedes abordar este problema.




También puedes utilizar el método replace() para eliminar los espacios en blanco de una cadena de texto. El método replace() reemplaza todas las ocurrencias de una cadena por otra cadena. Si pasamos un espacio en blanco (" ") como el primer argumento y una cadena vacía ("") como el segundo argumento, reemplazaremos todos los espacios en blanco por una cadena vacía.
"""
