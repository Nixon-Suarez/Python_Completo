import mysql.connector

import pyttsx3
engine = pyttsx3.init()

def deletef (column, filtro):
    try:
        conexion = mysql.connector.connect(
                                user = 'root', 
                                password = '',
                                host = 'localhost',  
                                database = 'violeta1.0',                 
                                port = 3306,
        )
        cursor = conexion.cursor()

        #! Borrar datos (Delete)
        sql = f"""DELETE FROM cliente WHERE {column} = %s;"""
        cursor.execute(sql, (filtro,))
        conexion.commit()

        finald = f"Se elimino exitosamente todas las filas en las que la columna {column} es igual a {filtro}\n"
        engine.say(finald)
        engine.runAndWait() # reproduce la voz    
        print(finald)

        # verificamos que se halla eliminado 👇
        sql = """SELECT * FROM cliente"""
        cursor.execute(sql)
        for i in cursor:
            print(i)
        
    except mysql.connector.Error as error:
        print("Error de MySQL", error)
    
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
        
columnv = "Ingrese la columna por la cual quiere filtrar para eliminar:"
engine.say(columnv)
engine.runAndWait() # reproduce la voz    
column = input("Ingrese la columna por la cual quiere filtrar para eliminar:\n")

filterv = "Ingrese el fitro por el cual eliminar:"
engine.say(filterv)
engine.runAndWait() # reproduce la voz   
filtro = int(input("Ingrese el fitro por el cual eliminar:\n"))

deletef(column, filtro)

#*YA  



