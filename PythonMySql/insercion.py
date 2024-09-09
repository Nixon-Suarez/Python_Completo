import mysql.connector

import pyttsx3
engine = pyttsx3.init()

def insertf(tell, name, age, gen):
    try:
        conexion = mysql.connector.connect(
                                user = 'root', 
                                password = '',
                                host = 'localhost',  
                                database = 'violeta1.0',                      
                                port = 3306,
        )
        cursor = conexion.cursor()

    #! Insertar (Insert into)                                               

        sql = """INSERT INTO cliente (TelefonoCliente, NombreCliente, EdadCliente, GeneroCliente) VALUES (%s, %s, %s, %s)"""
        valores = (tell, name, age, gen)
        cursor.execute(sql, valores)
        conexion.commit()

        #⬇️nos permite ver cuantos registro inserto 
        ultimo = f"{cursor.rowcount} nuevos registros insertados"
        engine.say(ultimo)
        engine.runAndWait() # reprodce la voz
        print(ultimo)
    except mysql.connector.Error as error:
        print("Error de MySQL", error)
    except ValueError as ve:
        print("Error en los datos proporcionados", ve)
    
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

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





#*YA