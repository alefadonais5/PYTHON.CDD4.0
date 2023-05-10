#faça uma função que conte quantas vogais tem um texto.

#O rato roeu a roupa do rei de Roma
def vogais(T):
    Cont = 0
    for x in T:
        if x in "aeiouAEIOU": #if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":"""
            Cont=Cont+1
    print(Cont)

texto = "O rato roeu a roupa do rei de Roma"
vogais(texto)

