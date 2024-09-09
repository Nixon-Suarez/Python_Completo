#hace referencia a crear una clase a partir de multiples clases padre
# se hace de la misma forma que una herencia normal, solo que los multiples padres iran separados por comas

class Telefono:
    def __init__(self):
        pass

    def llamar(self):
        print("Llamando...")

    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass

    def tomar_foto(self):
        print("Tomando Foto.....")
    
class Reproductor:
    def __init__(self):
        pass

    def reproducir_musica(self):
        print("Reproduciendo Musica......")

    def reproducir_video(self):
        print("Reproduciendo Video......")

class Celular(Telefono, Camara, Reproductor):
#           ⬇️__del__ =  elimina los objrtos y clases cuando no se esten utilizando 
    def __del__(self):
        print("Telefono Apagado")

class Samsung(Celular):
    def marca(self):
        print("Soy Samsung")

movil = Samsung()
#      ⬇️ trae todas las funciones que contiene su argumento
print(dir(movil))