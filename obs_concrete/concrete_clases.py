from typing import List
from random import randrange
from obs_abstract.abstract_clases import Observer
from obs_abstract.abstract_clases import Observable

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
        print("Observable: Adjunto un observador.")
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

    def some_business_logic(self) -> None:
        """
        Por lo general, la lógica de suscripción es solo una fracción
        de lo que realmente puede hacer un Observable.
        Los observables suelen tener una lógica comercial importante,
        que activa un método de notificación cada vez que algo
        importante está a punto de suceder (o después).
        """

        print("\nObservable: Estoy haciendo algo importante.")
        self._state = randrange(0, 10)

        print(f"Observable: Mi estado acaba de cambiar a: {self._state}")
        self.notify()

class Archivo(Observer):
    def update(self, observable: Observable) -> None:
        if observable._state == 1:
            print("Archivo: reaccionó al evento")

class Laptop(Observer):
    def update(self, observable: Observable) -> None:
        if observable._state == 0 or observable._state >= 2:
            print("laptop: reaccionó al evento")

class Telefono(Observer):
    def update(self, observable: Observable) -> None:
        if observable._state < 3:
            print("Telefono: reaccionó al evento")
