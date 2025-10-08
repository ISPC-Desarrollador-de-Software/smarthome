import mysql.connector
from dominio.usuario import Usuario
from dao.usuario_dao import Usuario_dao

class Usuario_Sv():
    
  def registro(self,dni:str ,nombre : str ,apellido:str ,nombre_usuario:str , contrasenia : str ,rol :str, db):
    pdao = Usuario_dao(db)
    nueva_usuario = Usuario(dni,nombre,apellido,nombre_usuario,contrasenia,rol)
       
 
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
    
    
       
     
        
        
        

       
        
        
        