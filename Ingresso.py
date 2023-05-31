# Crie uma classe chamada ingresso, que possui um valor em reias e método imprimeJava
# - Crie uma classe VIP, que herda de Ingresso e possui um valor adicional.
# Crie um método que retorne o valor do ingresso VIP(com o adicional incluído)

class Ingresso():
    def __init__(self, Valor):
        self.Valor = Valor

    def ImprimeValor(self):
        print(f"O valor do ingresso é {self.Valor}")


class VIP(Ingresso):
    def __init__(self,Valor):
        super().__init__(Valor)

    def Valor_Adicional(self,Percentual):
        print(f"O valor do ingresso VIP é R${self.Valor+(Percentual/100*self.Valor)}")

b = Ingresso(100)
b.ImprimeValor()
A = VIP(250)
A.Valor_Adicional(10)


