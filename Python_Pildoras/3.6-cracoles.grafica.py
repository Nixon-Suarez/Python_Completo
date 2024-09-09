import random
import turtle

ventana = turtle.Screen()
ventana.title("Carrera de caracoles")
ventana.bgcolor("lightblue")
ventana.setup(width=800,height=600)

caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("red")
caracol1.penup()
caracol1.goto(-300,100)

caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("blue")
caracol2.penup()
caracol2.goto(-300,0)



meta=300
    
while True: 
    avance_caracol_1 = random.randint(1,20)
    avance_caracol_2 = random.randint(1,20)

    if avance_caracol_1 % 2 == 0 or avance_caracol_2 & 2 == 0:
        continue

    caracol1.forward(avance_caracol_1)
    caracol2.forward(avance_caracol_2)

    print(f"""
        caracol1 avanza, {avance_caracol_1}
        caracol2 avanza, {avance_caracol_2}
    """)
    print("..............................................")

    print(f"el caracol uno avanza {avance_caracol_1} espacios para un tatal de {caracol1.xcor()} espacios")
    print(f"el caracol dos avanza {avance_caracol_2} espacios para un tatal de {caracol2.xcor()} espacios")
    print(".....................................................")

    if caracol1.xcor() >=310 or caracol2.xcor() >=310:
        break

if caracol1.xcor() > caracol2.xcor():
    print("El ganador es caracol 1")
elif caracol2.xcor() > caracol1.xcor():
    print("caracol 2 a ganado")
else:
    print("Empate entre los caracoles")

ventana.exitonclick()


