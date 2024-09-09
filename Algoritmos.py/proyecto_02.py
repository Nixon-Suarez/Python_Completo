
print("Ingrese el tamaño de la lamina en centimetros: ")
LargoL = float(input("Largo: ")) # Largo de la Lamina
AnchoL = float(input("Ancho: ")) # Ancho de la Lamina
AL = LargoL * AnchoL

print("Ingrese el tamaño de la caja en cm")
AltoC =  float(input("Alto: "))
AnchoC = float(input("Ancho: "))
LargoC = float(input("Largo: "))

LarOca = LargoC * 2 + AnchoC * 2 + 3  # Esto es lo Largo que ocupa la caja de la lamina
AnOca = AltoC + AnchoC # Esto es lo Ancho que ocupa la caja de la laminaTS
ArCL = LargoC + AnchoC # area que ocupa las cajas en la lamina

CC = int(LargoL / LarOca) #Cantidad de cajas que caben a lo largo 
CA = int(AnchoL / AnOca) # Cantidad de cajas que caben por ancho

CT = int(CC * CA)  # Cantidad de cajas que puedes sacar de la Lamina

preL = int( AL * 0.5) #Precio lamina
preM = int( 0.3 * preL ) #Precio mano de obra 30% de lo que vale la lamina
preT = preL + preM

if CT < 1:
     print("Cantidad de lamina insuficiente ")
else:    
     print ("Se pueden sacar", CT, "cajas.")
     print ("el precio total es: $", preT)
