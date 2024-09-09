import mysql.connector

import pyttsx3
engine = pyttsx3.init()

def select (op):
    try:
        conexion = mysql.connector.connect(
                                user = 'root',    
                                password = '',
                                host = 'localhost',  
                                database = 'violeta1.0',                      
                                port = 3306,
        )
        cursor = conexion.cursor()

    #! seleccionar (Select) 

        if op == 1:
            # op 1 selecciona todo con un inicio y un limite 
            n1v = "Ingrese el limite:"
            engine.say(n1v)
            engine.runAndWait() # reprodce la voz
            n1 = int(input("Ingrese el limite:\n")) #limite
            n2v = "Ingrese el inicio:"
            engine.say(n2v)
            engine.runAndWait() # reprodce la voz
            n2 = int(input("Ingrese el inicio:\n"))#inicio
            sql = f"""SELECT * FROM cliente LIMIT {n1} OFFSET {n2}""" 
        elif op == 2:
            # op 2 buscar columna especifica
            namecolumnv = "ingrese el nombre de la columna: "
            engine.say(namecolumnv)
            engine.runAndWait() # reprodce la voz
            namecolumn = input("ingrese el nombre de la columna:\n ") #nombre de la columna
            sql = f"""SELECT {namecolumn} FROM cliente"""
        elif op == 3:
            # op 3 selecciona todo filtrando por lo seleccionado 
            selcondiv = ("""ingrse por que quiere filtar:
                                Id [1]
                                Like [2]
                                Between [3]\n
                                """)
            engine.say(selcondiv)
            engine.runAndWait() # reprodce la voz
            selcondi = int(input("""ingrse por que quiere filtar:
                                Id [1]
                                Like [2]
                                Between [3]\n
                                """)) 
            
            if selcondi == 1:
                print(" filtro por id")
                idV = "ingrese el ID que desea seleccionar:\n "
                engine.say(idV)
                engine.runAndWait() # reprodce la voz
                id = int(input("ingrese el ID que desea seleccionar:\n "))
                sql = f"""SELECT * FROM cliente WHERE  IdCliente = {id}"""

            elif selcondi == 2:
                namecolfiltroV = ("nombre de la columna a filtrar:\n ")
                engine.say(namecolfiltroV)
                engine.runAndWait() # reprodce la voz
                namecolfiltro = input("nombre de la columna a filtrar:\n ")
                wordV = "palabra a buscar en esa columna:\n "
                engine.say(wordV)
                engine.runAndWait() # reprodce la voz
                word = input("palabra a buscar en esa columna:\n ")
                sql = f"""SELECT * FROM cliente WHERE {namecolfiltro} LIKE "%{word}%" """ 
            elif selcondi == 3:
                rangIniV = "Ingrese el punto de inicio: "
                engine.say(rangIniV)
                engine.runAndWait() # reprodce la voz
                rangIni = int(input("Ingrese el punto de inicio:\n "))

                rangFinv = ("Ingrese el punto de final:\n ")
                engine.say(rangFinv)
                engine.runAndWait() # reprodce la voz
                rangFin = int(input("Ingrese el punto de final:\n "))

                sql = f"""SELECT * FROM cliente WHERE IdCliente BETWEEN {rangIni} AND {rangFin};"""
            else:
                final = "Tal opcion no existe consulto no realizada exitosamente\n---ingrese nuevamente---"
                print(final)
                return

        else:
            finalfinal = "Tal opcion no existe consulto no realizada exitisamente\n---ingrese nuevamente---"
            print(finalfinal)
            return

        cursor.execute(sql)
        for i in cursor:
            print(i)

        conexion.commit()
    
    except mysql.connector.Error as error:
        errores = "Error de MySQL", error

        print(errores)
    except ValueError as ve:
        print("Error:", ve)
    
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


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
#*YA


