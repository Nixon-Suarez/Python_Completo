import csv
# Configuración
csv_file = 'C:\\Users\\Nixon\\Downloads\\data.ccv.xlsx' 
# se debe poner doble \\ ya que uno solo lo toma como excepcion 
sql_file = 'inserciones.sql'
table_name = 'employees'
 
# Abrir el archivo CSV y el archivo SQL
with open(csv_file, mode='r') as csv_f, open(sql_file, mode='w') as sql_f:
    csv_reader = csv.reader(csv_f)
   
    # Leer la primera línea (encabezados)
    headers = next(csv_reader)
   
    # Crear la plantilla para el script de inserción
    for row in csv_reader:
        # Usar repr() para manejar caracteres especiales
        values = ', '.join(repr(value) for value in row)
        sql_f.write(f"INSERT INTO prueba_app.Copy_employee ({', '.join(headers)}) VALUES ({values});\n")
 
print(f"Script de inserción creado en inserciones.sql")