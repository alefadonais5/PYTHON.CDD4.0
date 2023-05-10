#Jogo da forca, cadastrar 10 nomes(com a mesma quantidade de letras) em python.
#Quantidade de tentativa.
#bliblioteca py  game
#Pesquisar como fazer.
#função random faz sorteio aleatório

def somar (A,B):
    Soma = A+B
    print("A soma é ", Soma)
def subtrair (A,B):
    Sub = A-B
    print("A subtração é ", Sub)
def multiplicar (A,B):
    Multi = A * B
    print("A multiplicação é ", Multi)
def dividir (A, B):
    Div = A / B
    print("A divisão é ", Div)

resp = 0
while resp < 5:
    resp = int(input("1 - Somar \n 2 - Substrair \n 3 - Multiplicar \n 4 - Divisão \n 5 - Sair \n"))
    if resp == 5:
        print("Fim da Calculadora")
        break

    N1 = float(input("Digite o número 1: "))
    N2 = float(input("Digite o número 2:"))

    match resp:
        case 1:
            somar(N1,N2)
        case 2:
            subtrair(N1,N2)
        case 3:
            multiplicar(N1,N2)
        case 4:
            dividir(N1,N2)


