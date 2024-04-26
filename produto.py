from fastapi import FastAPI 
import sqlite3
app=FastAPI()

@app.post("/inserir/{nome}/{descricao}")
def inserir(nome:str,descricao:str):
    
    conn = sqlite3.connect("/Users/Ijovem01/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute("""INSERT INTO produto (nome,descricao,saldo,status) VALUES (?,?,?,?)""", (nome,descricao,0,1))
    conn.commit()
    conn.close()
    
    return {"msg":"inserido com sucesso"}

@app.put("/alterar/{id}/{nome}/{descricao}")
def alterar(id:int,nome:str,descricao:str):

    conn = sqlite3.connect("/Users/Ijovem01/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET nome = ?, descricao = ? WHERE id = ? """, (nome, descricao, id))
    conn.commit()
    conn.close()

    return {"msg":"alterado com sucesso"}
    
@app.put("/cancelar/{id}")
def cancelar(id:int):
    
    conn = sqlite3.connect("/Users/Ijovem01/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET status = 0 WHERE id = ? """, (id,))
    conn.commit()
    conn.close()

    return {"msg":"cancelado com sucesso"}

@app.put("/ativar/{id}")
def ativar(id:int):

    conn = sqlite3.connect("/Users/Ijovem01/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET status = 1 WHERE id = ? """, (id,))
    conn.commit()
    conn.close()


    return {"msg":"ativado com sucesso"}

@app.get("/inicializar_saldo/{id}/{saldo}")
def inicializar_saldo(id:int,saldo:int):

    conn = sqlite3.connect("/Users/Ijovem01/turma202402/database/estoque.db")
    cur = conn.cursor()

    cur.execute(""" UPDATE produto SET saldo = ? WHERE id = ? """, (saldo,id,))
    conn.commit()
    conn.close()

    return {"msg":"inicializado saldo com sucesso"}





