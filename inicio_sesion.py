#Modulo de inicio de sesion
def inicio_sesion(sesiones):
    verificar_usuario = True
    verificacion = True
    if sesiones:
        print("\nBienvenido a SMARTHOME, tus dispositivos estan bien administrados!")
                    
        while verificar_usuario: #verificacion del usuario
            sesion = input("Ingrese su nombre de usuario: ").strip().lower()
            usuario_encontrado = None # evitar malas verificaciones
            for usu in sesiones:
                if usu["usuario"] == sesion:
                    print(f"\nbienvenido/a {sesion} nos alegra tenerte de vuelta")
                                
                    verificar_usuario = False
                    usuario_encontrado = usu
            if usuario_encontrado == None:
                print("\nNombre de usuario no encontrado!" ,
                        "Intenta ponerlo exactamente igual como te registraste", sep = "\n")
                            

        while verificacion: #verificacion de la contraseña con variable creada en el for qe busca el usuario
            sesion_contra = input("Ingrese su contraseña: ").strip()
            if usuario_encontrado["contraseña"] == sesion_contra:
                print("\nSESION INICIADA CON EXITO!",
                  "Cargando...." , sep = "\n")
                            
                verificacion = False
            else:
                print("\nLa contraseña no es correcta!")
                continue
                                   
    else:
        print("\nNo estas registrado!")        
    return usuario_encontrado