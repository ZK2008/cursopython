from fastapi import FastAPI

app = FastAPI() 

@app.get("/ola/{nome}/{idade}")
def ola (nome:str, idade:str,):
    x= " ola " + nome + " ,sua idade é " + str(idade) + " anos "
    return{"msg":x}
    return {"msg":"ola"}

@app.post("/vlw")
def valeu ():
    return {"msg":"ok"}

@app.put("/blz")
def beleza ():
    return {"msg":"ok"}

@app.delete("/srf")
def surf ():
    return{"msg":"ok"}

@app.get("/somar/{x}/{y}")
def somar (x:int,y:int):
    return{"msg":x+y}

@app.("/quadrado/{x}/{y}")
def quadrado (x:int,y:int):
    return{"msg":(x+y)**2}

