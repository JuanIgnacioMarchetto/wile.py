#variables
accesoConcecido = False
usuario_guardado = "marcossosa"
pass_guardada = "password"


def verificar_credenciales(user,password):
    if(user == usuario_guardado) and (password == pass_guardada):
        return True
    else:
        return False
while (accesoConcecido == False):
        usuario_nuevo = input("Ingresa el usuario: ")
        password_nuevo = input("ingresa el password: ")
        
        if(verificar_credenciales(usuario_nuevo,password_nuevo) == True):
            print("BIENVENIDO")
            accesoConcecido = True
        else:
            print("ACCESO DENEGADO")