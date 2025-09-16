#Modulo de automatizaciones
def automatizar(dispositivos):
    print(" \n Bienvenidos a la pestaña de automatizacion" ,
          "Aca podras ver todos los tipos de automatizacion" , 
          "Mas adelante podras tener tus propios modos de automatizacion personalizados y mucho mas!",
          sep = "\n")
    
    lista_print = ["Seleccione una opcion de automatizacion por favor:" , 
                   "1. Modo Noche (luces apagadas y alarma encendida)." , 
                   "2. Mas modos proximamente" , "3. Salir del menu."]
    for i in lista_print:
        print(i)
    while True:
        try:
            opcion_automatizar =  int(input("Seleccione una opcion: "))
            modo_noche = False
            if opcion_automatizar == 1:
                for dispositivo in dispositivos:
                
                    if dispositivo["tipo"] in ["persiana" , "luces"]:
                        dispositivo["ecd coado"] = "apagado"
                        break
                    elif dispositivo["tipo"] in ["camara" , "alarma"]:
                        dispositivo["estado"] = "encendido"
                        modo_noche = True
                        break
                else:
                    print("No se encontraron dispositivos para hacer la automatizacion")
                    return
                print (dispositivo)
  
            elif opcion_automatizar == 2:
                print("Muy pronto tendras nuevos modos de automatizacion, gracias por tu paciencia.")

            elif opcion_automatizar == 3:
                print('Muchas gracias!')
                break
            
            else:
                print("Deja tus dispositivos en nuestras manos!")

        except ValueError:
            print("Por favor, solo se aceptan numeros.")
        
    