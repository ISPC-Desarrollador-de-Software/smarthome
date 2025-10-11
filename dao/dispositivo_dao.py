import mysql.connector
import logging

from db_conn import DBConn
from Interfaz.interface_dao_dispositivo import DataAccessDAO

from dominio.dispositivo import Dispositivo
 

class DispositivoDAO(DataAccessDAO):
    def __init__(self, db: DBConn):
        self.db = db
        self.logger = logging.getLogger(__name__)
        
        
    def agregar_dispositivo(self, dispositivo: Dispositivo) -> int:
        with self.db.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                sentencia_sql = "INSERT INTO dispositivo (nombre_dispositivo, tipo, estado, id_ubicacion) VALUES (%s, %s, %s, %s)"
                cursor.execute(sentencia_sql, (dispositivo.nombre,dispositivo.tipo,dispositivo.estado,dispositivo.id_ubicacion))
                conn.commit()
                
                nuevo_id = cursor.lastrowid
                self.logger.info(f"Dispositivo insertado correctamente con ID {nuevo_id}")
                return nuevo_id
                
            except mysql.connector.Error as err:
                self.logger.error(f"Error al insertar dispositivo: {err}")
                conn.rollback()
                raise
    
    
    def eliminar_dispositivo(self,id_dispositivo: int) -> bool:
        
        with self.db.connect_to_mysql() as conn:
             try:
                 cursor = conn.cursor()
                 sentencia_sql = "DELETE FROM dispositivo where id_dispositivo=%s"
                 cursor.execute(sentencia_sql,(id_dispositivo,))
                 conn.commit()
                 
                 self.logger.info("Dispositivo eliminado satisfactoriamente")
                 
                 filas_afectadas = cursor.rowcount
                 if filas_afectadas > 0:
                     self.logger.info(f"Dispositivo {id_dispositivo} eliminado satisfactoriamente")
                     return True
                 
                 else:
                     self.logger.warning(f"No se encontro dispositivo con id {id_dispositivo}")
                     return False
                 
             except mysql.connector.Error as err:
                    self.logger.error(f"Error al eliminar dispositivo: {err}")
                    conn.rollback()
                    raise err
                 
    
    def listar_dispositivos(self) -> list[Dispositivo]:
        with self.db.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                sentencia_sql = "SELECT id_dispositivo, nombre_dispositivo, tipo, estado, id_ubicacion FROM dispositivo"
                cursor.execute(sentencia_sql)
                filas = cursor.fetchall()
            
                for f in filas:
                    print(f"Id_dispositivo: {f[0]}, Nombre: {f[1]}, tipo: {f[2]}, estado: {f[3]}, ID_ubicacion: {f[4]}")
              
                
                self.logger.info(f"Se listaron {len(filas)} dispositivos correctamente.")
                
            except mysql.connector.Error as err:
                self.logger.error(f"Error al listar dispositivos: {err}")
                raise
        
        
    
    def cambiar_estado_del_dispostivo(self):
        pass
    
    def cambiar_ubicacion(self):
        pass