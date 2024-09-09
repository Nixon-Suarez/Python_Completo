import mysql.connector

conexion = mysql.connector.connect(user = 'root', 
                                   password = '',
                                   host = 'localhost',
                                  #? ⬇️ usar una base de datos asi se puede o como se pone abajo al usar use 
                                   database = 'pepes',
                                   port = 3306,
                                  )

#* print(conexion)
cursor = conexion.cursor()
# CRUD = CREATE READ UPDATE DELETE 
#! Actualizar tablas (Update)
# sql = """ UPDATE empresa1 SET DireccionEmpresa = 'cll 898' WHERE DetalleEmpresa = 'Arturo calle' """
# cursor.execute(sql)

#! crear tabla (Create table)
# sql = """ create table empresa1 (IdEmpresa INT AUTO_INCREMENT PRIMARY KEY, DireccionEmpresa varchar(40), DetalleEmpresa varchar(100) )"""
# cursor.execute(sql)
# conexion.commit()

#! Borrar datos (Delete)
# sql = """DELETE FROM cliente WHERE IdCliente = 14;"""
# cursor.execute(sql)
# sql = """SELECT * FROM cliente"""
# verificamos que se halla eliminado 👇
# cursor.execute(sql)
# for i in cursor:
#         print(i)

#! seleccionar (Select-cursor.fetchall)
#                                ⬇️LIMIT = limita a los primeros 5 resultados
#sql = """SELECT * FROM empresa1 LIMIT 2 OFFSET 2""" 
#                                         ☝️OFFSET = esto representa desde donde inicia
# sql = """SELECT * FROM empresa1 """
# sql = """SELECT DireccionEmpresa FROM empresa1 """
# sql = """SELECT * FROM empresa1 WHERE IdEmprese = 1"""
# sql = """SELECT * FROM empresa1 WHERE DetalleEmpresa LIKE "%violeta%" """
# sql = """SELECT * FROM empresa1 ORDER BY DetalleEmpresa DESC"""

# cursor.execute(sql)
# for i in cursor:
#     print(i)
# # #? hacen lo mismo ☝️👇
# aqui se almacena en la variable empresas 
#                   fetchall trae todo lo consultado y tambien existe fetchone que trea la primera
# empresas = cursor.fetchall()
# for empresa in empresas:
#     print(empresa)


#! editar una tabla (Alter table)
# sql = """ALTER TABLE empresa ADD COLUMN IdEmpresa INT AUTO_INCREMENT PRIMARY KEY"""
# cursor.execute(sql)
# conexion.commit()

#! Insertar (Insert into)                                               
#                                                                       ⬇️%s asi se asigna que se va a ingresar un srting
# sql = """INSERT INTO empresa1 (DireccionEmpresa, DetalleEmpresa) VALUES (%s, %s)"""
# valores = ("Cll 30 sur", "violeta")
# cursor.execute(sql, valores)
#? asi se inserta una vez ☝️
#?⬇️ asi se insertan mas de una insercion al tiempo
# valores = [
#     ("Cll 40 sur", "Arturo calle"),
#     ("Cll 90 sur", "BBW"),
#     ("Cll 99 sur", "Sony"),
#     ("Cll 23 sur", "Gabys")
#     ]
# cursor.executemany(sql, valores)

# ⬇️nos permite ver en que cuentos registro inserto 
# print(f"{cursor.rowcount} nuevos registros")

#! ver tablas 
# cursor.execute("show tables")
# for tabla in cursor:
#     print(tabla)

#! ver bases de datos existentes
# cursor.execute("show databases")
# for bd in cursor:
#     print(bd)

#! crear una base de datos
# cursor.execute("create database pepes")
#? usar una base de datos asi se puede o como se pone arriba al asignar conexion 
# cursor.execute("use pepes") 

conexion.commit()
conexion.close()