#clasee admin
from usuarios_poo import USUARIO
class Admin(USUARIO):
    def __init__(self, rol):
        self.__rol = 'admin' 

    def listar_usuarios(self):
        pass

    def eliminar_usuarios(self):
        pass