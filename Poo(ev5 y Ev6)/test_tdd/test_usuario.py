import pytest
from dominio.usuario import Usuario

def test_usuario_getters_setters():
    usuario = Usuario("Juan", "Perez", "juan@gmail.com", "juan123", "1234", "user")
    
    assert usuario.nombre == "Juan"
    assert usuario.apellido == "Perez"
    assert usuario.email == "juan@gmail.com"
    assert usuario.nombre_usuario == "juan123"
    assert usuario.contrasena == "1234"
    assert usuario.rol == "user"
    
    usuario.nombre = "Carlos"
    usuario.apellido = "Lopez"
    usuario.email = "carlos@gmail.com"
    usuario.nombre_usuario = "carlos123"
    usuario.contrasena = "abcd"
    usuario.rol = "admin"
    
    
    assert usuario.nombre == "Carlos"
    assert usuario.apellido == "Lopez"
    assert usuario.email == "carlos@gmail.com"
    assert usuario.nombre_usuario == "carlos123"
    assert usuario.contrasena == "abcd"
    assert usuario.rol == "admin"