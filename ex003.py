

def pirammide(A):
    for x in range(1,A+1):
        for y in range(1, x+1):
            print(y, end=" ")
        print()

Num = int(input("Digite o número: "))
pirammide(Num)