import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from manager import ManagerView
from views.observable import ObservableView
from views.observer import ObserverView

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

    @QtCore.pyqtSlot()
    def show_observable(self):
        if(len(self.lista_observables) == 1):
            print("Ya ha iniciado el observable.")
            return

        observable_window = ObservableWindow()
        observable_window.show()
        self.lista_observables.append(observable_window)

    @QtCore.pyqtSlot()
    def show_observador(self):
        if(len(self.lista_observables) < 1):
            print("Debe iniciar el observable primero.")
            return

        observer_window = ObserverWindow()
        observer_window.show()
        self.lista_observadores.append(observer_window)

if __name__ == "__main__":
    # Código del cliente.
    app = QtWidgets.QApplication(sys.argv)
    w = ManagerWindow()
    w.show()
    sys.exit(app.exec_())