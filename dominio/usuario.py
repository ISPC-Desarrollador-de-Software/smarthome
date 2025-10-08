class Usuario:
    
    def __init__(self ,dni,nombre : str ,apellido :str ,nombre_usuario :str ,contrasenia :str ,rol :str ):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nombre_usuario = nombre_usuario
        self.__contrasenia = contrasenia
        self.__rol = rol 
       
   
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,valor):
        self.__dni = valor

        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
    
    @property
    def apellido (self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,valor):
        self.__apellido =valor
        
    @property
    def nombre_usuario(self):
        return self.__nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self,valor):
        self.__nombre_usuario = valor
        
    @property
    def contrasenia(self):
        return self.__contrasenia
    
    @contrasenia.setter
    def contrasenia(self,valor):
        self.__contrasenia = valor
        

    @property
    def rol (self):
        return self.__rol
    
    @rol.setter
    def rol(self,valor):
        self.__rol = valor
        
    def __str__(self):
        return f" DNI: {self.__dni}, nombre: {self.__nombre}, apellido: {self.__apellido},usuario {self.__nombre_usuario},contrasenia{self.__contrasenia}, rol: {self.__rol}" 