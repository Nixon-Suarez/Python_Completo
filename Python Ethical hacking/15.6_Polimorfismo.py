# Capacidad que tienen los objetos en diferentes clases de tener un 
# comportamiento y atributos del mismo nombre con diferentes valores 
# La clase padre define el comportamiento y las clases hijas realizan sobrecarga (la sobre carga es cuando un metodo o un atributo provienen de una clase padre y en su clase hijo este se cambia)
# de metodos cambiando el comportamiento del objeto 

# class Legendario:
#     def ataque(self):
#         print("Ataque legendario")

# class Moltres(Legendario):
#     tipo = "Fuego"
#     def ataque(self):
#         print("Giro de fuego")

# class Articuno(Legendario):
#     tipo = "Hielo"
#     def ataque(self):
#         print("Canto Helado")

# legendario = Legendario()
# legendario.ataque()

# moltres = Moltres()
# moltres.ataque()

# articuno = Articuno()
# articuno.ataque()
#--------------------------

# class Vivienda:
#     def __init__(self, precio, superficie):
#         self.precio = precio
#         self.superficie = superficie

#     def tipo(self):
#         pass

# class Casa(Vivienda):
#     def tipo(self):
#         print(f"Casa de 2 pisos de {self.superficie}m2 cuesta {self.precio}")

# class Departamento(Vivienda):
#     def tipo(self):
#         print(f"Duplex de {self.superficie}m2 custa {self.precio}")

# familia = Casa(40000, 200)
# familia.tipo()

# pareja = Departamento(12000, 100)
# pareja.tipo() 
# -------------------------------
class Ave:
    def volar(self):
        print("No todas las aves volamos")

class Pinguino(Ave):
    def volar(self):
        print("Nosotros no Volamos")
    def velocidad(self):
        print("10 km/h")

    def color(self):
        print("Blanco")

class Aguila(Ave):
    def volar(self):
        print("Nosotros si volamos")

    def velocidad(self):
        print("300 km/h")

    def color(self):
        print("Cafe")

def funcion(obj):
    obj.velocidad()
    obj.color()
    obj.volar()

aguila_1 = Aguila()
Pinguino_1 =  Pinguino()
gallina_1 = Ave()

funcion(gallina_1)
funcion(aguila_1)
funcion(Pinguino_1)