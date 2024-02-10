import math

class FiguraGeometrica:
    def calcula_area(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return self.base * self.altura

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcula_area(self):
        return self.lado * self.lado

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcula_area(self):
        return math.pi * self.radio*2

# Ejemplo del objeto
triangulo = Triangulo(5, 8)
print(f"El area del triangulo es:", triangulo.calcula_area())

cuadrado = Cuadrado(4)
print(f"El area del cuadrado es:", cuadrado.calcula_area())

circulo = Circulo(3)
print(f"El area del circulo es:", circulo.calcula_area())