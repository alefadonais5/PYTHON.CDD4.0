class Atleta():
    def __init__(self, Peso):
        self.Aposentado = False
        self.Peso = Peso
        self.Aquecendo = False
        self.Correndo = False
        self.Nadando = False
        self.Pedalando = False

    def Aposentar (self):
        self.Aposentado = True
        print("Está aposentado")

    def Aquecer (self):
        if self.Aposentado == False:
            self.Aquecendo = True
            print("O atleta está aquecendo...")
        else:
            print("O atleta está aposentado...")


class Corredor(Atleta):
    def __init__(self,Peso):
        super().__init__(Peso)

    def Correr(self):
        if self.Aposentado==False:
            if self.Aquecendo==True:
                print("Está correndo....")
                self.Aquecendo=False
                self.Correndo = True
            else:
                print("O atleta não está aquecendo, não pode correr agora")
        else:
            print("O atleta está aposentado")

class Nadador(Atleta):
    def __init__(self,Peso):
        super().__init__(Peso)

    def Nadar(self):

        if self.Aposentado==False:
            if self.Aquecendo==True:
                print("O atleta está nadando....")
                self.Aquecendo=False
                self.Nadando = True
            else:
                print("O atleta não está aquecendo, não pode nadar agora")
        else:
            print("O atleta está aposentado")

class Ciclista(Atleta):
    def __init__(self,Peso):
        super().__init__(Peso)

    def Pedalar(self):

        if self.Aposentado==False:
            if self.Aquecendo==True:
                print("O atleta está pedalando....")
                self.Aquecendo=False
                self.Pedalando=True
            else:
                print("O atleta não está aquecendo, não pode pedalar agora")
        else:
            print("O atleta está aposentado")