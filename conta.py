class Conta:
    def __init__(self, Numero_Conta, Saldo, Status, Nome_Cliente, Tipo_Conta):

        self.Nome_Cliente = Nome_Cliente
        self.Numero_Conta = Numero_Conta
        self.Saldo = Saldo
        self.Status = Status
        self.Tipo_Conta = Tipo_Conta

    def Depositar(self, Deposito):
        self.Saldo = Deposito+self.Saldo
        return self.Saldo

    def Sacar(self, Saque):
        self.Saldo = self.Saldo-Saque
        return self.Saldo

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

C1 = Conta(254, 1500, "Ativado", "Cliente 1", "Corrente")
C2 = Conta(253,1000,"Ativado", "Opal", "Poupança")
