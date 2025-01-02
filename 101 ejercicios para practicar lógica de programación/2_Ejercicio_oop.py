import random

archivo = open("SpiasDetectados.txt","a")

class Perro():
    def __init__(self, nombre):
        self.nombre = nombre

    def Smell(self, persona):
        if persona.spy:
            if random.random() < 0.6:
                print(f"{self.nombre} bites {persona.nombre}")
                archivo.write(f"{self.nombre} detect a spy: {persona.nombre} \n")
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

class CountSpys():
    def __init__(self, archivo):
        self.archivo = archivo
        
    def cuentaEspias(self):
        with open(self.archivo, "r") as file:  # Usar 'self.archivo' y un bloque 'with'
            contador = 0

            leercontenido = file.read()
            CoList = leercontenido.split("\n")

            for i in CoList:
                if i:
                    contador += 1

            print(f"Número de espías: {contador}")


Firulais = Perro("Firulais")
parque = Park(Firulais)

parque.agregarPersonas(Persona("Nixon", True))
parque.agregarPersonas(Persona("Cristian"))
parque.agregarPersonas(Persona("Juan", isGrumpy = True))
parque.agregarPersonas(Persona("David", isGrumpy = True))
parque.agregarPersonas(Persona("Juanito", True))

parque.perroHuele()

contador_espias = CountSpys("SpiasDetectados.txt")
contador_espias.cuentaEspias()





