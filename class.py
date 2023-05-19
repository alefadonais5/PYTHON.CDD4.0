class Pessoas:
    def __init__(self, nome, peso, idade, comendo=False, falando=False):
        self.Nome = nome
        self.Peso = peso
        self.Idade = idade
        self.Comendo = comendo
        self.Falando = falando

    def Comer(self,Comida):
        self.Comida=Comida
        if self.Comendo == False:
            print(f"{self.Nome} foi comer! {self.Comida}")
            self.Comendo = True
        else:
            print(f"{self.Nome} estou comendo")

    def Parar_de_Comer(self):
        if self.Comendo == True:
            self.Comendo = False
            print(f"{self.Nome} parou de comer.")
        else:
            print(f"Não estou comendo")

    def falar(self):
        if self.Falando == False:
            if self.Comendo == False:
                print(f"{self.Nome} Pode falar...")
                self.Falando = True
            else:
                print(f"{self.Nome} Não pode falar. Porque está comendo")
        else:
                print(f"{self.Nome} pode falar")
                self.Falando = False
            
    def ParardeFalar(self):
        if self.Falando == True:
            self.Falando = False
            print(f"{self.Nome} parou de falar.")
        else:
            print(f"{self.Nome} está falando.")

P1 = Pessoas("João", 80, 23,True)
P2 = Pessoas("Opal", 65, 12)
P1.Comer("LAranja")
P1.Comer("Maçça")
P2.Comer("Arroz")
P2.Parar_de_Comer()
P1.falar()
P2.falar()
# print(vars(P1))
# print(vars(P1))
