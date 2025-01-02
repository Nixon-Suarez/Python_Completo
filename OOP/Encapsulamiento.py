# el encapsulamiento es basicamente que un atributo o un metodo sea privado osea que solo pueda acceder por medio de la clase

class MiClase:
    def __init__(self):
        #    ⬇️el encapsulamiento se refleja con (__) antes del nombre del atributo o metodo
        self.__atributo_privado = 1
    
    def __metodoprivado(self):
        print("soy un metodo privado")

objeto = MiClase()
# print(objeto.__atributo_privado) esta dara un error ya que no se puede acceder al atributo

# para acceder a un atributo encapsulado por medio de los setters y getters
