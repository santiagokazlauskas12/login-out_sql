#Clases Usuario para registrarse y logiarse
import datetime
import conexion.connect

conn=conexion.connect.connect()
cur=conn[0]
database=conn[1]

class Usuario:

    def __init__(self,name,last,mail,password,fecha=""):
        self.name=name
        self.last=last
        self.mail=mail
        self.password=password
        self.fecha=fecha


    def loguear (self):

        sql="INSERT INTO usuarios VALUES(NULL,%s,%s,%s,%s,%s)"
        usuario= (self.name,self.last,self.mail,self.password,self.fecha)
        cur.execute(sql,usuario)
        database.commit()

        print("--------------------ok")


    def registrar (self):
        sql="SELECT * FROM usuarios WHERE mail=%s and pass =%s"
        usuario=(self.mail,self.password)
        cur.execute(sql,usuario)
        return cur.fetchone()
