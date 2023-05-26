class Animal():
    def __init__(self, Nome, Cor):
        self.Nome = Nome
        self.Cor = Cor

    def Comer(self):
        print(f"O {self.Nome} foi comer...")
    def EmitirSom(self):
        print(f"O {self.Nome} está emitindo som....")

class Gato(Animal):
    def __init__(self,A, B):
        super().__init__(A, B)

    def EmitirSom(self):
        print(f"O {self.Nome} está miando....")

class Cachorro(Animal):
    def __init__(self, A, B):
        super().__init__(A,B)

    def EmitirSom(self):
        print(f"O {self.Nome} está latindo....")

class Vaca(Animal):
    def __init__(self, A,B):
        super().__init__(A,B)

p1 = Vaca("Opal", "Preta")
p1.EmitirSom()