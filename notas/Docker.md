# Docker

## ¿Qué es docker?

Es una plataforma de virtualización además de un conjunto de comandos para establecer *workflows* de trabajo que permitan crear, instalar, compartir etc, aplicaciones.

**Docker** está compuesto de dos partes un *daemon* o un servidor y un *cliente*, el comando `docker`.

## Instalación

- [Mac OS X](https://docs.docker.com/docker-for-mac/)
- [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
- [MS Windows](https://docs.docker.com/desktop/windows/)


## Imágen y contenedores

Una **imagen** es una especie de cascarón o plantilla no modificable.

> **Ejemplo**
> Ejemplos de imágenes son `ubuntu` y la imagen de la clase con la que trabajaremos (`ec2022`).

Un **contenedor** es creado a partir de una *imagen*. Los contenedores es aquello con lo que vas a interactuar. Pueden ser ejecutados, iniciados, detenidos, movidos, borrados, etc. Cada contenedor es un ambiente aislado. Aunque pueden ser conectados entre sí.

## Ejercicio

> **NOTA:** Si están en `ubuntu` y no configuraron su usuario como miembros del grupo `docker` agreguen `sudo` al principio de cada comando


- En su computadora, abran una terminal
- Verifiquen que el cliente `docker` esté instalado tecleando `docker`
- Verifiquen que el *daemon* esté corriendo con `docker run hello-world`
- Descarguen una *imagen* de `ubuntu`

```
docker pull ubuntu:latest
```

- Verifiquen que la imagen esté en su computadora

```
docker images
```


- Para crear un contenedor interactivo:

```
docker run -it ubuntu /bin/bash
```

(Aquí podemos hacer lo que se pide en las siguientes secciones de esta *clase*)


Para salir de este contendor tecleen `exit`.

- Para verificar que el contenedor está ahí:

```
docker ps -a
```


## ¿Y la imagen de la clase?

- Descargarla

```
docker pull skalas/ec2022
```

- Creen un contenedor:

```
docker run -p 8888:8888 -it skalas/ec2022
```
- Ejecuten el comando `whoami`. Debería de aparecer `jovyan`
- Si llegaron hasta acá ¡Felicidades! No sufrirán más de lo necesario en este curso.
- Para salir de `docker` usen `Ctrl-d` o tecleen `exit`.


## ¿Y la próxima vez?

- La siguiente vez que quieras ejecutar `docker` usa el siguiente comando:
```
docker start -a -i priceless_carson
```
donde debes de cambiar `priceless_carson` por el nombre del contenedor (la última columna de `docker ps -a`).


## Liga de ayuda

Pueden ver [esto](https://github.com/wsargent/docker-cheat-sheet) si tienen dudas
