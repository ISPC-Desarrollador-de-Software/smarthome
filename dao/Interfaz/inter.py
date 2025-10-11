from abc import ABC , abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def mostrar_datos(self,nombre : str):
        pass
    @abstractmethod
    def create(self,object):
        pass
    
    @abstractmethod
    def update_rol(self,object):
        pass
    
    @abstractmethod
    def delete(self,object):
        pass
    
    
    