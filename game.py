import sys
import os
import random
def menu():
    print("0-sair")
    print("1-mega sena")
    print("2-lotofacil")
    print("3-gerar senha")
    r=int(input("qual jogo ?"))
    return r

def megasena():
    os.system("cls")
    print("megasena")
    r=int(input("quantos jogos ?"))
    for j in range (r):
        numeros=""
        for n in range(6):
            x = random.randrange(1,60+1)
            numeros=numeros+str(x)+ " "
           
        print(f" jogo {j+1}: {numeros}   ")
    p=input("ENTER p/NOVO JOGO")
    os.system("cls")

def lotofacil():
    os.system("cls")
    print("lotofacil")
    r=int(input("quantos jogos ?"))
    for j in range (r):
        numeros=""
        for n in range(15):
            x = random.randrange(1,25+1)
            numeros=numeros+str(x)+ " "
           
        print(f" jogo {j+1}: {numeros}   ")
    p=input("ENTER p/NOVO JOGO")
    os.system("cls")

def senha():
    os.system("cls")
    print("senha") 
    numeros=""
    for n in range(100):
        x = random.randrange(1,10)
        numeros=numeros+str(x)+ ""
    print(f" senha : {numeros} ")  
    p=input("ENTER p/NOVA SENHA")
    os.system("cls")

if __name__=="__main__":
    while True:
        resposta = menu()
        if resposta==0:
            sys.exit()
        if resposta==1:
            megasena()
        if resposta==2:
            lotofacil()
        if resposta==3:
            senha()


