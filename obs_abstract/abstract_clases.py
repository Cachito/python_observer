from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Observable(ABC):
    """
    La interfaz Observable declara un conjunto de métodos para administrar suscriptores.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Adjunta un observador al observable.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Quita a un observador del observable.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notifica sobre un evento a todos los observadores.
        """
        pass

class Observer(ABC):
    """
    La interfaz de Observer declara el método de actualización (update),
    utilizado por los observables.
    """

    @abstractmethod
    def update(self, subject: Observable) -> None:
        """
        Recibir actualización del observable.
        """
        pass