#Menu principal de SMARTHOME proyecto final abp
from proyecto_final_abp import gestor_dispositivos
from registrarse import registrar_usuario
from inicio_sesion import inicio_sesion
from automatizaciones import automatizar
from domicilios import domicilios
import string
from admin import admin
def menu_principal():
    sesiones = []
    dispositivos = []
    lugares = []
    while True:
        print("                                            " , "SMARTHOME®" , "                                                 ""\n Cargando...")
        print("Hola seleccione una opcion: " , "1. Registrarse" , "2 Iniciar sesion" , sep = "\n")
        try:
            opcion = int(input("\nIngrese un numero del 1 - 3: "))
            if opcion == 1:
                sesiones = registrar_usuario(sesiones)
                
            if opcion == 2:
                if not sesiones:
                    print("NO hay sesiones registradas por favor registrate antes.")
                    continue
                usuario_actual = inicio_sesion(sesiones)
                
                if usuario_actual:
                    print(f"\nFelicidades, iniciaste sesion como: {usuario_actual["usuario"]}")
                    break
                
            elif opcion == 3:
                print("\nSaliendo....")
                print("Mucha suerte!")
                return
                
            else:
                print("Opcion invalida!")
                
        except ValueError:
            print("\nIngrese un numero por favor")
        
    while True:
        print("\n-----------Menu principal-----------")
        print("\nSeleccione una opcion:", 
              "1. Gestor de domicilios" ,
              "2. Gestor de dispositivos" ,
              "3.Automatizaciones" , 
              "4. Modo admin" ,
              "5. Salir" , sep = "\n")
        try:    
            seleccion = int(input("Ingrese un numero entre el 1 y 3: "))
            if seleccion == 1:#permite gestionar los domicilios
                lugares = domicilios()
            
            elif seleccion == 2: #toma dispositivos y lo modifica, saliendo con la informacion necesaria de la funcion
                if not lugares:
                    print("Registra tus domicilios primero por favor!")
                else:
                    dispositivos = gestor_dispositivos(dispositivos , lugares)
            
            elif seleccion == 3: #automatizar ya toma la lista de dispositivos anterior y sale modificada 
                automatizar(dispositivos)
            elif seleccion == 4:
                admin(sesiones , usuario_actual)
            
            elif seleccion == 5:
                print("\nMucha Suerte!")
                break
            
            else:
                print("\nProximamnete mas...")
                
        except ValueError:
            print("Seleccione un numero (1-3)")
    
menu_principal()