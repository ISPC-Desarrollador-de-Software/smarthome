class Dispositivos_entidad:
    
    def __init__(self,nombre, tipo,ubicacion,estado):
        self.__nombre = nombre 
        self.__tipo= tipo
        self.__ubicacion = ubicacion 
        self.__estado = estado
        
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,valor):
        self.__tipo = valor
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,valor):
        self.__estado = valor 
        
    @property
    def ubicacion(self):
       return self.__ubicacion 
    
    @ubicacion.setter
    def ubicacion(self,valor):
        self.__ubicacion = valor
    
def agregar_dispositivo():
    pass

def eliminar_dispositivo():
    pass

def mostrar_dispositivo():
    pass 

