

class Tiempo():
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo

    def __str__(self):
        # return 'Hora: {}, Minutos: {}, Segundos: {}'.format(self._hora, self._minuto, self._segundo)
        return f'Hora: {self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}'

    def cambiar_hora(self, hora=None, minuto=None, segundo=None):
        if hora is not None:
            self._hora = hora
        if minuto is not None:
            self._minuto = minuto
        if segundo is not None:
            self._segundo = segundo


class PruebaTiempo():
    def __init__(self):
        self.tiempo = Tiempo()

    def __str__(self):
        return str(self.tiempo)


prueba = PruebaTiempo()


# Modificiar la hora
while True:
    op = int(input('Elegir una opcion   \n1.Mostrar Hora  \n2.Salir \n'))

    if op == 1:
        hora = int(input('Ingresa la hora: '))
        minuto = int(input('Ingresa los minutos: '))
        segundo = int(input('Ingresa los segundos: '))

        prueba.tiempo.cambiar_hora(hora, minuto, segundo)
        print(prueba)
    if op == 2:
        print('Adios')
        break
