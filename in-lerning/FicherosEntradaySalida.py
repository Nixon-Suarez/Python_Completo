archovoN = open('valores.txt', 'r')
archovoS = open('valores_totales.txt', 'w')
print('Procesando entrada')
suma = 0
for linea in archovoN: # Por cada linea de el archivoN
    suma += int(linea) # va a sumar este como un entero 
                        #*   ⬇️indica que se va a insertar dentro del archivoS 
    print(linea.rstrip(), file=archovoS) # va a imprimir cada una de las lineas del archivoN en el archivoS 
print('\nTotal: ' + str(suma), file=archovoS) #Mensaje en el archivoS al terminar el for y tener la suma en el total 
archovoS.close() # cierra los archivos 
archovoN.close()
print('Salida Completa')

  
