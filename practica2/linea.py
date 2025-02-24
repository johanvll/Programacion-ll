import turtle
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea de {self.p1} a {self.p2}"

    def dibujarLinea(self):
        turtle.penup()
        turtle.goto(self.p1.x * 20, self.p1.y * 20)
        turtle.pendown()
        turtle.goto(self.p2.x * 20, self.p2.y * 20)
        turtle.penup()
