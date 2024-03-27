import sys
import math
def somar (x,y):
    return (x+y)
 
def multiplicar (x,y):
    return (x*y)

def subtrair (x,y):
    return (x-y)

def dividir (x,y):
    return (x/y)

def exponencial (x,y):
    return (x**y)

def calculo2 (x,y):
     return dividir(subtrair(x,y),somar(x,y))

def calculo3 (x,y):
    return (calculo2 (x,y) ** 3)

def raiz (x):
    return (math.sqrt(x))

def calculo4 (x,y):
    t1= subtrair(x,y)
    t2= somar (x,y) *3
    t3= dividir (t1,t2)
    return (t3 **4)


while True:
    a = int(input("digitar a : "))
    b = int(input("digitar b : "))

    print("======================")

    print("1-somar")
    print("2-dividir")
    print("3-multiplicar")
    print("4-subtrair")
    print("5- exponencial")
    print("0- sair")
    print("6- calculo2")
    print("7- calculo3")
    print("8- calculo4")
    print("9-raiz")
    op= int(input("qual operaçâo?"))
    if op==1:
        print(somar(a,b))
    if op==2:
        print(dividir(a,b))

    if op==3:
        print(multiplicar(a,b))

       

    if op==4:
        print(subtrair(a,b))

    if op==5:
        print(exponencial(a,b))
    if op==6:
        print(calculo2(a,b))   

    if op==7: 
        print(calculo3(a,b))

    if op==8:
        print(calculo4(a,b))

    if op==9:
        print(raiz (a))

    print(somar(a,b)**3)
    if op==0:
        sys.exit()
