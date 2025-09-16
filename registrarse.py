#Modulo de inicio de sesion
def registrar_usuario(sesiones):
    import string
    verificacion = True
    verificar_usuario = True
  
    while verificacion: # bucle del menu de seleccion entre registrar e iniciar sesion
            
            
            while True: # registro del nombre
                    nombre = input("\nIngrese su nombre: ").strip().lower()
                    if len(nombre.split()) > 1:
                        print("El nombre no debe contener espacios y debe ser solo tu primer nombre")
                            
                    elif nombre.isalpha():
                        break
                    else:
                        print("\nError, no se permiten espacios ni numeros, tampoco ningun tipo de puntuacion")
                            
                
            while True: #registro del apellido
                apellido = input("\nIngrese su apellido: ").strip().lower()
                if len(apellido.split()) > 1:
                    print("\nDebe ser tu primer apellido y no debe contener espacios!")
                        
                elif apellido.isalpha():
                    break
                else:
                    print("No debe contener caracteres especiales, numeros ni espacios!")
                
            while True: #registro del email
                email = input("\nIngrese su email :").strip().lower()
                if len(email.split()) > 1:
                    print("No debe contener espacios!")
                        
                elif "@" in email and email.endswith((".com", ".ar", ".mx", ".cl" , ".us" , ".es" , ".org" , ".net")):
                    break
                else:
                    print("\nError el correo debe estar correctamente escrito y no debe contener espacios")
                
            while True: #reglas del registro del usuario
                regla = ["\nIngrese el nombre de usuario que desee tener." , 
                                    "Recuerde seguir las siguientes reglas:" ,
                                    "- No debe tener espacios" ,
                                    "- No debe contener caracteres especiales" , 
                                    "- Debe tener al menos 6 caracteres el cual dos de ellos como minimo deben ser numeros"]
                for reglas in regla:
                    print (reglas)
                        
                    
                while True: #registro del usuario
                    usuario = input("\nIngrese su nombre de usuario: ").strip().lower()
                    if len(usuario.split()) > 1 or len(usuario) < 6 or any(caracter in string.punctuation for caracter in usuario):
                        print ("\nError, no debe contener espacios ni caracteres especiales y debe tener minimo 6 caracteres")
                            
                    elif len([num for num in usuario if num.isdigit()]) < 2:
                        print("\nEl usuario debe contener dos numero como minimo!")
                            
                    else:
                        break
                break
            validar_contra = True
                
            while validar_contra: #reglas de la contraseña
                regla_contra = ["\nIngrese la contraseña que desee." , 
                                    "Recuerde seguir las reglas para crear su contraseña:" , 
                                    "- No debe tener espacios" ,
                                    "- No debe contener caracteres especiales" , 
                                    "- Debe tener al menos 6 caracteres los cuales dos mayusculas como minimo y dos numeros"]
                for reglas_contra in regla_contra:
                    print(reglas_contra)
                        
                    
                while True:#registro de la contraseña
                    contra = input("\nIngrese la contraseña: ").strip()
                    if len(contra.split()) > 1 or len([num for num in contra if num.isdigit()]) < 2 or len([mayus for mayus in contra if mayus.isupper()]) < 2 or any(caracteres in string.punctuation for caracteres in contra) or len(contra) < 6:
                        print("Error no se cumplen las reglas de la contraseña")
                            
                    else:
                        print("\nBien, estas a un paso de registrarte")
                            
                        contra2 = input("Repita su contraseña: ").strip()
                        if contra2 == contra:
                            break
                        else:
                            print("\nERROR vuelve a ingresar tu contraseña")
                break
                
            print("\nFELICIDADES YA TE REGISTRASTE EN SMARTHOME!")
            rol = "admin" if len(sesiones) == 0 else "usuario"
            sesiones.append({"nombre" : nombre ,
                             "apellido" : apellido ,
                             "email" : email , 
                             "usuario" : usuario , 
                             "contraseña" : contra ,
                             "rol" : rol})
            validar_contra = False
            break
    return sesiones