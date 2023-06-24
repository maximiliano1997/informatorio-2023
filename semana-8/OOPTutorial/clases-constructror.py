# clase + constructor

class Persona:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return '{} tiene {} años'.format(self.nombre, self.año)

    def comentario(self, frase):
        return '{} dice: {}'.format(self.nombre, frase)


persona1 = Persona('Imanol', 26)

# print(persona1.comentario('whatsup dag?'))


# modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False

    def enviar_correo(self):
        self.enviado = True


# mi_correo = Email()
# print(mi_correo.enviado)
# mi_correo.enviar_correo()
# print(mi_correo.enviado)
