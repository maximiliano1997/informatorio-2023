# Crea una función llamada eliminar_duplicados que tome una lista como parámetro y devuelva una nueva lista sin duplicados, conservando el orden original


usuario = input('Ingresa lista de numeros separados por espacio: ').split(" ")


def eliminar_duplicados(data):
    nuevaLista = []

    for i in data:
        if i not in nuevaLista:
            nuevaLista.append(i)
    print(f'La lista nueva sin duplicados = {nuevaLista}')


eliminar_duplicados(usuario)
