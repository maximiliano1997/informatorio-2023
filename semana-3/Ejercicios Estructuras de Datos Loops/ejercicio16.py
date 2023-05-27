# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con cada palabra al revés.


def programa():
    usuario = input('Ingresa una cadena de texto: ').split(" ")
    nuevaCadenaDeTexto = []

    for palabra in usuario:

        palabraAlReves = palabra[::-1]
        nuevaCadenaDeTexto.append(palabraAlReves)

    resultado = " ".join(nuevaCadenaDeTexto)
    print(resultado)

    # usuario.reverse()
    # print(usuario)


programa()


"""
¡Gracias por la aclaración! Para invertir el orden de las letras en cada palabra de una cadena de texto sin cambiar el orden de las palabras, podemos seguir los siguientes pasos:

1- Pedir al usuario que ingrese una cadena de texto utilizando la función input().
2- Separar las palabras de la cadena de texto utilizando el método split(). Esto nos dará una lista de palabras.
3- Crear una nueva lista vacía para almacenar las palabras invertidas.
4- Utilizar un bucle for para recorrer cada palabra de la lista de palabras.
5- Utilizar la sintaxis de rebanado ([:: -1]) para invertir el orden de las letras de cada palabra.
6- Agregar cada palabra invertida a la lista de palabras invertidas.
7- Unir las palabras invertidas de nuevo en una sola cadena de texto utilizando el método join().
8- Mostrar la cadena de texto con las palabras invertidas utilizando la función print().

Es importante recordar que hay varias formas de abordar este problema, y lo que se describe aquí es solo una posible solución. Al escribir el código, es posible que tengamos que manejar casos especiales, como palabras que contienen caracteres especiales o espacios en blanco al inicio o al final de la cadena.
"""
