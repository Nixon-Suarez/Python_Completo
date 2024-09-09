# Consiste en crear una calse a partir de una o mas clases existentes
# las clases reciben formas que se denominan clases hijo y clases padres 
#Para asignar un padre a una clase se tendra que definir la clase hijo y poner entre parentesis la clase padre.
# class ClasePadre:
# class ClaseHijo(ClasePadre):

class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return f"Mi nombre es {self.nombre} y soy de tipo {self.tipo}"

class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return f"{self.nombre} es un Pikachu\ntipo de ataque: {tipo_ataque}"

class Charmander(Pokemon):
    def ataque(self, tipo_ataque):
        return f"{self.nombre} es un Charmander\ntipo de ataque: {tipo_ataque}"


Pokemon_1 = Pikachu("Pikachu", "Electrico")
print(Pokemon_1.descripcion())
print(Pokemon_1.ataque("impactrueno"))

Pokemon_2 = Charmander("Criss", "Fuego")
print(Pokemon_2.descripcion())
print(Pokemon_2.ataque("Lanzallamas"))
