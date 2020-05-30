# Sistema de Recomendación de Videos

Este es un proyecto en el que se implementa un sistema de recomendacion de videos basandonos en el algoritmo content-based filtering en el cual se hace una prediccion en base al contenido que un usuario consume utilizando las caracteristicas del mismo (Tags, Genero, etc).


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu computadora para propósitos de desarrollo y pruebas._

### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

* Tener instalado neo4J
* Crear un grafo local con las siguientes propiedades:

```
name: neo4j
password: 123
```

* Tener instalado python
* Instalar la librería py2neo en python
* Importar la librería “Graph” de py2neo

### Instrucciones de ejecucion ▶️

1. Correr el grafo local creado anteriormente en neo4j
2. Importar el archivo csv llamado “datosVideos.csv”
3. Correr el programa en Python
4. Introducir de nombre de usuario “Gabriel” o “Oscar”
5. Se desplegará un menú como el que se muestra a continuación:

```
INGRESE UNA OPCION:

1. Explorar
2. Recomendaciones
3. Historial
4. Eliminar historial
5. Salir
```
6. Debe ingresar el número de opción para acceder a cada función
	a. Si selecciona “1” se le mostraran videos que no están relacionados con
	   videos que ha visto anteriormente
	b. Si selecciona “2” se le mostraran videos que tienen relación con lo que ha
	   visto
	c. Si selecciona “3” se le mostraran los videos que ha visto
	d. Si selecciona “4” eliminara el registro de los videos que ha visto
	e. Si selecciona “5” saldrá del programa


## Construido con 🛠️

* [Python](https://www.python.org/doc/) - Lenguaje utilizado
* [Neo4j](https://neo4j.com/docs/) - Manejador de base de datos y grafos
* [Py2neo](https://py2neo.org/2.0/essentials.html) - Libreria de Neo4j


## Autores ✒️

* **Oscar Paredez** [oscarparedez](https://github.com/oscarparedez)
* **Gabriel Quiroz** [gabrielquirozz](https://github.com/gabrielquirozz)
* **Jose Pablo Ponce** [JosePabloPonce](https://github.com/JosePabloPonce)
* **Eduardo Ramírez** [eduardorh1312](https://github.com/eduardorh1312)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/eduardorh1312/Proyecto2_CC2003S30/graphs/contributors) quíenes han participado en este proyecto. 

