import hashlib

def initial():
    r = input("qual senha")
    f = input("sua frase")
    return r + "#" + f

def crypto(senha):
    x=hashlib.sha512(senha.encode("utf-8")).hexdigest()
    return x

def estrela(minions):
    estrela_invertida=minions [::-1]
    print(estrela_invertida)#output:"olpmxE"
       


if __name__=="__main__":
    while True:
        x = initial()
        print(crypto(x))
        print(estrela(x))



 
