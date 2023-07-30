# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.



usuario = input("Ingrese una letra cualquiera: ")
if usuario.lower() in "aeiou":
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada es una consonante.")


# Primero, utilizamos la función input() para pedir al usuario que ingrese una letra, y guardamos la entrada en la variable letra.

# Luego, utilizamos una estructura de control if -else para verificar si la letra es una vocal o una consonante. Para hacer esto, utilizamos el método lower() de la cadena de texto letra, que convierte la letra ingresada a minúsculas. De esta manera, podemos comparar la letra ingresada en minúsculas con una cadena de texto que contiene las vocales "aeiou".

# Si la letra ingresada es una vocal, es decir, si se encuentra en la cadena de texto "aeiou", se imprime el mensaje "La letra ingresada es una vocal." De lo contrario, si la letra no se encuentra en la cadena de texto de vocales, se imprime el mensaje "La letra ingresada es una consonante."

# Es importante mencionar que este programa no verifica si el usuario ha ingresado una letra válida. En otras palabras, si el usuario ingresa un número o un símbolo en lugar de una letra, el programa dará un error. Para hacerlo más robusto, se podría añadir una validación previa para asegurarse de que la entrada del usuario sea una letra.
