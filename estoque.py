from fastapi import FastAPI

app = FastAPI() 

@app.get("/debito/{produto}/{quantidade}}")
def debito (produto:str , quantidade:int):
    return{"msg":"debito executado com sucesso"}

@app.get("/credito/{produto}/{quantidade}}")
def credito (produto:str , quantidade:int):
     return{"msg":"credito executado com sucesso"}

@app.get("/extrato_diario/{data}")
def extrato_diario (data:int):
     return{"msg":"ok"}

@app.get("/extrato_mensal/{ano}/{mes}/{dia}")
def extrato_mensal (ano:int , mes:int , dia:int):
     return{"msg":"ok"}
