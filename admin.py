#Modulo admin
def admin(sesiones , usuario_encontrado):
    
    if usuario_encontrado["rol"] != "admin":
        print("Esta seccion es solo para los usuarios con el rango de admin!")
        return
    while True:
        print('\nHola, bienvenido a la seccion de admin, aca podras gestionar a los usuarios y eliminar usuarios.')
        print('\n1.Listar usuarios.', '2. Gestionar usuarios' , '3.Salir' , sep = "\n")
    
        try:
            seleccion_admin = int(input('Ingrese un numero (1-3): '))
            if seleccion_admin == 1:
                for usuarios in sesiones:
                    print(f'nombre y apellido: {usuarios["nombre"] , usuarios["apellido"]} email: { usuarios["email"]} usuario: { usuarios["usuario"]} contraseña: {usuarios["contraseña"]}')

            elif seleccion_admin == 2:
                eliminar_usuario = input("ingrese el nombre de usuario que desea eliminar de la base de datos: ").strip().lower()
                for usu in sesiones:
                    if usu["usuario"] == eliminar_usuario:
                        if usu["rol"] == "admin":
                            print('\nNo se puede elminar a un admin!')
                        else:
                            sesiones.remove(usu)
                            print(f"usuario {eliminar_usuario} eliminado con exito!")
                        break
                else:
                    print('Usuario no coincide con los usuarios registrados en la base de datos!')
            
            elif seleccion_admin == 3:
                print("Muchas Gracias!")
                break
            else:
                print("\nopcion no encontrada!")
                    
        except ValueError:
            print("Ingrese un valor numerico por favor")