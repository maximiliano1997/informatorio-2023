class Cafetera():
    def __init__(self):
        self._capacidadMaxima = 10
        self._cantidadActual = 2

    def inspeccionarCafetera(self):
        print(f'Capacidad Maxima de Cafetera: {self._capacidadMaxima}lts')
        print(f'Cantidad Disponible en Cafetera: {self._cantidadActual}lts')
        return f'-----------------------------------------------------------'

    def llenarCafetera(self):
        self._cantidadActual = 10
        if self._cantidadActual == self._capacidadMaxima:
            print(f'La cafetera se ha llenado! 10 Litros completados')
        return '------------------------------------------------------'

    def servirTaza(self, capacidadTaza=1):

        if self._cantidadActual < capacidadTaza:
            print(
                f'Se cargo en la taza lo que quedaba en la Cafetera...{self._cantidadActual}lts')
            print(
                f'A la taza le quedaron {capacidadTaza - self._cantidadActual}ltrs por llenar')
            # self._cantidadActual - self._cantidadActual
            return f'Cafetera ahora tiene: {self._cantidadActual - self._cantidadActual}ltrs'
        else:
            print(
                f'Taza cargada, La cafetera ahora le quedan: {self._cantidadActual - capacidadTaza}ltrs')

    def vaciarCafetera(self):
        self._cantidadActual = 0
        return 'Cafetera Vacia!'

    def agregarCafe(self, cantidadDeCafe):
        self._cantidadActual += cantidadDeCafe


a = Cafetera()

print(a.inspeccionarCafetera())
print(a.llenarCafetera())
print(a.agregarCafe(4))
print(a.servirTaza(15))
