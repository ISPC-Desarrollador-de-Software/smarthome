
import mysql.connector
from dominio.usuario import Usuario
from mysql.connector import errorcode
from dao.interfaz.inter import DataAccessDAO
from dao.db_conn import DBConn


class  Usuario_dao(DataAccessDAO):
    
   
    def __init__(self,db_conn: DBConn):
            
            self.db_conn = db_conn.connect_to_mysql()
            self.db_name=db_conn.get_data_base_name()
    
    def get(self,dni : str ) -> Usuario:
    
        with self.db_conn as conn : 
            
            try: 
                cursor = conn.cursor()
                querry = f"select dni, nombre,apellido,nombre_usuario,contrasenia,rol from {self.db_name}.usuario where dni =%s"
                cursor.execute(querry,(dni,))
                
                row = cursor.fetchone()
                if row :
                    return Usuario(row[0],row[1],row[2],row[3],row[4],row[5])
                return None
            except mysql.connector.Error as err:
                raise err
             
    def create(self,usuario :Usuario):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                query = f"insert into {self.db_name}.usuario(dni, nombre,apellido,nombre_usuario,contrasenia,rol) values (%s,%s,%s,%s,%s,%s)"
                parametros = (usuario.dni,usuario.nombre,usuario.apellido,usuario.nombre_usuario,usuario.contrasenia,usuario.rol)
                cursor.execute(query,parametros)
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            
    def update(self,usuario : Usuario):
        with self.db_conn as conn :
            try:
                cursor = conn.cursor()
                query = f"update {self.db_name}.usuario set rol = %s where nombre = %s"
                
                cursor.execute(query,usuario.rol)
                conn.commit()
            except mysql.connector.Error as err:
                raise err 
    
    def delete(self,usuario : Usuario):
        with self.db_conn as conn : 
            try:
                cursor = conn.cursor()
                query = f"delete form {self.db_name}.usuario where dni = %s "
                cursor.execute(query, usuario.dni)
                conn.commit()
            except mysql.connector.Error as err:
                raise err
            
    def consulta_iniciar_sesion(self,nombre_usuario:str , contrasenia : str , rol :str )->bool :
        
        with self.db_conn as conn :
            try:
                cursor = conn.cursor()
                query = f"select nombre_usuario,contrasenia,rol from {self.db_name}.usuario where nombre_usuario = %s and contrasenia = %s and rol = %s"
                cursor.execute(query,(nombre_usuario,contrasenia,rol))
                
                encontrado = cursor.fetchone() is not None
                cursor.close()
                return encontrado
            
               
            except mysql.connector.Error as err:
                raise err
            
    
        