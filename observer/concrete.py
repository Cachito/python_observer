from typing import List
from random import randrange
from observer.abstract import Observer
from observer.abstract import Observable
from views.observer_view import ObserverView
from mvc.controller import Controller


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

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Métodos de gestión de suscripciones.
    """

    def notify(self) -> None:
        """
        Lanza una actualización en cada suscriptor.
        """

        print("Observable: Notificación a los observadores...")
        for observer in self._observers:
            observer.update(self)

    def informa_temperatura(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción
        de lo que realmente puede hacer un Observable.
        Los observables suelen tener una lógica comercial importante,
        que activa un método de notificación cada vez que algo
        importante está a punto de suceder (o después).
        """

        print("\nObservable: Estoy haciendo algo importante.")
        self._state = randrange(-10, 40)

        print(f"Observable: Mi estado acaba de cambiar a: {self._state}")
        self.notify()

class Archivo(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")

    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)

class Laptop(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")

    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)

class Telefono(Observer):
    @property
    def controller(self) -> Controller:
        return self._controller

    @controller.setter
    def controller(self, valor):
        self._controller = valor

    @property
    def observer_view(self) -> ObserverView:
        return self._observer_view

    @observer_view.setter
    def observer_view(self, valor):
        self._observer_view = valor
        self.tipo = type(self).__name__
        self._observer_view.lbl_display.setText(f"{self.tipo} display")

    def update(self, observable: Observable) -> None:
        self.observer_view.lbl_state.setText(f"Temperatura: {observable._state}°")
        self.controller.save(self.tipo, "Temperatura", observable._state)