from banco import banco
import json,datetime

class Segredos:
    def __init__(self):
        b = banco()
        global Conn
        global Cur
        Conn = b.conectabanco('D:\Projetos\Android\Api OurSecrets\Banco\BANCO_API.FDB')
        Cur  = Conn.cursor()

    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")


    def insereSegredo(self,operador,seg,ativo):
        try:
            Cur.execute("INSERT INTO SEGREDOS(SEGREDO,OPERADOR,ATIVO) VALUES("+"'"+seg+"'"+","+"'"+operador+"'"+","+"'"+ativo+"'"+")")
            Conn.commit()
        except Exception as Msg:
            print(Msg)
            
    def retornaSegredos(self,Codigo):
        try:
            if(Codigo == 0) or (Codigo == ""):
                resultado = Cur.execute("SELECT FIRST 10 CODIGO,SEGREDO FROM SEGREDOS WHERE DATA = CURRENT_DATE AND ATIVO = 1 ORDER BY CODIGO DESC")                            
            else:
                resultado = Cur.execute("SELECT CODIGO,SEGREDO FROM SEGREDOS WHERE CODIGO BETWEEN "+"'"+str(Codigo)+"'"+" AND "+"'"+str(Codigo+10)+"'"+" ORDER BY CODIGO DESC")            
            item = [dict(zip([key[0] for key in Cur.description],row)) for row in resultado]
            return json.dumps({'segredos':item})    
        except Exception as Msg:
            print(Msg)
        
                
