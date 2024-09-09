# setter = modificar, setear
# getter = obtener, visualizar 

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, new_nombre):
        self.__nombre = new_nombre
    
juan = Persona("Juan", 23)

nombre = juan.get_nombre()
print(nombre)

juan.set_nombre("Pepito")

nombre = juan.get_nombre()
print(nombre)

print(juan.edad)



