import turtle
class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio {self.radio}"

    def dibujarCirculo(self):
        turtle.penup()
        turtle.goto(self.centro.x * 20, (self.centro.y - self.radio) * 20)
        turtle.pendown()
        turtle.circle(self.radio * 20)
        turtle.penup()
