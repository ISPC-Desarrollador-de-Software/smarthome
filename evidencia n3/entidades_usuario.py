class Usuario_entidad:
    
    def __init__(self,nombre,apellido,email,usuario,contraseña,rol):
        self._nombre = nombre
        self._apellido = apellido 
        self._email = email
        self._usuario = usuario 
        self.__contraseña = contraseña
        self._rol = rol
    
    @property
    def nombre(self):
       return self._nombre
    
    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,valor):
        self._apellido = valor
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,valor):
        self._email = valor 
        
    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self,valor):
        self._usuario = valor
    
    @property
    def contraseña(self):
        return self.__contraseña
     
    @contraseña.setter
    def contraseña(self,valor):
        self.__contraseña = valor
        
    @property
    def rol(self):
        return self._rol
    
    @rol.setter
    def rol(self,valor):
        self._rol = valor
