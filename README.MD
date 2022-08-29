## Informacion de la materia:

- ST0263 TOPICOS EN TELEMATICA

## Estudiante(s):

- Andres Danilo Patiño Velez, apatin14@eafit.edu.co
- Juan camilo Anzola Gomez, jcanzolag@eafit.edu.co

## Profesor:

- Edwin Nelson Montoya Munera

## Actividad:

- Laboratorio 1

## 1. breve descripción de la actividad

Desplegar un middleware orientado a mensajes (MOM) con el fin de afianzar los conocimientos
desarrollados en la sesión de clases.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Incluir un dispositivo fisico para enviar datos al middleware (MOM)
- Incluir tres aplicaciones que simulen datos para enviar datos al middleware (MOM)
- Incluir una aplicacion cliente que almacene los datos del middleware en base de datos
- Incluir Clientes que consuman los datos emitidos al middleware

### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.


### como se compila y ejecuta.

#### Proveedor 1

- py sensorServer.py

#### Proveedor 2

- py tempServer.py

#### Cliente 1

- py sensorClient.py

#### Proveedor 2

- py tempClient.py

### detalles del desarrollo.

El desarrollo esta generado en python con una arquitectura Cliente/Servidor, en la cual se encuentra en la raiz el archivo correspondiente a las variables de entorno `.env` la cual contiene la configuracion de la aplicacion.

### opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

- 📁./
-  |
- ├─💽sensorClient.py
- ├─💽sensorServer.py
- ├─💽tempServer.py
- ├─💽tempClient.py
- ├─💽.env
- ├─💽README.MD


## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lista de requisitos de python [aca](https://github.com/apatin14/lab2-apatin14_jcanzolag/blob/master/requirements.txt)

## IP o nombres de dominio en nube o en la máquina servidor.

[Lab1-apatin](https://lab1-apatin14.herokuapp.com/)

## como se lanza el servidor.

Ejecutando el comando para el servidor del Sensor: py sensorServer.py
Ejecutando el comando para el cliente del Sensor: py sensorClient.py
Ejecutando el comando para el servidor de Temperatura: py tempServer.py
Ejecutando el comando para el cliente de Temperatura: py tempClient.py

## una mini guia de como un usuario utilizaría el software o la aplicación

Se puede abrir la direccion https://lab1-apatin14.herokuapp.com, acontinuacion debe agregar /{{filename}}.{{fileextension}} dentro de la misma url

en caso de ser encontrado el servidor mostrar el archivo
en caso contrario monstrar la pantalla de error 404

si se accede bajo un protocolo no valido mostrar un error

#### versión README.md -> 1.0 (2022-agosto)
