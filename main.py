import usuarios.acciones
import notas.acciones

do=usuarios.acciones.Acciones()
do_A_C=notas.acciones.AccionesNota()

print("""

        Bienvenido a tu deposito de Notas madafaka.

        -Login
        -Register
        -salir
"""        )

accion=input("Tipea lo que deseas hacer : ").lower().strip()

if accion=="login":
    do.login()


elif accion=="register":

    reg_user=do.register()
    accion=do_A_C.menu()

    if accion=="crear":
        do_A_C.create(reg_user[0])
        accion=do_A_C.menu()

    if accion=="ver":
        select_nota=do_A_C.see(reg_user[0])

        accion=do_A_C.menu()

    if accion=="borrar":
        do_A_C.delete(reg_user[0])
        accion=do_A_C.menu()

    if accion=="salir":
        exit()


elif accion=="salir":
    exit()
