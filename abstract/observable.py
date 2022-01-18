from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from observer import Observer

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
