## info de la materia: 

ST0263 TOPICOS EN TELEMATICA

## Estudiante(s): 

Andres Danilo Patiño Velez, apatin14@eafit.edu.co
Juan camilo Anzola Gomez, jcanzolag@eafit.edu.co

## Profesor: 

Edwin Nelson Montoya Munera

## Actividad: 

Laboratorio 1
  
## 1. breve descripción de la actividad

Desplegar un middleware orientado a mensajes (MOM) con el fin de afianzar los conocimientos
desarrollados en la sesión de clases.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

✔ Incluir un dispositivo fisico para enviar datos al middleware (MOM)
✔ Incluir tres aplicaciones que simulen datos para enviar datos al middleware (MOM) 
✔ Incluir una aplicacion cliente que almacene los datos del middleware en base de datos 
✔ Incluir Clientes que consuman los datos emitidos al middleware


### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.



## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

### como se compila y ejecuta.

#### Proveedor 1
  py sensorServer1.py
  
### detalles del desarrollo.
  El desarrolo esta generado en python como un servidor, tiene configurado por defecto el puerto 80 configurado en el codigo.
  
  El desarrollo esta ligado al puerto 80 para la ejecucion, suele dar algunos inconvenientes en distribuciones de linux
### opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
  
   📁./
    |
    ├─💽index.html
    ├─💽404.html
    ├─💽server.js
    ├─💽Readme.MD
  

## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
  
  Lista de requisitos de python [aca](https://github.com/st0263-2266/lab1-apatin14/blob/main/requirements.txt)

## IP o nombres de dominio en nube o en la máquina servidor.
  
[Lab1-apatin](https://lab1-apatin14.herokuapp.com/)

## como se lanza el servidor.
  Ejecutando el comando: Python server.py

## una mini guia de como un usuario utilizaría el software o la aplicación

  Se puede abrir la direccion https://lab1-apatin14.herokuapp.com, acontinuacion debe agregar /{{filename}}.{{fileextension}} dentro de la misma url
  
  en caso de ser encontrado el servidor mostrar el archivo
  en caso contrario monstrar la pantalla de error 404

  si se accede bajo un protocolo no valido mostrar un error
  

#### versión README.md -> 1.0 (2022-agosto)