import mysql.connector

#Conexion con la base de datos de mysql
def connect():
    database=mysql.connector.connect(

        host="localhost",
        user="root",
        password= "",
        database= "practica1",
        port=3306

        )

    cur=database.cursor(buffered=True)

    con_ok= [cur,database]
    return con_ok
