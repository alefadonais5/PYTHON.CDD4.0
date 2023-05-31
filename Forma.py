class Forma():
    def __init__(self):
        self.Area = 0
        self.Perimetro = 0


class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def Calcular_Area(self,Base, Altura):
        self.Area = Base*Altura
        print(f"A área do retângulo é {self.Area}")   #return self.Area

    def Calcular_Perimetro(self,Base, Altura):
        self.Perimetro = (Base*2) + (Altura*2)
        print(f"O perímetro do retângulo é {self.Perimetro}")

class Triangulo(Forma):
    def __init__(self):
        super().__init__()

    def Calcular_Area(self,Base, Altura):
        self.Area = Base*Altura/2
        print(f"A área do triângulo é {self.Area}")

    def Calcular_Perimetro(self, Lado1, Lado2, Lado3):
        self.Perimetro = Lado1 + Lado2 + Lado3
        print(f"O perímetro do triângulo é {self.Perimetro}")




Retangulo = Retangulo()
Retangulo.Calcular_Area(3,5)
Retangulo.Calcular_Perimetro(3,5)

Triangulo = Triangulo()
Triangulo.Calcular_Area(6,6)
Triangulo.Calcular_Perimetro(3,4,5)


