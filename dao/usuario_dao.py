
import mysql.connector
from dominio.usuario import Usuario
from mysql.connector import errorcode
from dao.interfaz.inter import DataAccessDAO
from dao.db_conn import DBConn


class  Usuario_dao(DataAccessDAO):
    
   
    def __init__(self,db_conn: DBConn):
            
            self.db_conn = db_conn.connect_to_mysql()
            self.db_name=db_conn.get_data_base_name()
    
    def mostrar_datos(self,nombre : str ) -> Usuario:
    
        with self.db_conn as conn : 
            
            try: 
                cursor = conn.cursor()
                querry = f"select  nombre,apellido,email,nombre_usuario,contrasena,rol from {self.db_name}.usuario where nombre_usuario =%s"
                cursor.execute(querry,(nombre,))
                
                row = cursor.fetchone()
                if not row:
                    return None
                return Usuario(*row)
            except mysql.connector.Error as err:
                raise err
             
    def create(self,usuario :Usuario):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = f"insert into {self.db_name}.usuario(nombre,apellido,email,nombre_usuario,contrasena,rol) values (%s,%s,%s,%s,%s,%s)"
                parametros = (usuario.nombre,usuario.apellido,usuario.email,usuario.nombre_usuario,usuario.contrasena,usuario.rol)
                cursor.execute(query,parametros)
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            
    def update_rol(self,rol :str , nombre_usuario :str ):
        with self.db_conn as conn :
            try:
                cursor = conn.cursor()
                query = f"update {self.db_name}.usuario set rol = %s where  nombre_usuario= %s"
                
                cursor.execute(query,(rol,nombre_usuario))
                conn.commit()
            except mysql.connector.Error as err:
                raise err 
    
    def delete(self,usuario : Usuario):
        with self.db_conn as conn : 
            try:
                cursor = conn.cursor()
                query = f"delete form {self.db_name}.usuario where id = %s "
                cursor.execute(query, usuario.dni)
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            
    def consulta_iniciar_sesion(self,nombre_usuario:str , contrasena : str , rol :str )->bool :
        
        with self.db_conn as conn :
            try:
                cursor = conn.cursor()
                query = f"select nombre_usuario,contrasena,rol from {self.db_name}.usuario where nombre_usuario = %s and contrasena = %s and rol = %s"
                cursor.execute(query,(nombre_usuario,contrasena,rol))
                
                encontrado = cursor.fetchone() is not None
                cursor.close()
                return encontrado
            
               
            except mysql.connector.Error as err:
                raise err
            
    
