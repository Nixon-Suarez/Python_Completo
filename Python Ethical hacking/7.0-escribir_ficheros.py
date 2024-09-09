# ficheros son archivos 👍
# write permite sobreescribir un archivo ya existente o crearlo desde cero 
#? ya que se sobre escribe si se cirra el archivo y se agraga otra cosa se borrara lo anterios y quedara lo actualizado

archivo = open("nombres.txt","w")

for i in range(10):
    archivo = open("nombres.txt","w")  # se abre 10 veces el archivo y diez veces se cierra , pero solo la última operación es efectiva
    archivo.write("Pedro\n")
    archivo.write(str(i))

archivo.close()