# ejercicio 8; Mis libros favoritos

class Libro():
    def __init__(self, titulo, autor, nroPaginas, calificacionDada):
        self.titulo = titulo
        self.autor = autor
        self.nroPaginas = nroPaginas
        self.calificacionDada = calificacionDada

    # Modificadores
    def modificarTitulo(self, nuevoTitulo):
        self.titulo = nuevoTitulo

    def modificarAutor(self, nuevoAutor):
        self.autor = nuevoAutor

    def modificarNroPaginas(self, nuevoNroPaginas):
        self.nroPaginas = nuevoNroPaginas

    def modificarTitulo(self, nuevaCalificacion):
        self.calificacionDada = nuevaCalificacion

    # Retornadores de Datos
    def verTitulo(self):
        return self.titulo

    def verAutor(self):
        return self.autor

    def verNroPaginas(self):
        return self.nroPaginas

    def verCalificacionDada(self):
        return self.calificacionDada

    # def verInfo(self):
        # if


class ConjuntoLibros():
    def __init__(self, capacidad):
        self.libros = []
        self.capacidad = capacidad
        self.contador = 1

    def agregarLibro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            print(f' {self.contador}° Libro agregado correctamente.')
            self.contador += 1
        else:
            print('No hay suficiente espacio para agregar el libro')

    def eliminarLibro(self, titulo):
        librosEliminados = []
        for libro in self.libros:
            if libro.verTitulo() == titulo:
                self.libros.remove(libro)
                librosEliminados.append(libro)
            if librosEliminados:
                print('Los siguientes libros fueron eliminados: ')
                for libro in librosEliminados:
                    print(libro.verTitulo())
            else:
                print('No se encontor ningun libro con ese titulo...')

    def verLista(self):
        if not self.libros:
            print('No hay libros en el conjunto.')
        else:
            print('Contenido del conjunto de libros (ordenado por calificacion): ')
            librosOrdenados = sorted(
                self.libros, key=lambda libro: libro.verCalificacionDada(), reverse=True)
            for libro in librosOrdenados:
                print(f'Titulo: {libro.verTitulo()}')
                print(f'Autor: {libro.verAutor()}')
                print(f'N° Paginas: {libro.verNroPaginas()}')
                print(f'Calificacion: {libro.verCalificacionDada()}')
                print(f'--------------------------------------------')


# a = Libro()
# b = ConjuntoLibros(5)

listaDeLibrosFavoritos = [
    Libro('El inversor inteligente', 'Benjamin Graham', 800, 10),
    Libro('1984', 'George Orwell', 332, 9),
    Libro('Cien años de soledad', 'Gabriel G Marquez', 432, 8),
    Libro('Margin of Safety', 'Set Khlarman', 832, 7),
    Libro('Mi vida', 'Imanol Aguer', 1432, 5),
]

conjuntoLibros = ConjuntoLibros(5)

for libro in listaDeLibrosFavoritos:
    conjuntoLibros.agregarLibro(libro)

conjuntoLibros.eliminarLibro('Mi vida')

print(conjuntoLibros.verLista())
