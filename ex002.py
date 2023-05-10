
"""for x in range(Num+1):
    for i in range(x):
        print(x, end=" ")
    print()"""

def multiplicador(N):
    for x in range(1,N+1):
        print(str(x) * x, end= "  \n")

Num = int(input("Digite o número: "))
multiplicador(Num)
