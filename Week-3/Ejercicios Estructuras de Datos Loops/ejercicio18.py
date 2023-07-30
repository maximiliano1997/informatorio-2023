

def programa():
    usuario = int(input('Ingresa un numero: '))
    keeper = 1

    for i in range(1, usuario-5):
        for c in range(i):
            print(keeper, end=" ")
            keeper += 1

        print()


programa()
