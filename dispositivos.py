#Proyecto final ABP(Entrega 1)


def gestor_dispositivos (dispositivos , lugares):
    if dispositivos is None:
        dispositivos = []
    elif lugares is None:
        print("Primero registre una casa!")
        return
    
    print("Hola bienvenido a Smarthome® aca podras gestionar todos los dispositivos de tu hogar." , 
          "Esto es una version alpha, te pedimos que cualquier error lo reportes para ayudarnos a mejorar." , 
          "Desde ya muchas gracias y bienvenido!" , 
          sep = "\n")
    while True:#Elije sobre que casa  va a trabajar
        casa = input("Ingrese el nombre de la casa que desea operar (0 para salir): ").lower().strip()
        if casa == "0":
            print("\nsaliendo...")
            break
        casa_encontrada = False
        for nombre_de_casa in lugares:
            if nombre_de_casa["nombre"] == casa:
                casa_encontrada = nombre_de_casa
                print("\nCasa encontrada!")
                break
        if casa_encontrada == False:
            print("\nDomicilio no encontrado!")
        
        elif casa_encontrada:
            print(f"Se encontro correctamente el domicilio: {casa_encontrada["nombre"]}")
            break

      
    while True:
        try:
            print("","Opciones:", "1. Agregar dispositivos", 
                  "2. Listar dispositivos",
                  "3. Eliminar dispositivo",
                  "4. Cambiar estado de un dispositivo", 
                  "5. Cambiar ubicacion del dispositivo" ,
                  "6. Salir", sep="\n")
            opcion = int(input("Seleccione una opcion (1-6): "))
            
            #OPCION 1(agregar dispositivos)
            if opcion == 1: #este modulo permite agregar un dispositivo
                 nombre = input("Ingrese un nombre del dispositivo: ").strip().lower()
                 tipo = input("Ingrese el tipo de dispositivo que desea ingresar: ").strip().lower()
                 estado = input ("Ingrese el estado (apagado o encendido) de su dispositivo: ").strip().lower()
                 if estado not in ["encendido", "apagado"]:
                     estado = "encendido"
                 
                 while True:#agregar ubicacion al dispositivo
                    print(f"Seleccione e ingrese la ubicacion")
                    for ubicaciones in casa_encontrada["ubicaciones_casa"]:
                        print(f"-{ubicaciones}")
                    ubicacion = input("Ingrese la ubicacion del dispositivo: ").strip().lower()
                    ubicacion_encontrada = False
                    for ubic in casa_encontrada["ubicaciones_casa"]:
                        if ubicacion in ubic:
                            ubicacion_encontrada = True
                            break
                    if ubicacion_encontrada:
                        print("\nUbicacion correcta")
                        break
                    elif not ubicacion_encontrada:
                        print("esta ubicacion no se encunetra disponible")
                    

                 
                 agregar = {"nombre": nombre, "tipo" : tipo , "estado" : estado , "ubicacion" : ubicacion}
                 dispositivos.append(agregar)
                 print(f"\n dispositivo {nombre} agregado correctamente")
                 
            #OPCION 2(listar)
            elif opcion == 2:
                if dispositivos:
                    print("Dispositivos actuales: \n")
                    for i, dispositivo in enumerate(dispositivos,1):
                        print(f"Nombre: {dispositivo["nombre"]}" , f"Tipo: {dispositivo["tipo"]}" ,f"Estado: {dispositivo["estado"]}.", f"Ubicacion: {dispositivo["ubicacion"]}." , sep = "/") 
                        
                else:
                    print("No hay dispositivos registrados!")
                    
            #OPCION 3(eliminar)
            elif opcion == 3:
                nombre = input("Ingrese el nombre del dispositivo a eliminar: ").strip().lower()
                for dispositivo in dispositivos:
                    if dispositivo["nombre"] == nombre:
                        dispositivos.remove(dispositivo)
                        print(f"Se elimino correctamente el dispositivo {nombre}")
                        
                        break
                else:
                    print("El nombre ingresado no se encuentra en la lista de dispositivos")
                    
            #OPCION 4(estado)
            elif opcion == 4:
                nombre = input("Ingrese el nombre del dispositivo que deseecambiar su estado: ").strip().lower()
                for dispositivo in dispositivos:
                    if dispositivo["nombre"] == nombre:
                        if dispositivo["estado"] == "encendido":
                            dispositivo["estado"] = "apagado"
                        else:
                            dispositivo["estado"] = "encendido"
                        print(f"\n El dispositivo {nombre} se a cambiado su estado a {dispositivo["estado"]} ")
                        
                        break
                else:
                    print(f"\n El dispositivo {nombre} no se encuentra en la lista de dispositivos, por favor agregelo.")
                    
            #OPCION 5(ubicacion)
            elif opcion == 5:
                    dispositivo_encontrado = False
                    dispositivos_actual = None
                    ubicacion_valida = False
                    cambiar_lugar = input("Ingrese el nombre del dispositivo que desea cambiar su posicion: ").strip().lower()
                           
                    for cambio in dispositivos:
                        if cambio["nombre"] == cambiar_lugar:
                            dispositivos_actual = cambio
                            dispositivo_encontrado = True
                            break
                    if  dispositivo_encontrado == False:
                        print("Nombre del dispositivos mal colocado, vuelve a colocarlo")
                    
                    else:
                        while True:
                            ubicacion_cambio = input("Ingrese la nueva ubicacion del dispositivo: ").strip().lower()
                            for ubicaciones in casa_encontrada["ubicaciones_casa"]:
                                if ubicacion_cambio in ubicaciones:
                                    ubicacion_valida = True
                                    break
                            
                            if not ubicacion_valida:
                                print("La ubicacion no es valida!")
                            
                            elif ubicacion_valida == True:
                                dispositivos_actual["ubicacion"] = ubicacion_cambio
                                print(f"ubicacion cambiada con exito a {dispositivos_actual["ubicacion"]}")
                                break
                        

                        
            elif opcion == 6:
                print("Muchas gracias por usar nuestra app." , 
                      "Te recordamos que esta en version alpha." , 
                      "Te invitamos a reportar todos los errores que encuentres, muchas gracias!", 
                      sep = "\n")
                
                break
            
            else:
                print("Este numero no pertenece a una opcion.")
                
        except ValueError:
            print("ERROR ingrese un numero de opcion del 1 al 4.")
    return dispositivos