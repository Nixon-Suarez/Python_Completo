# Mejor forma de encapsular 
# mejor sintaxis y flexibilidad  
# Las Propiedad son setters getters y deleters  

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    @property #@property = indica que lo de abajo es un getter (Ya no es una funcion es una propiedad)
    def nombre(self):
        return self.__nombre
    
    @nombre.setter #@(nombredelapropiedad).setter 
    def nombre(self, new_nombre): 
        #        ⬇️tomo __nombre no del atributo sino del getter(nombre)
        self.__nombre = new_nombre

    @nombre.deleter #@(nombredelapropiedad).deleter
    def nombre(self):
        del self.__nombre
    
juan = Persona("Juan", 23)
# aqui se ultiliza el getter

print(juan.nombre)

# y aqui es setter
juan.nombre = "Juanito alimaña"
print(juan.nombre)

# del juan.nombre # elimina el atributo nombre de juan -> se necesita el deleter para esto 

print(juan.nombre)

