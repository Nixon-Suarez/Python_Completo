#* se implementa el menu para la tabla cliente
# debe ingresar, actualizar, eliminar, consultar registro, y opcion para hacer una busqueda por medio de un filtro 
# produccion de voz 
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