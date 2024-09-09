try:    # esto ejecutara si no se cumple la excepcion 
    print("hola mundo") 
except: # esto se ejecutara si se produce una excepcion 
    print("error en el codigo") 
finally:     # finally se ejecuta sin importar que se cumpla o no se cumpla la excepcion (finally no es obligatorio)
    print("Hola")

# ☝️ si se opera de esta manera sejecutara a menos que de un error o algo que no permita la ejecucion 
