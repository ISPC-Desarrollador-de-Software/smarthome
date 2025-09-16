#Modulo de ubicacion de los dispositivos
import string
def domicilios():
    lugares = []
    ubicaciones_casa = []
    registro_casa = True
    
    while True:
        print("\nIngrese su domicilio/s:" ,
          "1.agregar un domicilio." ,
          "2.quitar un domicilio." ,
          "3.listar domicilios" ,
          "4. Salir", sep = "\n")
        try:
            opcion_domicilio = int(input("\nIngrese un numero (1-4): "))
            
            #OPCION 1
            if opcion_domicilio == 1:
                while registro_casa:
                    nombre_domicilio = input("\nEl nombre por el cual desea identificar a su domicilio (solo letras): ").strip().lower()
                    if len(nombre_domicilio.split()) > 1 or any(especial in string.punctuation for especial in nombre_domicilio) or len(nombre_domicilio) < 1:
                        print("\nNo debe contener espacios ni signos especiales o de puntuacion, solo letras por favor.")
                    elif nombre_domicilio.isalpha():
                        print ("\nIngrese las ubicaciones que tiene en su hogar( para salir del menu ingrese el numero '0'): ")
                        while True:
                            ubicaciones = input("\nIngrese el lugar de su hogar: ").strip().lower()
                            if len(ubicaciones.split()) > 1 or any(especial in string.punctuation for especial in ubicaciones) or len(ubicaciones) < 1:
                                print("\nIngrese solo letras, ningun caracter especial por favor, muchas gracias!.")
                                continue
                        
                            elif ubicaciones == "0":
                                print("\nGracias por agregar tus ubicaciones!")
                                registro_casa = False
                                break
                            elif ubicaciones.isalpha():
                                ubicaciones_casa.append(ubicaciones)
                                continue

                        lugares.append({"nombre" : nombre_domicilio , 
                                                "ubicaciones_casa" : [ubicaciones_casa]})    
            
            
            if opcion_domicilio == 2:
                casa_encontrada = False
                while casa_encontrada == False:
                    casa = input("\nIngrese el nombre del domicilio que desea eliminar (ingrese 0 para salir): ").strip().lower()
                    if casa == "0":
                        print("\nsaliendo..")
                        break
                    for casa_eliminar in lugares:
                        if casa_eliminar["nombre"] == casa:
                            casa_encontrada = True
                            break
                    if casa_encontrada == False:
                        print("No se encontro la casa, vuelve a ingresarlo por favor.")
                    elif casa_encontrada == True:
                        lugares.remove(casa_eliminar)
                        print(f"\nDomicilio {casa_eliminar["nombre"]} eliminado con exito!")
                    
            if opcion_domicilio == 3:
                for domicilio in lugares:
                    print (f"\nnombre del domicilio: {domicilio["nombre"]} / lugares del domicilio: {domicilio["ubicaciones_casa"]}")
            
            elif opcion_domicilio == 4:
                print("\nMuchas gracias!" , 
                      "saliendoo..." , sep = "\n")
                break
            
    
                
        except ValueError:
            print("Solo se aceptan numeros, ingrese un numero por favor.")
    return lugares