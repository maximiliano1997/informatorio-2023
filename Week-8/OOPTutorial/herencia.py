# Herencia


class Persona:
    def __init__(self, nombre, edad, genero, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}. ¡Mucho Gusto!')

    def obtener_informacion(self):
        print('Informacion Personal: ')
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')
        print(f'Genero: {self.genero}')
        print(f'Direccion: {self.direccion}')
        print(f'Telefono: {self.telefono}')


# imanolsito = Persona('Imanol', 26, 'Macho', 'Almirante Brown 3665', 3624701650)
# imanolsito.saludar()
# imanolsito.obtener_informacion()


class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, direccion, telefono, escuela):
        super().__init__(nombre, edad, genero, direccion, telefono)
        self.escuela = escuela

    def obtener_informacion(self):
        super().obtener_informacion()
        print(f'Escuela: {self.escuela}')

    def estudiar(self):
        print(f'{self.nombre} esta estudiando en {self.escuela}')


estudiante = Estudiante('Imanol Aguer', 26, 'Masculino',
                        'Almirante Brown 3665', '3624701650', 'Colegio Piacentini')
estudiante.saludar()
estudiante.obtener_informacion()
estudiante.estudiar()


# En este ejemplo, la clase Persona es la clase base y la clase Estudiante hereda de ella utilizando la instrucción class Estudiante(Persona). La clase Estudiante añade un atributo adicional escuela y un método adicional estudiar(). La función super() se utiliza en el método __init__ de la clase Estudiante para llamar al constructor de la clase base y asegurar que los atributos de la clase base se inicialicen correctamente. Luego, se pueden llamar a los métodos de ambas clases para obtener información o realizar acciones específicas para cada una.
