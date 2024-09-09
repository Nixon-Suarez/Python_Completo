#usando algunas palabras reservadas sacaremos provecho de los valores de los atributos

class Persona:
    edad = 24
    nombre = "Juan"
    #* def hola(self):
    #*     self.edad_2 = 32

    # def __init__(self):
    #     self.edad_2 = 32

ingeniero = Persona()
#* ingeniero.hola()
print(ingeniero.edad)
#?  getattr = obtener el valor de la propiedad sin ejecutar la propiedad
#?       ⬇️     👇objeto      👇propiedad
print(getattr(ingeniero, 'nombre'))
# hacen lo mismo ☝️👇
print(ingeniero.nombre)

#?   ⬇️ hasattr = consulta si existe un atributo (¿tiene el atributo edad?)
if hasattr(ingeniero, 'edad') == True:
    respuesta = "si"
else:
    respuesta = "No"


print("El doctor dijo su edad?\n" + respuesta)
#?  ⬇️  setattr = asignarle un nuevo valor a una propiedad o atributo
setattr(ingeniero, "nombre", "Javier")
print("El nuevo nombre es: {}".format(getattr(ingeniero, 'nombre')))

#?   delattr = eliminar el atributo definido por fuera de la clase 
delattr(ingeniero, "nombre")
print("El antiguo nombre era: {}".format(getattr(ingeniero, 'nombre')))
