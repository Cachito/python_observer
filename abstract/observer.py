from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
from observable import Observable

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