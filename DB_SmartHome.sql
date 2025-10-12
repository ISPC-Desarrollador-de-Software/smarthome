create database SmartHome;
use SmartHome;

create table usuario(
id_usuario int auto_increment primary key,
nombre varchar(60) not null,
apellido varchar(100) not null,
email varchar(255) not null,
usuario varchar(10) not null ,
contrasena varchar(255) not null,
rol varchar(20) not null);

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
estado_deseado int not null,
id_automatizacion int ,
id_dispositivo int,
foreign key (id_automatizacion) references automatizaciones(id_automatizacion),
foreign key (id_dispositivo) references dispositivo(id_dispositivo));




