

num_filas = int(input('Ingrese cantidad de filas: '))


for f in range(num_filas):
    for c in range(f+1):
        print("*", end=" ")

    print()
