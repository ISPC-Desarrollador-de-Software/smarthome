
import mysql.connector
from dao.db_conn import DBConn
from dao.usuario_dao import Usuario_dao
from dominio.usuario import Usuario
from servicio.Usuario import Usuario_Sv
from dominio.dispositivo import Dispositivo
from servicio.dispositivos import ServicioDispositivos


if __name__ == "__main__":
   
    db = DBConn(config_file="../config.ini")
    dao = Usuario_dao(db)

     
    svc = ServicioDispositivos(db) #Permite manejar el menu de dispositivos


    while True:
        print("\n::::::::::::")
        print("::::MENU::::")
        print("::::::::::::")
    
        print("Opcion 1 : Registro ")
        print("Opcion 2 : Iniciar Sesion")
    
        opcion = input("Ingrese una opcion: ")

        
        if not opcion.isdigit():
            print("error ingrese un valor numerico valido")
            continue
        else :
            opcion_entero = int(opcion)
        
        match opcion_entero:
            case 1:
                while True: 
                    print("\n::::::::::::::::")
                    print("::::Registro::::")
                    print("::::::::::::::::") 

                    us =Usuario_Sv()
                    #dni = input("Ingrese su DNI: ")
                    nombre = input("Ingrese su nombre: ")
                    apellido = input("Ingrese su apellido: ")
                    email = input("Ingrese su email: ")
                    nombre_usuario = input("Ingrese el usuario: ")
                    contrasena = input("Ingrese la contrasenia: ")
                    
                    print("Opciones para ROL")
                    print("Digite 1 para admnistrador ")
                    print("Digite 2 para usuario estandar")
                    rol = input("Ingrese el rol: ")
                    
                    if not rol.isdigit():
                        print("Ingrese un valor numerico valido ")
                        continue
                        
                    else : 
                        rol_opcion = int(rol)

                
                
                    us.registro(nombre,apellido,email,nombre_usuario,contrasena,rol_opcion,db)
                    pregunta = input("¿Quiere registrar otro usuario? SI o NO: ").lower().strip
                    
                    if pregunta != "no":
                        break
           

            case 2: 
                print("\n:::::::::::::::::::::::")
                print("::::Iniciar Sesion ::::")
                print(":::::::::::::::::::::::") 
                us =Usuario_Sv()
                usuario = input("Ingrese su usuario: ")
                contrasenia = input ("Ingrese su contrasenia: ")
                usuario_guardado = usuario
                rol= us.iniciar_sesion(usuario, contrasenia, db)
                
                if rol == 1:
                    while True :
                        print("\n:::::::::::::::::::::::::::::")
                        print(":::Bienvenido Administrador::")
                        print(":::::::::::::::::::::::::::::")
                        print("\nopcion 1: Cambiar de rol de un usuario")
                        print("opcion 2: Crear Dispostivo")
                        print("Opcion 3: Actualizar estado del Dispositivo")
                        print("Opcion 4: Listar Dispositivos")
                        print("Opcion 5: Eliminar Dispositivo")
                        print("Opcion 6: volver al menu anterior")
                        
                        opcion = input("Ingrese una opcion: ")
                        
                        if not opcion.isdigit():
                            print("Error : Ingrese valores numerico valido")
                            continue
                        else:
                            opcion_administrador = int(opcion)
                        match(opcion_administrador):
                            case 1 : 
                                usuario = input("Ingrese el usuario a cambiar rol: ")
                                rol =input("Ingrese el nuevo rol: ")
                                
                                us.cambiar_rol(rol,usuario,db)
                            
                            case 2:
                                
                                try:
                                    print("\n:::::::::::::::::::::::")
                                    print(":::: Crear dispositivo ::::")
                                    print("\n:::::::::::::::::::::::")
                                
                                    nombre = input("Ingrese el nombre del dispositivo: ")
                                    tipo = input("Ingrese el tipo: ")
                                    estado = input("Ingrese el estado (encendido/apagado): ")
                                    id_ubicacion = int(input("Ingrese el ID de la ubicación: "))
                                
                                    if id_ubicacion <= 0:
                                        print("ID ubicacion debe ser positivo")
                                        continue
                                
                                    nuevo_id = svc.alta(nombre, tipo, estado, id_ubicacion)
                                except ValueError as error:
                                    print(f"Error al agregar: {error}")
                                   

                            
                            case 3 : 
                                    id_dispositivo = None
                                    while id_dispositivo is None:
                                        try:
                                            id_input = input("Ingrese el ID del dispositivo que desea actualizar su estado: ").strip() 
                                            id_dispositivo = int(id_input)
                                            
                                            if id_dispositivo <= 0:
                                                print("El ID debe ser un numero positivo")
                                                id_dispositivo = None
                                        except ValueError:
                                            print("El ID debe ser un numero entero")
                                    
                                    print("Ingrese el estado. Estado posible: encendido o apagado")
                                    nuevo_estado = input("Ingrese el nuevo estado: ").strip().lower()
                                    
                                    if not nuevo_estado:
                                        print("El estado no puede estar vacio")
                                        continue
                                    
                                    actualizacion_exitosa = svc.cambiar_estado_del_dispostivo(id_dispositivo, nuevo_estado)
                                    
                                    if actualizacion_exitosa:
                                        print("El estado pudo ser cambiado con exito")
                                    else:
                                        print("El dispositivo no pudo ser actualizado con exito")

                            
                            case 4 :
                                try:
                                    dispositivos = svc.listar()
                                except Exception as error:
                                    print(f"Error al listar: {error}")
                            
                            case 5: 
                                try:
                                    id_dispositivo = None
                                    while id_dispositivo is None:
                                        try:
                                            id_input = input("ID dispositivo a eliminar: ").strip()
                                            id_dispositivo = int(id_input)
                                            
                                            if id_dispositivo <= 0:
                                                print("ID dispositivo debe ser un numero positivo.")
                                                id_dispositivo = None
                                        except ValueError:
                                            print("ID dispositivo debe ser un numero entero valido.")
                                    
                                    eliminacion_exitosa = svc.eliminar(id_dispositivo)
                                    if eliminacion_exitosa:
                                        print("Eliminado con exito")
                                    else:
                                        print("No se encontro el dispositivo")
                                except ValueError as err:
                                    print(f"Error al eliminar: {err}")
                                except Exception as err:
                                    print(f"Error inesperado al eliminar: {err}")
                                    
                                    
                            case 6:
                                print("Saliendo...")
                                break
                                                       
                            case 6 :
                                break
                            case __:
                                print("Error : Ingreso una opcion incorrecta")
                            
                            
                
                elif  rol ==2  : 
                    
                    while True: 
                        print("\n:::::::::::::::::::")
                        print(":::Panel usuario:::")
                        print(":::::::::::::::::::")
                        
                        print("Opcion 1 : Consultar datos personales.")
                        print("Opcion 2 : Consultar Dispostivos.")
                        print("Opcion 3 : Salir.")

                        opcion= input("Ingrese una opcion: ")
                        
                        if not opcion.isdigit():
                            print("Error Ingrese un valor numerico valido")
                            continue
                        else : 
                            opcion_estandar = int(opcion)
                        
                        match(opcion_estandar):
                            
                            case 1:
                                
                                us.consultar_datos(usuario_guardado,db)
                                
                                
                            case 2:
                                    print("\nListando dispositivos disponibles:")
                                    dispositivos = svc.listar()
                            
                            
                            case 3:
                                print("Saliendo...")
                                break
                               
                            case __:
                                print("Error: Ingrese una opción válida")
                                    
                            
                

