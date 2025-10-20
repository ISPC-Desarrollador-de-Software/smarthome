import logging
from dominio.dispositivo import Dispositivo
from dao.dispositivo_dao import DispositivoDAO
from dao.db_conn import DBConn


class ServicioDispositivos:
    def __init__(self, db: DBConn):
        self.db = db
        self.dao = DispositivoDAO(db)
        self.logger = logging.getLogger(__name__)
        
    def alta(self, nombre: str, tipo: str, estado_str: str, id_ubicacion: int) -> int:
        
        nombre = nombre.strip()
        tipo = tipo.strip()
        estado = estado_str.strip().lower()
        
        if not nombre or not tipo:
            raise ValueError("Nombre y tipo no pueden estar vacios.")
        

        if estado not in ("encendido", "apagado"):
            raise ValueError("Estado inválido: usa 'encendido' o 'apagado'.")
        
        if id_ubicacion <= 0:
            raise ValueError("ID ubicacion debe ser un numero positivo.")


        disp = Dispositivo(
            id_dispositivo=None,
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            ubicacion=None,     
            id_ubicacion=id_ubicacion
        )
        
        try: 
            nuevo_id = self.dao.agregar_dispositivo(disp)
            disp.id = nuevo_id
            self.logger.info(f"Dispositivo agregado con ID {nuevo_id}")
            return nuevo_id
        
        except Exception as e:
            self.logger.error(f"Error básico al agregar dispositivo: {e}")
            
            raise ValueError("No se pudo agregar el dispositivo. Verifica que la ubicación exista y los datos sean correctos.")
            
    
    
    def eliminar(self, id_dispositivo: int) -> bool:
        
          return self.dao.eliminar_dispositivo(id_dispositivo)

    
    def listar(self):
        
        return self.dao.listar_dispositivos()
    
    def cambiar_estado_del_dispostivo(self, id_dispositivo: int, nuevo_estado: str) -> bool:
        
            if nuevo_estado not in ["encendido", "apagado"]:
                print ("Error el estado debe ser encendido o apagado.")
                return False
            
            return self.dao.cambiar_estado_del_dispostivo(id_dispositivo, nuevo_estado)
        
        