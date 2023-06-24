class Mate():
    # construtor
    def __init__(self, cebadas, estado):
        self.cebadas = cebadas
        self.estado = estado
        self.max_cebadas = 20

    # metodos
    def cebar(self):
        if self.estado.lower() == 'lleno':
            raise Exception(
                'Cuidado esta lleno el mate, te re quemaste brother!')
        self.estado == 'lleno'

    def beber(self):
        if self.estado.lower() != 'lleno':
            raise Exception('El mate esta vacio brother!')
        else:
            if self.cebadas > 0:
                self.max_cebadas -= 1
            if self.max_cebadas == 0:
                print('el mate está lavado')
            self.estado == 'vacio'


# crear instancia de clase Mate con 6 cebadas y estadio 'vacio'
mate = Mate(5, 'lleno')


try:
    mate.cebar()  # intento cebar el mate
    print('Se cebo el mate correctamente')
except Exception as e:
    print(str(e))  # capturar y mostrar cualquier excepcion que se lance


try:
    mate.beber()
    print('Que rico mate me tome')
except Exception as e:
    print(str(e))
