from insercion import insertf
from actualizacion import update
from eliminacion import deletef
from seleccion import select

import pyttsx3

engine = pyttsx3.init()
def CRUD():
    while True:
        #? selccionar un modo
        seleccionv = ( """Bienvenido al servidor de Base de Datos violeta que desea realizar en la tabla cliente:
            Para Ingresar Datos presione 1
            Para Actualizar Datos presione 2
            Para Eliminar Datos presione 3
            Para Consultar Datos precione 4
            Para Salir presione 5\n""")
        engine.say(seleccionv)
        engine.runAndWait()
        seleccion = int(input( """Bienvenido al servidor de Base de Datos violeta que desea realizar en la tabla cliente:
            Para Ingresar Datos presione 1
            Para Actualizar Datos presione 2
            Para Eliminar Datos presione 3
            Para Consultar Datos precione 4
            Para Salir presione 5\n"""))

        if 1 <= seleccion <= 5:
            if seleccion == 1:
                #! Insertar (Insert into)     
                tellv = "Ingrese el Telefono del Cliente:"
                engine.say(tellv)
                engine.runAndWait() # reprodce la voz
                tell = input("Ingrese el Telefono del Cliente:\n")

                namev = "Ingrese el Nombre del Cliente: "
                engine.say(namev)
                engine.runAndWait() # reprodce la voz
                name = input("Ingrese el Nombre del Cliente:\n ")

                agev = "Ingrese la Edad del Cliente"
                engine.say(agev)
                engine.runAndWait() # reprodce la voz
                age = int(input("Ingrese la Edad del Cliente:\n "))

                genv = "Ingrese el genero del Cliente:"
                engine.say(genv)
                engine.runAndWait() # reprodce la voz
                gen = input("Ingrese el genero del Cliente:\n")

                insertf(tell, name, age, gen)

            elif seleccion == 2:
                #! Actualizar tablas (Update)

                columnav = "La columna que desea actualizar es:"
                engine.say(columnav)
                engine.runAndWait() # reprodce la voz
                columna = input("La columna que desea actualizar es:\n")

                condicionColv = "se actualizara cuando la columna:"
                engine.say(condicionColv)
                engine.runAndWait() # reprodce la voz
                condicionCol = input("se actualizara cuando la columna:\n")

                condicionv =f"{condicionCol} sea igual a:\n"
                engine.say(condicionv)
                engine.runAndWait() # reprodce la voz   
                condicion = input(f"{condicionCol} sea igual a:\n")  

                valorv = f"y el Valor que va a tomar {columna} es:\n"
                engine.say(valorv)
                engine.runAndWait() # reprodce la voz
                valor = input(f"y el Valor que va a tomar {columna} es:\n")

                final = f"la columna que se actualizo fue {columna} que tomo el valor de {valor} cuando la columna {condicionCol} es igual a {condicion} "
                engine.say(final)
                engine.runAndWait() # reprodce la voz
                print(final)

                update(columna, valor, condicion, condicionCol)

            elif seleccion == 3:
                #! Borrar datos (Delete)
                columnv = "Ingrese la columna por la cual quiere filtrar para eliminar:"
                engine.say(columnv)
                engine.runAndWait() # reproduce la voz    
                column = input("Ingrese la columna por la cual quiere filtrar para eliminar:\n")

                filterv = "Ingrese el fitro por el cual eliminar:"
                engine.say(filterv)
                engine.runAndWait() # reproduce la voz   
                filtro = int(input("Ingrese el fitro por el cual eliminar:\n"))

                deletef(column, filtro)

            elif seleccion == 4:
                #! seleccionar (Select)
                optionv = """Ingrese la opcion a consultar en la tabla cliente: 
                ingrese [1] para seleccionar todo con un inicio y un limite 
                ingrese [2] para buscar una columna especifica
                ingrese [3] para selecciona todo filtrando por lo seleccionado\n """
                engine.say(optionv)
                engine.runAndWait() # reprodce la voz
                option = int(input("""Ingrese la opcion a consultar en la tabla cliente: 
                                ingrese [1] para seleccionar todo con un inicio y un limite 
                                ingrese [2] para buscar una columna especifica
                                ingrese [3] para selecciona todo filtrando por lo seleccionado\n """))

                select(option)

            elif seleccion == 5:
                Mi5 = "\n¡Hasta luego Profe, Yo vere mi 5\n"
                print(Mi5)
                engine.say(Mi5)
                engine.runAndWait() # reprodce la voz

                break 

        else:
            fuerarango = "El numero elegido esta fuera de lo permitido: ingrese nuevamente\n"
            print(fuerarango)
            engine.say(fuerarango)
            engine.runAndWait()

CRUD()