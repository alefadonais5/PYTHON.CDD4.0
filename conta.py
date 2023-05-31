import datetime

Arquivo = open("Extrato.txt", "a")
class Conta:
    def __init__(self, Numero_Conta, Saldo, Status, Nome_Cliente, Tipo_Conta, Limite=0, Limite_Usado=0):

        self.Nome_Cliente = Nome_Cliente
        self.Numero_Conta = Numero_Conta
        self.Saldo = Saldo
        self.Status = Status
        self.Tipo_Conta = Tipo_Conta
        self.Data = datetime.datetime.now()
        self.Limite = Limite
        self.Limite_Usado = Limite_Usado


    def Depositar(self, Deposito):
        if self.Status == "Ativado":
            if self.Saldo >= 0:
                self.Saldo = Deposito+self.Saldo
                # return self.Saldo
                Arquivo.write(f'Foi depositado R$ {Deposito} em {self.Data}\n')#só funciona  sem o retorno

            else:
                self.Limite_Usado = Deposito+self.Saldo
                self.Saldo = self.Saldo + Deposito
                # return self.Limite_Usado, self.Saldo
                Arquivo.write(f'Foi depositado R$ {Deposito} em {self.Data}\n') #só funciona  sem o retorno

        else:
            print("Conta está desativada")

    def Sacar(self, Saque):
        if self.Status == "Ativado":
            if Saque < self.Saldo or Saque == self.Saldo:
                self.Saldo = self.Saldo-Saque
                # return self.Saldo
                Arquivo.write(f'Foi sacado R$ {Saque} em {self.Data}\n')#só funciona  sem o retorno

            else:
                self.Limite_Usado = Saque-self.Saldo
                self.Saldo = self.Saldo-Saque
                print(f'Seu limite usado é {self.Limite_Usado} e o saldo é {self.Saldo}')#só funciona  sem o retorno
                Arquivo.write(f'Foi sacado R$ {Saque} em {self.Data}\n')

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

    def Extrato_Conta(self):
        if self.Status == "Ativado":
            Arquivo.write(f"Número da conta: {self.Numero_Conta} \n Saldo: {self.Saldo}.")
            print("O extrato da sua conta foi gerado com sucesso.")
        else:
            print("Sua conta está desativada! Não pode gerar o extrato.")


C1 = Conta(254,850, "Ativado", "Opal", "Corrente")
C1.Depositar(50)
C1.Sacar(200)
C1.Depositar(50)
var = C1.Sacar(700)
var1= C1.Depositar(700)
C1.Extrato_Conta()
