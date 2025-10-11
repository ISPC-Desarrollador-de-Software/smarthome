import mysql.connector
from dominio.usuario import Usuario
from dao.usuario_dao import Usuario_dao

class Usuario_Sv():
    
  def registro(self,nombre : str ,apellido:str ,email:str, nombre_usuario:str , contrasena : str ,rol :str, db):
    pdao = Usuario_dao(db)
    nueva_usuario = Usuario(nombre,apellido,email,nombre_usuario,contrasena,rol)
       
 
    try:
      pdao.create(nueva_usuario)

    except mysql.connector.Error as e:
      print(f"Error MySQL: {e}")
    
  def iniciar_sesion(self,usuario : str , contrasenia : str ,rol ,db):
        
    pdao = Usuario_dao(db)
        
    try: 
      
      return pdao.consulta_iniciar_sesion(usuario, contrasenia, rol)
   
    except mysql.connector.Error as err:
    
      return err
    
  def cambiar_rol(self,rol,nombre_usuario,db):
    
    pdao = Usuario_dao(db)
    
    try:
      
      pdao.update_rol(rol,nombre_usuario)
      
      
    
    except mysql.connector.Error as err:
      return err
    
  def consultar_datos(self,nombre_usuario,db):
    
    pdao = Usuario_dao(db)
     
    try:
      
      usuario =  pdao.mostrar_datos(nombre_usuario)
      
      print(usuario)
    except mysql.connector.Error as err:
      return err
      
    
     
        
        
        

       
        
        
        