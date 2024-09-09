# un decorador agrega una funcionalidad extra a una funcion ya creada y ejecuta la nueva con las modificaciones agregadas

def decorador(funcion):
    def funcion_modificada():
        print("Antes de LLanar a la funcion ")
        funcion()
        print("Despues de llamar a la funcion ")
    return funcion_modificada

# la funcion decoradora crea una funcion  que ejecuta un codigo x ejecuta la funcion que le pasamos como parametro ejecuta otro codigo y y retorna la funcion que creo 

# def saludo():
#     print("Hola Mundo")

# saludoModificado = decorador(saludo)
# saludoModificado()

# esto⬇️ es lo mismo que esto ☝️
@decorador # esto llama al decorador y lo que este abajo es la funcion 
def saludo():
   print("Hola Mundo")

saludo()