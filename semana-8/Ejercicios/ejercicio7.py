# Bebidas online


class Almacen():
    def __init__(self):
        self.listaBebidas = []

    def agregarBebidas(self, bebida):
        if not isinstance(bebida, AguaMineral) and not isinstance(bebida, Gaseosa):
            print('Tipo de dato no permitido')
        for b in self.listaBebidas:
            if b.id == bebida.id:
                print('Id Bebida ya existente')
        self.listaBebidas.append(bebida)

    def eliminarBebidas(self, id):
        for x in self.listaBebidas:
            if x.id == id:
                self.listaBebidas.remove(x)
                return
        print('No se Encontro el producto que desea eliminar')

    def precioTotal(self):
        resultado = sum(self.listaBebidas)
        return resultado

    def verInfo(self):
        for x in self.listaBebidas:
            x.verInfo()


class Bebidas():
    def __init__(self, id, litros, precio, marca):
        self.id = id
        self.litros = litros
        self.precio = precio
        self.marca = marca

    def get_precio(self):
        return self.precio

    def verInfo(self):
        print(f'id: %s' % (self.id))
        print(f'Litros: %s' % (self.litros))
        print(f'Precio: $%s' % (self.precio))
        print(f'Marca: %s' % (self.marca))


class AguaMineral(Bebidas):
    def __init__(self, id, litros, precio, marca, origen):
        super().__init__(id, litros, precio, marca)
        self.origen = origen

    def verInfo(self):
        super().verInfo()
        print(f'Origen: %s' % (self.origen))


class Geaseosa(Bebidas):
    def __init__(self, id, litros, precio, marca, azucar, promocion):
        super().__init__(id, litros, precio, marca)
        self.azucar = azucar
        self.promocion = promocion

    def verInfo(self):
        super().verInfo()
        print(f'% Azucar: %s' % (self.azucar))
        print(f'% Promocion: %s' % (self.promocion))


a = Almacen()

x = AguaMineral(1, 3, 355, 'Secco', 'Manantiales')
a.agregarBebidas(x)

a.verInfo()
