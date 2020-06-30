CREATE DATABASE IF NOT EXISTS practica1;

USE practica1

CREATE TABLE IF NOT EXISTS usuarios (

id           INTEGER(10) AUTO_INCREMENT NOT NULL,

name         VARCHAR(100) NOT NULL ,

last         VARCHAR(100) NOT NULL,

mail          VARCHAR(100) NOT NULL,

pass          VARCHAR(100) NOT NULL,

fecha          DATE NOT NULL,

CONSTRAINT   pk_usuarios PRIMARY KEY (id),
CONSTRAINT   uq_mail     UNIQUE (mail)

) ENGINE=InnoDb;


CREATE TABLE IF NOT EXISTS notas (

id                   INTEGER(100) AUTO_INCREMENT NOT NULL,

usuario_id            INTEGER(100) NOT NULL,

titulo                VARCHAR(100) NOT NULL,

nota                  VARCHAR(100) NOT NULL,

fecha                 DATE NOT NULL,

CONSTRAINT   pk_notas PRIMARY KEY (id),
CONSTRAINT   fk_notas FOREIGN KEY = (usuario_id) REFERENCES usuarios(id)


)ENGINE=InnoDb;
