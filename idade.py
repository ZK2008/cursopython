def crianca (x):
    if x < 12:
        return True 
    else: 
        return False
def pre (x):
    if x > 11 and x < 16:
        return True 
    else: 
        return False 
def jovem (x):
    if x > 15 and x < 25: 
        return True
    else:
        return False
def jovem_adulto (x):
    if x > 24 and x < 36 :
        return True
    else: 
        return False
def adulto (x):
    if x > 35 and x < 66 :
        return True
    else:
        return False
def idoso (x):
    if x > 65 :
        return True
    else:
        return False
a = int(input("qual e sua idade? :")) 
if crianca(a) == True :
    print("voce e uma crianca")
else:
    if pre(a) == True :
        print("voce e um pre")
    else:
        if jovem(a) == True :
            print("voce e jovem") 
        else:
            if jovem_adulto(a) == True :
                print("voce e jovem_adulto")
            else:
                if adulto(a) == True :
                    print("voce e adulto")
                else:
                    if idoso(a) == True :
                        print("voce e idoso")        