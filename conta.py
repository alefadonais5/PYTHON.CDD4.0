import datetime
class Conta:
    def __init__(self, Numero_Conta, Saldo, Status, Nome_Cliente, Tipo_Conta, Limite=0, Limite_Usado=0):

        self.Nome_Cliente = Nome_Cliente
        self.Numero_Conta = Numero_Conta
        self.Saldo = Saldo
        self.Status = Status
        self.Tipo_Conta = Tipo_Conta
        self.Limite = Limite
        self.Limite_Usado = Limite_Usado


    def Depositar(self, Deposito):
        if self.Status == "Ativado":
            if self.Saldo >= 0:
                self.Saldo = Deposito+self.Saldo
                return self.Saldo
                Extrato.write(f'Deposito R$ {Deposito} ocorrido em:')
            else:
                self.Limite_Usado = Deposito+self.Saldo
                self.Saldo = self.Saldo + Deposito
                return self.Limite_Usado, self.Saldo

        else:
            print("Conta está desativada")

    def Sacar(self, Saque):
        if self.Status == "Ativado":
            if Saque < self.Saldo or Saque == self.Saldo:
                self.Saldo = self.Saldo-Saque
                print(f'Seu saldo é {self.Saldo}')
                inforDoTxt = f'Foi sacado R$ {Saque}'

            else:
                self.Limite_Usado = Saque-self.Saldo
                self.Saldo = self.Saldo-Saque
                print(f'Seu limite usado é {self.Limite_Usado} e o saldo é {self.Saldo}')

        else:
            print("Conta está desativada")

    def Desativar (self):
        if self.Status == "Ativado":
            if self.Saldo == 0:
                self.Status = "Desativado"
            else:
                print(f"O saldo precisa está zerado, seu saldo é {self.Saldo}")
        else:
            print("Sua conta já está desativada.")

    def Ativar_Conta(self):

        if self.Status == "Desativado":
            self.Status = "Ativado"
        else:
            print("A conta já está ativada.")
    def Verificar(self):
        if self.Status == "Ativado":
            if self.Saldo > 0:
                print(f"Seu saldo é R${self.Saldo}.")
            else:
                print(f"Seu saldo está negativo no valor de R${self.Saldo}")
        else:
            print("Conta desativada, não tem saldo....")

    def Ativar_Limite(self, Limite):
        if self.Saldo != 0 and self.Status == "Ativado":
            self.Limite = Limite
        else:
            print("Sua conta está desativada, não pode ser utilizada.")

    def Desativar_Limite(self):
        if self.Limite > 0:
            self.Limite = False
            return self.Limite

    def Extrato_Conta(self, add):
        self.add = add
        with open('Extrato.txt', 'a') as Extrato: #não estou conseguindo inserir as movimentações
            Extrato.write(f'Nome: {self.Nome_Cliente}\nNúmero da conta: {self.Numero_Conta}\nSaldo: {self.Saldo}\nTipo da conta: {self.Tipo_Conta}\nSaques')
            Extrato.write(add)
C1 = Conta(254,850, "Ativado", "Opal", "Corrente")
#C2 = Conta.Extrato_Conta(253,1000,"Ativado", "Opal", "Poupança")
C1.Ativar_Limite(300)
var = C1.Sacar(700)
var1= C1.Depositar(700)
print(var1)
C1.Extrato_Conta()