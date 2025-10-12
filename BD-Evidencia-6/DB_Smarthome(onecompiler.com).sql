
-- create
CREATE TABLE usuario (
  id_usuario int auto_increment PRIMARY KEY,
  nombre varchar(60) NOT NULL,
  apellido varchar(100) NOT NULL,
  email varchar(255) NOT NULL,
  usuario varchar(10) NOT NULL,
  contrasena varchar(50) NOT NULL,
  rol varchar(20) NOT NULL 
);



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
estado bool ,
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


-- insert
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('David', 'Flores','David_Flores@gmail.com','David11','123456',"administrador");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('laura', 'Diaz','laura_diaz14@gmail.com','laura2','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('sofia', 'vergara','sofia_vergara69@gmail.com','sofi99','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Luis', 'Lopez','lopez_luis_40@gmail.com','luisL23','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('daniel', 'zapata','zapata_daniel@gmail.com','daniel20','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('lucas', 'tapia','lucas_tapia58@gmail.com','lucas10','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('matias', 'tolaba','matias_tolaba@gmail.com','matute','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('lisandro', 'anzaldo','lisandro_88@gmail.com','lis88','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Miguel', 'Flores','miguel_10@gmail.com','miguelito','123456',"estandar");
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Martin', 'Flores','martin_flores969@gmail.com','tincho132','123456',"estandar");

INSERT into domicilio(nombre_domicilio,direccion,id_usuario) VALUES ('Junin','agustin garzon 88', 1);
-- casa 1
INSERT into ubicacion(nombre,id_domicilio) VALUES('cocina',1);
INSERT into ubicacion(nombre,id_domicilio) VALUES('patio',1);
INSERT into ubicacion(nombre,id_domicilio) VALUES('habitacion juan',1);
INSERT into ubicacion(nombre,id_domicilio) VALUES('cochera',1);
INSERT into ubicacion(nombre,id_domicilio) VALUES('living',1);
-- casa 2 
INSERT into domicilio(nombre_domicilio,direccion,id_usuario) VALUES ('gorriti','lisandro de la torre 380',2);
INSERT into ubicacion(nombre,id_domicilio) VALUES('cocina',2);
INSERT into ubicacion(nombre,id_domicilio) VALUES('patio',2);
INSERT into ubicacion(nombre,id_domicilio) VALUES('habitacion sofia',2);
INSERT into ubicacion(nombre,id_domicilio) VALUES('cochera',2);
INSERT into ubicacion(nombre,id_domicilio) VALUES('living',2);


INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('estufa','calefaccion',true,1);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('televisor','entretenimiento',true,1);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('computadora','entretenimiento',true,1);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('microondas','electrodomestico',true,1);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('heladera ','electrodomestico',true,1);

-- casa 2 dispositivo
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('estufa','calefaccion',true,2);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('televisor','entretenimiento',true,2);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('computadora','entretenimiento',true,2);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('microondas','electrodomestico',true,2);
INSERT INTO dispositivo(nombre_dispositivo,tipo,estado,id_ubicacion) VALUES('heladera ','electrodomestico',true,2);

-- fetch 
SELECT * FROM usuario;
SELECT * FROM domicilio;
SELECT * from ubicacion;
select * from dispositivo;

