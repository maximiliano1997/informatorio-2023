# Desafío 2:
# Escribe un programa que solicite al usuario su información personal, incluyendo
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:
# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono


def programa():
    print('Ingrese su informacion personal...')

    nombreApellido = input('Nombre y Apellido: ')
    edad = input('Edad: ')
    estatura = input('Estatura: ')
    peso = input('Peso: ')
    direccion = input('Direccion: ')
    telefono = input('Nro Telefono: ')

    return (f""" 
La informacion Ingresada es la siguiente:

Nombre Completo: {nombreApellido} 
Edad: {edad}
Estatura: {estatura}
Direccion: {direccion}
Numero de Telefono: {telefono}
    """)


print(programa())
