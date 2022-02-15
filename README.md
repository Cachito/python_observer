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

## Fuentes Consultadas.
* Documentos y videos entregados en este curso.
* [Observer Pattern: Christopher Okhravi](https://youtu.be/_BpmfnqjgzQ)
* [Observer method – Python Design Patterns](https://www.geeksforgeeks.org/observer-method-python-design-patterns/#:~:text=The%20observer%20method%20is%20a,object%20that%20they%20are%20observing.)
* [Creating additional windows](https://www.pythonguis.com/tutorials/creating-multiple-windows/)
* [Having trouble opening multiple windows in PyQt5](https://stackoverflow.com/questions/52797269/having-trouble-opening-multiple-windows-in-pyqt5)

## Requerimientos.
Es conveniente (aunque no necesario) crear un entorno virtual para instalar:
```
pip install SIP
pip install PyQt5
pip install pyqt5-tools
pip install PySide2
pip install QT-PyQt-PySide-Custom-Widgets
pip install pyqt5-tools
pip install peewee
```

## Pantalla Principal.
![](./docs/Manager.png)
La pantalla principal (llamada Manager) permite:
### Iniciar ```Observable``` (```Subject```).
Solo es posible iniciar uno.
### Iniciar Observador (```Observer```).
Solo se pueden iniciar si el Observable está iniciado, no antes. Pueden crearse tantas instancias de Observer como se desee.
###Terminar.
Al terminar el programa se cierran todas las ventanas abiertas.

## Preview
Insert here an image of the preview if your project has one. The image can be into the project, you have to indicate the route and look like this.

![](/preview.jpg)

### Notes
If you want to learn all about markdown i recommend you visit the site [markdown.es](https://markdown.es/sintaxis-markdown/)
