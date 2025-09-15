class Domicilio:
    def __init__(self,nombre,direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__habitaciones = []
        
    @property
    def nombre_del_hogar(self):
        return self.__nombre
    
    @nombre_del_hogar.setter
    def nombre_del_hogar(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self,nueva_direcion):
        self.__direccion = nueva_direcion
        
    @property
    def habitaciones(self):
        return self.__habitaciones
    
    @habitaciones.setter
    def habitaciones(self, nueva_habitacion):
        pass
    

        
    def agregar_domicilio(self,nuevo_domicilio):
        pass
    
    def quitar_domicilio(self,domicilio_a_quitar):
        pass
    
    def listar_domicilio(self,domicilio_a_buscar):
        pass
    