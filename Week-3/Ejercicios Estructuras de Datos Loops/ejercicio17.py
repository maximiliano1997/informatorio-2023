# 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con las palabras en orden inverso.


def programa():
    usuario = input('Ingrese una cadena de texto: ').split(" ")

    usuarioAlReves = usuario[::-1]
    resultado = " ".join(usuarioAlReves)
    print(resultado)


programa()
