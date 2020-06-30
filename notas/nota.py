import conexion.connect
import datetime

conn=conexion.connect.connect()
cur=conn[0]
database=conn[1]



class Nota:

    def __init__(self,usuario_id,titulo,nota):
        self.usuario_id=usuario_id
        self.titulo=titulo
        self.nota=nota

    def crear (self):
        sql="INSERT INTO notas VALUES (NULL,%s,%s,%s,NOW())"
        user=(self.usuario_id,self.titulo,self.nota)
        cur.execute(sql,user)
        database.commit()
        if cur.rowcount>0:
            print("Guardando")
        else:
            print("Hubo un inconveniente, no se guardo tu nota.")

    def ver  ( self ):
        sql=f"SELECT * FROM notas WHERE usuario_id={self.usuario_id}"

        cur.execute(sql)
        titulos=cur.fetchall()
        return titulos

    def borrar (self):
        sql=f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND  titulo LIKE '%{self.titulo}%' "
        cur.execute(sql)
        database.commit()




"""
    def vernota ( self ):
        print("----------NOTA.PY self titulo es igual a {}".format(self.titulo))
        sql=f"SELECT * FROM notas WHERE titulo={self.titulo}"
        cur.execute(sql)
        ("--------------cur execute")
        nota=cur.fetchone()
        ("----------------fetchone execute")
        print("---------imprimiendo el fetchone", nota)
        return nota
"""
