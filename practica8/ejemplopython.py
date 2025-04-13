class A:
    def __init__(self, x):
        self.x = x

    def muestraX(self):
        return f"Valor de x: {self.x}"

class B:
    def __init__(self, y):
        self.y = y

    def muestraY(self):
        return f"Valor de y: {self.y}"

class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x)
        B.__init__(self, y)
        self.z = z

    def muestraTodos(self):
        return f"{self.muestraX()}, {self.muestraY()}, Valor de z: {self.z}"

objeto_d = D(1, 2, 3)
print(objeto_d.muestraTodos())
