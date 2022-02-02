from ast import arg
from typing import List
from random import randrange
from observer.abstract import Observer
from observer.abstract import Observable
from views.observer_view import ObserverView
from mvc.controller import Controller
from modulos.deco_clase import deco_clase
import datetime
import modulos.constantes as constant

def deco_metodo(f):
    def _deco_metodo(*args):
        if(args):
            file = f'log_{datetime.datetime.now().strftime("%Y_%m_%d")}.txt'
            tipo = type(args[0]).__name__
            cadena = ''

            if(tipo == 'ServicioMeteorologico') and len(args) > 1:
                cadena = f'{datetime.datetime.now().strftime("%H:%M:%S")}'
                cadena = f'{cadena} --> {tipo} opera sobre observer {type(args[1]).__name__}'

            if(tipo != 'ServicioMeteorologico'):
                cadena = f'{datetime.datetime.now().strftime("%H:%M:%S")}'
                cadena = f'{cadena} --> actualizando observer {tipo}'
#
            if(len(cadena) > 0):
                log = open(f'{constant.RUTA_LOG}{file}', 'a')
                log.write(f'{cadena}\n')
                log.close()

        return f(*args)

    return _deco_metodo
@deco_clase
class ServicioMeteorologico(Observable):
    """
    El Observable posee algún estado importante y
    notifica a los observadores cuando el estado cambia.
    """

    _state: int = None
    """
    En aras de la simplicidad, el estado del Observable,
    esencial para todos los suscriptores, se almacena en esta variable.
    """

    _observers: List[Observer] = []

    """
    Lista de suscriptores.
    En la vida real, la lista de suscriptores se puede almacenar de manera más completa
    (clasificada por tipo de evento, etc.).
    """

    @deco_metodo
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    @deco_metodo
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Métodos de gestión de suscripciones.
    """

    @deco_metodo
    def notify(self) -> None:
        """
        Lanza una actualización en cada suscriptor.
        """

        #print("Observable: Notificación a los observadores...")
        for observer in self._observers:
            observer.update(self)

    @deco_metodo
    def informa_temperatura(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción
        de lo que realmente puede hacer un Observable.
        Los observables suelen tener una lógica comercial importante,
        que activa un método de notificación cada vez que algo
        importante está a punto de suceder (o después).
        """

        #print("\nObservable: Estoy haciendo algo importante.")
        self._state = randrange(-10, 40)

        #print(f"Observable: Mi estado acaba de cambiar a: {self._state}")
        self.notify()
class Archivo(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")
        self._observer_view.setWindowTitle(f"Observer {self.tipo}")

    @deco_metodo
    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)

class Laptop(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")
        self._observer_view.setWindowTitle(f"Observer {self.tipo}")

    @deco_metodo
    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)

class Telefono(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")
        self._observer_view.setWindowTitle(f"Observer {self.tipo}")

    @deco_metodo
    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)
