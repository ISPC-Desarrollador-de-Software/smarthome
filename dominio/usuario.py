class Usuario:
    
    def __init__(self ,nombre : str ,apellido :str , email :str ,nombre_usuario :str ,contrasena :str ,rol :str ):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__nombre_usuario = nombre_usuario
        self.__contrasena = contrasena
        self.__rol = rol 
       
   
    
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
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,valor):
        self.__email = valor
    
    @property
    def nombre_usuario(self):
        return self.__nombre_usuario
    
    @nombre_usuario.setter
    def nombre_usuario(self,valor):
        self.__nombre_usuario = valor
        
    @property
    def contrasena(self):
        return self.__contrasena
    
    @contrasena.setter
    def contrasena(self,valor):
        self.__contrasena = valor
        

    @property
    def rol (self):
        return self.__rol
    
    @rol.setter
    def rol(self,valor):
        self.__rol = valor
        
    def __str__(self):
        return f"  nombre: {self.__nombre}, apellido: {self.__apellido},email: {self.email}, usuario {self.__nombre_usuario},contrasena{self.__contrasena}, rol: {self.__rol}" 