import turtle
ventana = turtle.Screen()
ventana.bgcolor("white")

tortuga = turtle.Turtle()
tortuga.speed(1)

for _ in range(5): 
    tortuga.forward(300)
    tortuga.right(144)

ventana.exitonclick()