from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def agregar_dispositivo(self,int):
        pass
    
    @abstractmethod
    def eliminar_dispositivo(self,int):
        pass
    
    @abstractmethod
    def listar_dispositivos(self,id):
        pass
    
    @abstractmethod
    def cambiar_estado_del_dispostivo(self):
        pass
    
    @abstractmethod
    def cambiar_ubicacion(self):
        pass
    
    