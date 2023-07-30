# Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()


fecha = (input(
    'Ingresa tu fecha de nacimiento con este Formato dia/mes/año : ')).split('/')
print(f'Tu edad es: {2023 - int(fecha[2])} años')
