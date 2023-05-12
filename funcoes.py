def somar (*numeros):
    soma = 0
    for y in numeros:
        soma = soma + y
    return soma

def subtrair (A,B):
    return A-B

def multiplicar (A,B):
    return A * B

def dividir (A, B):
    return A / B

def multiplicador(N):
    for x in range(1,N+1):
        print(str(x) * x, end= "  \n")

def pirammide(A):
    for x in range(1,A+1):
        for y in range(1, x+1):
            print(y, end=" ")
        print()


def vogais(T):
    Cont = 0
    for x in T:
        if x in "aeiouAEIOU": #if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":"""
            Cont=Cont+1
    return (Cont)

def alfabeto_inverte (T):
    Cont = 0
    Textoi = ""
    for x in range(len(T)-1,-1,-1):
        Textoi+=T[x]
        if T[x] != " ":
           Cont+=1

    print(Textoi)
    print(Cont)

def estoque(Nome, Quantidade, Valor):
    return Nome,Quantidade*Valor

def nova_lista(A):
    B=[]
    for y in A:
        if y not in B:
            B.append(y)
    print(B)
#set faz essa função no python