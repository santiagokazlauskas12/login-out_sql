import notas.nota as modelo
class AccionesNota:

    def menu(self):
        print("""

        Que accion deseas realizar :

        -Crear notas    (crear)
        -ver mis notas  (ver)
        -borrar Notas   (borrar)
        -Salir          (salir)
        """)

        accion= input("Escribe la opcion que deseas realizar").lower().strip()
        return accion

    def create (self,user_id):
        titulo=input("Por favor, ingresa el titulo de tu nota")
        nota=input("Por favor, ingresa el contenido de tu nota")
        #crear clase nota y pasarle las variables
        classnota=modelo.Nota(user_id,titulo,nota)
        classnota.crear()
        print("Se a guardado la nota ""{}"" exitosamente".format(titulo))

    def see (self,user_id):
        classnota=modelo.Nota(user_id," ", " ")
        listanotas=classnota.ver()
        titulos=[titulos[2] for titulos in listanotas ]

        print("Estos son tus titulos : {} ".format(titulos))

        select_nota=input("escribe el titulo de la nota que deseas ver")

        nota = [nota[3] for nota in listanotas if nota[2]==select_nota]
        print(nota)

    def delete (self, user_id):
        borrar=input("Selecciona el Titulo de la nota que deseas borrar")
        classnota=modelo.Nota(user_id ,borrar," ")
        borrado=classnota.borrar()
        print(borrado,"\n1 , 2 y PAW se a borrado la nota{}".format(borrar))


"""
    def seenota (self,select_nota):
        print("--------- titulo elegido ====={}".format(select_nota))
        classnota=modelo.Nota(" ",select_nota," ")
        print("--------clase creada -----------")
        nota=classnota.vernota()
        print("--------ejecutado ver nota ")
        print(nota[3])
"""
