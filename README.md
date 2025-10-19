# SmartHome – Programa de Consola (Python + MySQL)

## Propósito
Gestionar funciones básicas de **SmartHome** desde consola:
- **Registro** de usuario estándar e **inicio de sesión**.
- Menú **usuario estándar**: ver **datos personales** y **dispositivos**.
- Menú **admin**: **CRUD de dispositivos** y **cambio de rol** de usuarios.

## Contexto
Entrega de Programación I (Ev. 6). El programa `main.py` se conecta a **MySQL** usando clases **DAO**.

## Alcance
**Incluye:** `main.py` con login/menús, DAOs para usuario y dispositivo, consultas y CRUD.  
**No incluye:** interfaz gráfica, API, automatizaciones avanzadas .

## Requisitos
- Python 3.10+
- Paquete: `mysql-connector-python` 
- **MySQL 8+** con BD `SmartHome` ya creada (tablas y datos cargados).

## Configuración rápida

- Documento Config.ini 
[database]
host = localhost
port = 3306  --> Puerto 
user = root --> usuario de MYSQL
password = root  --> Contrasenia
database = SmartHome  --> nombre de base de datos 

## Ejecución 

- Archivo " main.py"
- Iniciar sesión o registrarse.
- Si sos estándar: consultar datos personales y dispositivos.
- Si sos admin: CRUD de dispositivos y cambiar rol.

## autores 
- Lautaro Villafañe — DNI 41037495
- Luis David Flores — DNI 37730625