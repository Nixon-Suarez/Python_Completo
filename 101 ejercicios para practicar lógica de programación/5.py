#5 ÁREA DE UN POLÍGONO
#  Crea una única función (importante que sólo sea una) que sea capaz
#  de calcular y retornar el área de un polígono.
#   - La función recibirá por parámetro sólo UN polígono a la vez.
#  - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

# Area de un cuadrado es Lado x Lado 
# Area de un Triangulo es Base x Altura / 2
# Area de un rectángulo es Base x Altura


class Poligono:
    def __init__(self, nombre, base, altura):
        self.nombre = nombre
        self.base = base
        self.altura = altura

    def calcular_area(self):
        if self.nombre == "cuadrado" or self.nombre == "c":
            return self.base * self.base
        elif self.nombre == "rectángulo" or self.nombre == "r":
            return self.base * self.altura
        elif self.nombre == "triangulo" or self.nombre == "t":
            return (self.base * self.altura) / 2
        else:
            return None
try:
    while True:
        figura = input("Ingresa la figura (nombre completo o su inicial: cuadrado, rectángulo, triangulo): ").lower()
        alturas = int(input("Ingrese la altura: "))
        bases = int(input("Ingrese la base: "))

        poli = Poligono(figura, bases, alturas)
        area = poli.calcular_area()

        if area is not None: # se valida que no este vacio 
            print(f"El área del {figura} es: {area}")
        else:
            print("No se reconoce el polígono.")
        
        cont = input("¿Desea calcular el área de otra figura? (s/n): ")
        if cont.lower() == "n":
            break
except ValueError as ve:
    print("Error en los datos proporcionados", ve)
