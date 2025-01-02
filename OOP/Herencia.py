
#* Herencia-----------------------
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print("Se hablar")
#                  ⬇️empleado hereda de Persona
# class Empleado(Persona):
#     def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
#         super().__init__(nombre, edad, nacionalidad) # super().__init__() = se usa para llamar atributos de la clase padre(Persona) y heredarla en esta clase hija(Empleado) 
#         self.salario = salario
#         self.trabajo = trabajo

#                   ⬇️estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad) # super().__init__() = se usa para llamar atributos de la clase padre(Persona) y heredarla en esta clase hija(Empleado) 
        self.notas = notas
        self.universidad = universidad

Persona1 = Persona("juan", 12, "Colombiana")
# Empleado1 = Empleado("roberto", 12, "Colombiana", "programador", 10000000)

# Empleado1.hablar()
# print(Empleado1.edad) # imprime el salario del empleado

Estudiante1 = Estudiante("juan", 21, "Peruana", 4.5, "Gran Colombiana")
print(Estudiante1.notas)

#*Herencia Multiple-------------------------
class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        return (f"Mi habilidad es {self.habilidad}")

#                         ⬇️Hereda de Persona y de Artista
class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad) # 👈asi se hereda de mas de una clase padre y se llaman los atributos qeu se quieran heredar 
        Artista.__init__(self, habilidad)#                    👈⬇️
        self.salario = salario
        self.empresa = empresa

    # def mostrar_habilidad(self):  # aqui se le da un nuevo valor a mostrar habilidad unicamente en esta clase 
    #     print("no tengo")

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}") # aqui se llama a el metodo mostrar_habilidad de la clase padre de EmpleadoArtista(Artista) la cual no tiene ningun cambio y es llamada por medio de super()
                                       #!   ☝️siempre usar super para llamar metodos de clases padres no self por que si se reescribe puede genarar un error 

EmpleadoArtista1 = EmpleadoArtista("juan", 21, "Colombiana", "cantar", "1000", "Sony")

EmpleadoArtista1.presentarse()


herencia = issubclass(EmpleadoArtista, Artista) # de esta manera se mira si una clase hereda de otra
                    # ☝️esta hereda de esta☝️?

print(herencia)

instancia = isinstance(Persona1, Persona) # de esta manera se mira si un objeto es una isntacia de una clase osea es un objeto de la clase x
              #este objeto☝️       ☝️
              #es instacia de esta clase 
print(instancia)

