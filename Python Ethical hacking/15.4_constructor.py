#utilizamos el constructor para inicializar un objeto
# En el constructor ingresamos los valores iniciales del objeto
# definimos el constructor con el metodo __init__


class Persona:
    def __init__(self, nombre, apellido, año):
        self.nombre = nombre
        self.apelledo = apellido
        self.año = año

    def descripcion(self):
        print( '{}:{}'.format(self.nombre, self.año))

    def comenatario(self, frase):
        print('{} dice {}'.format(self.nombre, frase))
    
ingeniero = Persona('Pedro','Vargas', 2021)
ingeniero.descripcion()
print(ingeniero.comenatario("Good Morning"))

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

correo = Email()
print(correo.enviado)
correo.enviar_correo() 
print(correo.enviado)