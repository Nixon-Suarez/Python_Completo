primer_nombre = 'rigoberta'
segundo_nombre = 'menchu'
nota = 'Ganadora Premio Nobel de la Paz'

primer_nombre_cap = primer_nombre.capitalize() #capitalize = convierta la primera letra en mayuscula
segundo_nombre_cap = segundo_nombre.capitalize()
premio_ubicacion = nota.find('Premio')
premio_texto = nota[9:]

print(primer_nombre_cap)
print ( segundo_nombre_cap)
print(premio_ubicacion)
print(premio_texto)