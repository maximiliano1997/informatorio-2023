# ANALIZADOR DE TEXTOS


# PROGRAMA

def programa():

    print('\nBienvenido Usuario, como te llamas?')
    usuario = input('\nIngresa tu nombre: ')

    print(
        f'\nPor favor {usuario}, ingresa un texto cualquiera, por ejemplo, un artículo o una frase...')

    textoRequest = input('\nIngresa texto aqui: ').lower()

    print(
        f'\nGracias {usuario}, ahora te pedimos que ingreses 3 letras a eleccion tuya, separadas con espacio por favor...')

    letrasRequest = input('\nIngresa las 3 letras aqui: ').lower().split(" ")

    print(
        f'\nMuchisimas gracias {usuario}, estamos procesando la informacion...\n')

# 1- Cantidad de veces que aparece cada una de letras que eligió.
    print('________(1)________')
    if letrasRequest[0] in textoRequest:
        print(
            f'La letra {letrasRequest[0].upper()} aparece {textoRequest.count(letrasRequest[0])} veces en el texto ingresado\n')
    else:
        print(f'La letra {letrasRequest[0].upper()} no esta en el texto\n')

    if letrasRequest[1] in textoRequest:
        print(
            f'La letra {letrasRequest[1].upper()} aparece {textoRequest.count(letrasRequest[1])} veces en el texto ingresado\n')
    else:
        print(f'La letra {letrasRequest[1].upper()} no esta en el texto\n')

    if letrasRequest[2] in textoRequest:
        print(
            f'La letra {letrasRequest[2].upper()} aparece {textoRequest.count(letrasRequest[2])} veces en el texto ingresado\n')
    else:
        print(f'La letra {letrasRequest[2].upper()} no esta en el texto\n')

# 2- Cuantas palabras hay en total en todo el texto
    print('_________(2)_________')
    print(
        f'En el texto ingresado existen {len(textoRequest.split(" "))} palabras en total\n')

# 3- Cual es la primera letra y cuál es la última. (Indexación).
    print('_________(3)_________')
    print(
        f'La primera letra del texto es: {textoRequest[0]} y la ultima es: {textoRequest[-1]}\n')

# 4- Mostrar el texto en orden inverso.
    print('_________(4)________')
    reverse = textoRequest[::-1]
    print(f'{reverse}\n')

# 5- Decir si la palabra "python" aparece en el texto.
    print('_________(5)________')
    respuestas = {
        True: 'La palabra "Python" esta en el texto\n',
        False: 'No aparece la palabra "Python"\n'
    }
    if "python" in textoRequest:
        print(respuestas[True])
    else:
        print(respuestas[False])

    return (f'''
 __________( FIN )_________
Gracias por participar {usuario}
    ''')


print(programa())
513059
