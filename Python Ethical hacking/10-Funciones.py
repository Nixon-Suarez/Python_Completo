
def adios_mundo():
    nombre = "Jorge"
    print("Adios" + nombre)
def hola_mundo ():
    nombre = "Pedro"
    print("Hola, {}".format(nombre))

# define el orden de ejecucion 👇esto generalmete esta predefinido 
def main():
    hola_mundo
    adios_mundo()
if  __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()