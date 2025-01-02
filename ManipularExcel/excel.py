import pandas as pd
import numpy as np

# df = data frame 
df_excel = pd.read_excel('archivo.xlsx')
print(df_excel)


# # Leer un archivo Excel
# df = pd.read_excel('archivo.xlsx')

# # Mostrar las primeras 5 filas del archivo
# print(df.head())

# # Modificar un valor específico
# df.loc[0, 'Columna'] = 'Nuevo valor'

# # Guardar los cambios en un nuevo archivo Excel
# df.to_excel('archivo_modificado.xlsx', index=False)