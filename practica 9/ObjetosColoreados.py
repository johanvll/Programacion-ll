from abc import ABC, abstractmethod
import random
import math



class Coloreado:
    def como_colorear(self):

        pass

class Figura(ABC):
    def __init__(self, color=""):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Figura de color {self.color}"

    @abstractmethod
    def area(self):

        pass

    @abstractmethod
    def perimetro(self):

        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color=""):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado con lado {self.lado} y color {self.color}"


class Circulo(Figura):
    def __init__(self, radio, color=""):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo con radio {self.radio} y color {self.color}"


def main():

    colores = ["rojo", "azul", "verde", "amarillo", "negro"]


    figuras = []


    for i in range(5):
        tipo_figura = random.randint(1, 2)
        color = random.choice(colores)

        if tipo_figura == 1:
            lado = random.uniform(1.0, 10.0)  # Lado aleatorio entre 1 y 10
            figura = Cuadrado(lado, color)
        else:
            radio = random.uniform(1.0, 10.0)  # Radio aleatorio entre 1 y 10
            figura = Circulo(radio, color)

        figuras.append(figura)


    print("INFORMACIÓN DE LAS FIGURAS ")
    for i, figura in enumerate(figuras, 1):
        print(f"Figura {i}: {figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")


        if isinstance(figura, Coloreado):
            print(f"Método para colorear: {figura.como_colorear()}")
        else:
            print("Esta figura no implementa el método como_colorear")


if __name__ == "__main__":
    main()
