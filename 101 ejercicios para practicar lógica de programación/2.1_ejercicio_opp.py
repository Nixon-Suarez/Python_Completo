import random

class Perro():
    def __init__(self, nombre):
        self.nombre = nombre
        self.count = 0 

    def Smell(self, persona):
        if persona.spy:
            if random.random() < 0.6:
                print(f"{self.nombre} bites {persona.nombre}")
                self.count += 1

            else:
                print(f"{self.nombre} saluted {persona.nombre}")


        elif persona.grumpy:
            if random.random() < 0.2:
                print(f"{self.nombre} licked {persona.nombre}")
            else:
                print(f"{self.nombre} saluted {persona.nombre}")
        else:
            print(f"{self.nombre} saluted {persona.nombre}")

class Persona():
    def __init__(self, nombre, isSpy = False, isGrumpy = False):
        self.nombre = nombre
        self.spy = isSpy
        self.grumpy = isGrumpy

class Park():
    def __init__(self, dog):
        self.dog = dog
        self.persona = []

    def agregarPersonas(self, personas):
        self.persona.append(personas)

    def perroHuele(self):
        for personas in self.persona:
            self.dog.Smell(personas)
        
        print(f"Numero final de espías detectados es: {self.dog.count}")

Firulais = Perro("Firulais")
parque = Park(Firulais)

parque.agregarPersonas(Persona("Nixon", True))
parque.agregarPersonas(Persona("Cristian"))
parque.agregarPersonas(Persona("Juan", isGrumpy = True))
parque.agregarPersonas(Persona("David", isGrumpy = True))
parque.agregarPersonas(Persona("Juanito", True))

parque.perroHuele()



