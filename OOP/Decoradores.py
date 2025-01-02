# un decorador agrega una funcionalidad extra a una funcion ya creada y ejecuta la nueva con las modificaciones agregadas

# 1ro inicia la funcion 
def decorador(funcion):
    def funcion_modificada():
        #2do ejecuta esta parte de la funcion
        print("Antes de LLanar a la funcion ")
        #3ro llama a la funcion externa que pasamos como parametro
        funcion()
        #4to ejecuta esta parte
        print("Despues de llamar a la funcion ")
    return funcion_modificada

# la funcion decoradora crea una funcion  que ejecuta un codigo x ejecuta la funcion que le pasamos como parametro ejecuta otro codigo y y retorna la funcion que creo 

# def saludo():
#     print("Hola Mundo")

# saludoModificado = decorador(saludo)
# saludoModificado()

# esto⬇️ es lo mismo que esto ☝️
# se puede llamar distinto a decorador se le pone asi porque asi se llama la funcion de arriba 
@decorador # esto llama al decorador y lo que este abajo es la funcion 
def saludo():
   print("Hola Mundo")
saludo()

# ☝️Cuando usamos @decorador (@nombre_funcion) le estamos diciendo que pase da funcion que esta debajo como parametro (como funcion decoradora)

