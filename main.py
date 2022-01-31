from msilib.schema import Control
import sys
import random
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from views.manager_view import ManagerView
from views.observable_view import ObservableView
from views.observer_view import ObserverView
from observer.concrete import ServicioMeteorologico
from observer.concrete import Telefono
from observer.concrete import Laptop
from observer.concrete import Archivo
from mvc.controller import Controller

class ObserverWindow(QtWidgets.QMainWindow, ObserverView):
    def __init__(self, parent=None):
        super(ObserverWindow, self).__init__(parent)
        self.setupUi(self)

class ObservableWindow(QtWidgets.QMainWindow, ObservableView):
    def __init__(self, parent=None):
        super(ObservableWindow, self).__init__(parent)
        self.setupUi(self)

class ManagerWindow(QtWidgets.QMainWindow, ManagerView):
    def __init__(self, parent=None):
        super(ManagerWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_iniciar_observable.clicked.connect(self.show_observable)
        self.btn_iniciar_observador.clicked.connect(self.show_observador)
        self.lista_observables = []
        self.lista_observadores = []
        self.controller = Controller()

    @QtCore.pyqtSlot()
    def show_observable(self):
        if(len(self.lista_observables) == 1):
            print("Ya ha iniciado el observable.")
            return

        observable_window = ObservableWindow()
        observable_obj = ServicioMeteorologico()
        observable_window.observable = observable_obj
        observable_window.show()
        self.lista_observables.append(observable_window)

    @QtCore.pyqtSlot()
    def show_observador(self):
        if(len(self.lista_observables) < 1):
            print("Debe iniciar el observable primero.")
            return

        observable_obj = self.lista_observables[0]

        observer_obj = self.get_observer_type()

        observer_window = ObserverWindow()

        observer_window.observable = observable_obj
        observer_window.observer = observer_obj
        observer_obj.observer_view = observer_window
        observer_obj.controller = self.controller

        observable_obj.attach(observer_obj)

        observer_window.show()
        self.lista_observadores.append(observer_window)

    def get_observer_type(self):
        observer_type = random.randint(1, 3)

        if observer_type == 1:
            return Archivo()
        elif observer_type == 2:
            return Telefono()
        else:
            return Laptop()

if __name__ == "__main__":
    # Código del cliente.
    app = QtWidgets.QApplication(sys.argv)
    w = ManagerWindow()
    w.show()
    sys.exit(app.exec_())