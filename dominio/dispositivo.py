class Dispositivo:
    
    def __init__(self,id_dispositivo,nombre, tipo,estado,ubicacion,id_ubicacion):
        self.__id = id_dispositivo
        self.__id_ubicacion = id_ubicacion
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
    
    @property
    def id_ubicacion(self):
        return self.__id_ubicacion
    
    @id_ubicacion.setter
    def id_ubicacion(self,valor):
        self.__id_ubicacion = valor
        
    @property
    def id_dispositivo(self):
        return self.__id
    
    @id_dispositivo.setter
    def id_dispositivo(self,valor):
        self.__id = valor
        