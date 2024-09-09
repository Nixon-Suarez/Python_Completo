# para que funcione VSC debe estar como administrador 
import mysql.connector
import pyttsx3
engine = pyttsx3.init()

def update (columna, valor, condicion, condicionCol):
    try:
        conexion = mysql.connector.connect(
                                user = 'root', 
                                password = '',
                                host = 'localhost',  
                                database = 'violeta1.0',                      
                                port = 3306,
        )
        cursor = conexion.cursor()

    #! Actualizar tablas (Update)

        # Actualizar tablas (Update) usando parámetros
        sql = f"""UPDATE cliente 
                  SET {columna} = %s
                  WHERE {condicionCol} = %s;"""
        cursor.execute(sql, (valor, condicion))

        # Verifica la actualización
        sql = f"""SELECT * FROM cliente WHERE {condicionCol} = %s;"""
        cursor.execute(sql, (condicion,))
        result = cursor.fetchall()
        for row in result:
            print(row)
        print("Actualización exitosa.")

        conexion.commit()

    except mysql.connector.Error as error:
        print("Error de MySQL", error)
    
    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


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

#Ya





