# Estación Meteorológica
Entrega final del nivel avanzado del curso Python 3 de Facultad Regional Buenos Aires de la Universidad Tecnológica Nacional.

## Grupo de Trabajo
* Luis Elías Carro
* Christian Maier

## Profesores
* Gabriela Verónica Aquino
* Brenda Abigail Barreto Aquino
* Juan Marcelo Barreto Rodriguez

## Descripción
El programa simula una estación meteorológica que informa la temperatura. Distintos dispositivos pueden suscribirse (attach) para recibir esta información y cancelar esta suscripción (detach) cuando deseen hacerlo.

Este proyecto cumple con:
* Patrón de diseño Observer. 
* Patrón de diseño MVC.
* Uso de ORM peewee con SQLite.
* Registro de log mediante decoradores.

El módulo principal es ```main.py```.

El patrón de diseño ```Observer``` se presenta con una clase ```Subject``` como el elemento a observar, al que los ```Observers``` se suscriben para recibir información. Nosotros decidimos llamar a esta clase ```Observable```.

## Demo
If you want to see the demo of this proyect deployed, you can visit [Demo of the proyect](https://anabelisa.co/tips-para-hacer-un-buen-readme-md/)

## How to clone
If you have special requirements, you have to list it step by step.
* This is the first step
* Then you have to do this
* Finally do this

Markdown has enumation and nested lists.

## Installation
To install and run this proyect just type and execute
```bash
npm install
```
## Preview
Insert here an image of the preview if your project has one. The image can be into the project, you have to indicate the route and look like this.

![](/preview.jpg)

### Notes
If you want to learn all about markdown i recommend you visit the site [markdown.es](https://markdown.es/sintaxis-markdown/)
