
import pytest
from admin import Admin
from automatizacion import AccionAutomatizacion, Automatizacion
from domicilio import Domicilio
from entidades_dispositivos import Dispositivos_entidad, agregar_dispositivo, eliminar_dispositivo, mostrar_dispositivo
from entidades_usuario import Usuario_entidad


# ---------- Usuario_entidad ----------
def test_usuario_entidad_getters_setters():
    usuario = Usuario_entidad("Juan", "Pérez", "juan@gmail.com", "juan123", "1234", "user")

    assert usuario.nombre == "Juan"
    assert usuario.apellido == "Pérez"
    assert usuario.email == "juan@gmail.com"
    assert usuario.usuario == "juan123"
    assert usuario.contraseña == "1234"
    assert usuario.rol == "user"

    usuario.nombre = "Carlos"
    usuario.apellido = "Lopez"
    usuario.email = "carlos@gmail.com"
    usuario.usuario = "carlos123"
    usuario.contraseña = "abcd"
    usuario.rol = "admin"

    assert usuario.nombre == "Carlos"
    assert usuario.apellido == "Lopez"
    assert usuario.email == "carlos@gmail.com"
    assert usuario.usuario == "carlos123"
    assert usuario.contraseña == "abcd"
    assert usuario.rol == "admin"


# Admin
def test_admin_inherits_usuario():
    admin = Admin("Ana", "Gomez", "ana@gmail.com", "ana123", "pass", "admin")
    assert isinstance(admin, Usuario_entidad)

Dispositivos_entidad
def test_dispositivo_getters_setters():
    disp = Dispositivos_entidad("Lámpara", "Luz", "25 de mayo 800", "Apagado")

    assert disp.nombre == "Lámpara"
    assert disp.tipo == "Luz"
    assert disp.ubicacion == "25 de mayo 800"
    assert disp.estado == "Apagado"

    disp.nombre = "Ventilador"
    disp.tipo = "Clima"
    disp.ubicacion = "Corrientes 1234"
    disp.estado = "Encendido"

    assert disp.nombre == "Ventilador"
    assert disp.tipo == "Clima"
    assert disp.ubicacion == "Corrientes 1234"
    assert disp.estado == "Encendido"


def test_dispositivo_funciones_stub():
    assert agregar_dispositivo() is None
    assert eliminar_dispositivo() is None
    assert mostrar_dispositivo() is None


#Domicilio
def test_domicilio_getters_setters():
    dom = Domicilio("Casa Juan", "25 de mayo 800")

    assert dom.nombre_del_hogar == "Casa Juan"
    assert dom.direccion == "25 de mayo 800"
    assert dom.habitaciones == []

    dom.nombre_del_hogar = "Casa Ana"
    dom.direccion = "Corrientes 1234"

    assert dom.nombre_del_hogar == "Casa Ana"
    assert dom.direccion == "Corrientes 1234"


def test_domicilio_metodos_stub():
    dom = Domicilio("Casa Test", "25 de mayo 800")
    assert dom.agregar_domicilio("otro") is None
    assert dom.quitar_domicilio("otro") is None
    assert dom.listar_domicilio("otro") is None


#Automatizacion
def test_accion_automatizacion_getters():
    accion = AccionAutomatizacion("Luz", 1, "Encendido")
    assert isinstance(accion, AccionAutomatizacion)


def test_automatizacion_agregar_y_aplicar_stub():
    auto = Automatizacion(1, "Encender luces", "Prende luces")
    accion = AccionAutomatizacion("Luz", 1, "Encendido")

    assert auto.agregar_accion(accion) is None
    assert auto.aplicar([]) is None
