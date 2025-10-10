# App Matematica/main.py
import mysql.connector
from dao.db_conn import DBConn
from dao.usuario_dao import Usuario_dao
from dominio.usuario import Usuario
from servicio.Usuario import Usuario_Sv

if __name__ == "__main__":
    # OJO: tu DBConn busca el INI relativo a /dao, por eso uso ../config.ini
    db = DBConn(config_file="../config.ini")
    dao = Usuario_dao(db)


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
                rol = input("Ingrese el rol: ")
                us.registro(nombre,apellido,email,nombre_usuario,contrasena,rol,db)
                
           

            case 2: 
                print("\n:::::::::::::::::::::::")
                print("::::Iniciar Sesion ::::")
                print(":::::::::::::::::::::::") 
                us =Usuario_Sv()
                usuario = input("Ingrese su usuario: ")
                contrasenia = input ("Ingrese su contrasenia: ")
                rol = input("Ingrese su rol: ")
                if us.iniciar_sesion(usuario,contrasenia,rol,db) == True and rol :
                    print("Se Conecto con exito")
                else :
                    print("Error Ingrese un usuario valido")
                    
            
                
                
                

