import re 

codigo_cinco_digitos = '12345'
codigo_nueve_digitos = '12345-6789'
numero_telefono = '123-456-7890'

# /hola/ = taxto especifico que hay que e contrar 
# \d = digitos 
# \W = letra
# . = any character 
# + = una o mas acurrencias del caracter anterior 
# * = cero o mas acorrencias 
# ? = cero y una ocurrencia

#                     ⬇️r = indica que debe ignorara las siguientes barras diagonales        
regex_cinco_digitos = r'\d{5}'
#                          ☝️Agrupacion de 5 digitos

print(re.search(regex_cinco_digitos, codigo_cinco_digitos))
print(re.search(regex_cinco_digitos, codigo_nueve_digitos))
print(re.search(regex_cinco_digitos, numero_telefono))