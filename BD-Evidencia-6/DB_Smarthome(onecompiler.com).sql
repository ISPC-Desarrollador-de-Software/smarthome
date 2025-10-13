create database SmartHome;
use SmartHome;

create table usuario(
id_usuario int auto_increment primary key,
nombre varchar(60) not null,
apellido varchar(100) not null,
email varchar(255) not null,
nombre_usuario varchar(10) not null ,
contrasena varchar(255) not null,
rol varchar(20)not null);

create table domicilio(
id_domicilio int auto_increment primary key,
nombre_domicilio varchar(255) not null,
direccion varchar(255) not null,
id_usuario int ,
foreign key (id_usuario) references usuario(id_usuario));

create table ubicacion(
id_ubicacion int auto_increment primary key,
nombre varchar(100) not null,
id_domicilio int ,
foreign key(id_domicilio) references domicilio(id_domicilio));

create table dispositivo(
id_dispositivo int auto_increment primary key,
nombre_dispositivo varchar(100) not null,
tipo varchar(100) not null,
estado varchar(100) not null,
id_ubicacion int, 
foreign key (id_ubicacion) references ubicacion(id_ubicacion));


create table automatizaciones(
id_automatizacion int primary key auto_increment,
nombre_automatizacion varchar(255) not null,
descripcion_automatizacion text,
id_usuario int,
foreign key (id_usuario) references usuario(id_usuario));

create table accion_automatizacion(
id_accion int auto_increment primary key,
estado_deseado varchar(100) not null,
id_automatizacion int ,
id_dispositivo int,
foreign key (id_automatizacion) references automatizaciones(id_automatizacion),
foreign key (id_dispositivo) references dispositivo(id_dispositivo));

-- USUARIO (10)
INSERT INTO usuario (nombre, apellido, email, nombre_usuario, contrasena, rol) VALUES
('Ana','García','ana@gmail.com','ana','123456','administrador'),
('Luis','Flores','luis@gmail.com','luis','123456','estandar'),
('María','Pérez','maria@gmail.com','maria','123456','estandar'),
('Carlos','López','carlos@gmail.com','carlos','123456','estandar'),
('Sofía','Martínez','sofia@gmail.com','sofia','123456','administrador'),
('Julián','Ramos','julian@gmail.com','julian','123456','estandar'),
('Agustina','Vega','agustina@gmail.com','agus','123456','estandar'),
('Mateo','Suárez','mateo@gmail.com','mateo','123456','estandar'),
('Carla','Quiroga','carla@gmail.com','carla','123456','estandar'),
('Flor','Romero','flor@gmail.com','flor','123456','administrador');



-- DOMICILIO (10)
INSERT INTO domicilio (nombre_domicilio, direccion, id_usuario) VALUES
('Casa Ana','Mitre 123, Córdoba', 1),
('Depto Luis','Belgrano 456, Córdoba', 2),
('Casa María','San Martín 789, Córdoba', 3),
('Casa Carlos','Rivadavia 101, Córdoba', 4),
('Casa Sofía','Sarmiento 202, Córdoba', 5),
('Casa Julián','Brown 303, Córdoba', 6),
('Casa Agustina','Ituzaingó 404, Córdoba', 7),
('Casa Mateo','Colón 505, Córdoba', 8),
('Casa Carla','9 de Julio 606, Córdoba', 9),
('Casa Flor','Vélez Sarsfield 707, Córdoba', 10);

-- UBICACION (10)
INSERT INTO ubicacion (nombre, id_domicilio) VALUES
('Living', 1),
('Cocina', 1),
('Dormitorio', 2),
('Patio', 2),
('Comedor', 3),
('Garaje', 4),
('Lavadero', 5),
('Oficina', 6),
('Balcón', 7),
('Terraza', 8),
('cocina',9),
('garage',10);

-- DISPOSITIVO (10)
INSERT INTO dispositivo (nombre_dispositivo, tipo, estado, id_ubicacion) VALUES
('Luz principal', 'iliminacion', 'apagado', 1),
('Cámara IP', 'seguridad', 'encendido', 1),
('Aire Split', 'Aire', 'apagado', 2),
('Tv', 'Electrodomestico', 'apagado', 3),
('Sensor Puerta', 'Sensor', 'encendido', 4),
('Luz Patio', 'iliminacion', 'encendido', 4),
('Luz Garaje', 'iliminacion', 'apagado', 6),
('Cámara Garaje', 'seguridad', 'encendido', 6),
('Camara patio', 'seguridad', 'encendido', 8),
('Luz Terraza', 'iliminacion', 'apagado', 10);


INSERT INTO automatizaciones (nombre_automatizacion, descripcion_automatizacion, id_usuario) VALUES
('Modo Noche','Apaga luces interiores y enciende sensor de seguridad',1),
('Llegada a Casa','Enciende luz living y enchufe TV',2),
('Ahorro Energía','Apaga aires y enchufes no críticos',3),
('Seguridad Garaje','Enciende cámara y luz garaje al detectar movimiento',4),
('Patio Seguro','Enciende luz patio por la noche',5),
('Trabajo Oficina','Enciende enchufe PC y luz oficina',6),
('Fin de Jornada','Apaga todo salvo cámaras',7),
('Terraza Noche','Enciende luz terraza al anochecer',8),
('Cocina Mañana','Enciende luz cocina 07:00',1),
('Descanso','Apaga luces y aires de dormitorios',2);

-- ACCION_AUTOMATIZACION (10)
INSERT INTO accion_automatizacion (estado_deseado, id_automatizacion, id_dispositivo) VALUES
('apagado', 1, 1),   -- Modo Noche: apaga luz living
('encendido', 1, 5), -- Modo Noche: asegura sensor
('encendido', 2, 1), -- Llegada: enciende luz living
('encendido', 2, 4), -- Llegada: enciende enchufe TV
('apagado', 3, 3),   -- Ahorro: apaga Aire
('apagado', 3, 9),   -- Ahorro: apaga Enchufe PC
('encendido', 4, 8), -- Seguridad Garaje: cámara on
('encendido', 4, 7), -- Seguridad Garaje: luz garaje on
('encendido', 5, 6), -- Patio Seguro: luz patio on
('encendido', 8,10); -- Terraza Noche: luz terraza on



