# celular1_marca = "samsung "
# celular2_marca = "apple"
# celular3_marca = "huawei"

# celular1_modelo = "S23"
# celular2_modelo = "iPhone 15"
# celular3_modelo = "P20 pro"

# celular1_camaraF = "24MP"
# celular2_camaraF = "24MP"
# celular3_camaraF = "8MP"

# celular1_camaraT = "48MP"
# celular2_camaraT = "48MP"
# celular3_camaraT = "12MP"

#sin_OOP☝️--------------------

# clase⬇️
# class Celular(): #clases siempre con pascalcase 
#     # atributos ⬇️
#     marca = "samsung"
#     modelo = "S23"
#     camaraF = "24MP"
#     camaraT = "48MP"   

# Objeto de la clase Celular (Un objeto es una instacia de la clase por que es el resultado de la clase)
# celular1 = Celular()

class Celular:
    # metodo constructor se ejecuta antes que todo 
    def __init__(self, marca, modelo, camaraF, camaraT):
        #atributos de instancia 
        self.marca = marca
        self.modelo = modelo
        self.camaraF = camaraF
        self.camaraT = camaraT

    #metodos: es una funcion dentro de una clase  
    def llamar(self):
        print(f"Llamando desde un {self.marca}...")
    
    def colgar(self):
        print(f"Llamada finalizada desde un {self.marca}...")

celular1 = Celular("samsung", "S23", "24MP", "48MP")
celular2 = Celular("apple", "iPhone 15", "24MP", "48MP")

print(celular1.marca)
print(celular2.marca)

print(celular2.llamar())