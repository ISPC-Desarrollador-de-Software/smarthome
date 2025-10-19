#modulo de automatizaciones en programacion orientada a objetos

class AccionAutomatizacion:
    def __init__(self, tipo_objetivo, id_objetivo, estado_deseado):
        self.__tipo_objetivo = tipo_objetivo
        self.__id_objetivo = id_objetivo
        self.__estado_deseado = estado_deseado

    def aplica_a(self, dispositivo):
        pass


class Automatizacion:
    def __init__(self, id_automatizacion, nombre, descripcion):
        self.__id = id_automatizacion
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__acciones = []

    def agregar_accion(self, accion):
        pass

    def aplicar(self, dispositivos):
        pass

