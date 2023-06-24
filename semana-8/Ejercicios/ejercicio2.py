# SUPER CLASE

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color {}, {} ruedas'.format(self.color, self.ruedas)


# SUB CLASE
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velociodad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velociodad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg".format(self.carga)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ', {} km/h, {} cc'.format(self.velocidad, self.cilindrada)

# FUNCION CATALOGAR 1


# def catalogar(lista_vehiculos):
#     for vehiculo in lista_vehiculos:
#         print('Clase: {}'.format(vehiculo.__class__.__name__))
#         print('Atrivutlos: {}'.format(vehiculo))


# FUNCION CATALOGAR 2
def catalogar(lista_vehiculos, ruedas=4):
    if ruedas != 0:
        vehiculos_filtro = [
            vehiculo for vehiculo in lista_vehiculos if vehiculo.ruedas == ruedas]
        print('Se han encontrado {} vehiculos con {} ruedas:'.format(
            len(vehiculos_filtro), ruedas))
        for vehiculo in vehiculos_filtro:
            print('Clase: {}'.format(vehiculo.__class__.__name__))
            print('Atributos: {}'.format(vehiculo.__str__()))
    else:
        for vehiculo in lista_vehiculos:
            print("Clase: {}".format(vehiculo.__class__.__name__))
            print("Atributos: {}".format(vehiculo))


# Crear una lisrta de vehiculos
vehiculos = [
    Vehiculo('Rojo', None),
    Coche('Azul', 4, 150, 1500),
    Camioneta('Negro', 4, 180, 2000, 500),
    Bicicleta('Amarillo', 2, 'Urbana'),
    Motocicleta('Verde', 2, 'dax', 100, 1000),
]

# LLamar a la funcion

catalogar(vehiculos)
