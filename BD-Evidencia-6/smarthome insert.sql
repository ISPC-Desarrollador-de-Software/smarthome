-- insert
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('David', 'Flores','David_Flores@gmail.com','David11','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('laura', 'Diaz','laura_diaz14@gmail.com','laura2','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('sofia', 'vergara','sofia_vergara69@gmail.com','sofi99','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Luis', 'Lopez','lopez_luis_40@gmail.com','luisL23','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('daniel', 'zapata','zapata_daniel@gmail.com','daniel20','123456',0);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('lucas', 'tapia','lucas_tapia58@gmail.com','lucas10','123456',0);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('matias', 'tolaba','matias_tolaba@gmail.com','matute','123456',0);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('lisandro', 'anzaldo','lisandro_88@gmail.com','lis88','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Miguel', 'Flores','miguel_10@gmail.com','miguelito','123456',1);
INSERT INTO usuario(nombre,apellido,email,usuario,contrasena,rol) VALUES ('Martin', 'Flores','martin_flores969@gmail.com','tincho132','123456',1);

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