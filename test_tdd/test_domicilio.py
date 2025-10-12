import pytest
from dominio.dispositivo import Dispositivo

def test_dispositivo_getters_setters():
    disp = Dispositivo(1,"Lámpara", "Luz", "Apagado","rivera indarte 1500",2)

    assert disp.id_dispositivo == 1
    assert disp.nombre == "Lámpara"
    assert disp.tipo == "Luz"
    assert disp.ubicacion == "rivera indarte 1500"
    assert disp.estado == "Apagado"
    assert disp.id_ubicacion == 2

    disp.id_dispositivo = 2
    disp.nombre = "Ventilador"
    disp.tipo = "Clima"
    disp.ubicacion = "Corrientes 1234"
    disp.estado = "Encendido"
    disp.id_ubicacion = 3
    
    assert disp.id_dispositivo == 2
    assert disp.nombre == "Ventilador"
    assert disp.tipo == "Clima"
    assert disp.ubicacion == "Corrientes 1234"
    assert disp.estado == "Encendido"
    assert disp.id_ubicacion == 3
