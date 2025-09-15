#modulo de automatizaciones en programacion orientada a objetos

class AccionAutomatizacion:
    def __init__(self, tipo_objetivo, id_objetivo, estado_deseado):
        self.tipo_objetivo = tipo_objetivo
        self.id_objetivo = id_objetivo
        self.estado_deseado = estado_deseado

    def aplica_a(self, dispositivo):
        pass


class Automatizacion:
    def __init__(self, id_automatizacion, nombre, descripcion):
        self.id = id_automatizacion
        self.nombre = nombre
        self.descripcion = descripcion
        self.acciones = []

    def agregar_accion(self, accion):
        pass

    def aplicar(self, dispositivos):
        pass
