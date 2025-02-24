import turtle
from linea import Punto, Linea
from circulo import Circulo

ESCALA = 50

def dibujar_plano():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()

    for i in range(-10, 11):
        turtle.goto(i * ESCALA, -5)
        turtle.write(str(i), align="center")
    turtle.goto(-10 * ESCALA, 0)
    turtle.pendown()
    turtle.goto(10 * ESCALA, 0)
    turtle.penup()

    for i in range(-10, 11):
        turtle.goto(-5, i * ESCALA)
        turtle.write(str(i), align="right")
    turtle.goto(0, -10 * ESCALA)
    turtle.pendown()
    turtle.goto(0, 10 * ESCALA)
    turtle.penup()


turtle.setup(800, 800)
turtle.title("Plano Cartesiano ")
dibujar_plano()

p1 = Punto(-5, -5)
p2 = Punto(0, 0)
centro = Punto(0, 0)
radio = 0

linea = Linea(p1, p2)
linea.dibujarLinea()

circulo = Circulo(centro, radio)
circulo.dibujarCirculo()

turtle.done()
