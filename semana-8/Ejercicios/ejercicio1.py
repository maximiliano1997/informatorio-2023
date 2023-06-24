class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color {}, {} ruedas'.format(self.color, self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velociodad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velociodad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche('Azul', 4, 300, 1000)
print(c.__str__())
