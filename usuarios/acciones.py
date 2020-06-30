import usuarios.usuario as crea
import datetime

class Acciones:

    def login(self):
        print("Por favor completa los siguientes parametros : \n")
        name=input("Nombre : ")
        last=input("Apellido : ")
        mail=input("Email : ")
        pasword =input("Pasword")
        fecha=datetime.datetime.now()

        #creamos el usuario con la classe USUARIO  y le pasamos los parametros
        user=crea.Usuario(name,last,mail,pasword,fecha)
        result=user.loguear()

        print("Bienvenido {} !!! \n tu usuario se a creado a las {}, ya puedes logiarte".format(name,fecha))

    def register (self):
        print("Ingresa tu mail y clave por favor")
        mail=input("Ingresa tu Email : \n")
        password=input("Ingresa tu password : \n")

        user=crea.Usuario("","",mail,password,"")
        reg_user=user.registrar()
        print("Bienvenido {} que deseas hcaer?".format(reg_user[1]))
        return reg_user
