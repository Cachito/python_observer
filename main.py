import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from manager import ManagerView
from views.observable import ObservableView

class ObservableWindow(QtWidgets.QMainWindow, ObservableView):
    def __init__(self, parent=None):
        super(ObservableWindow, self).__init__(parent)
        self.setupUi(self)

class ManagerWindow(QtWidgets.QMainWindow, ManagerView):
    def __init__(self, parent=None):
        super(ManagerWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_iniciar_observable.clicked.connect(self.show_observable)
        self.observable_windows = []

    @QtCore.pyqtSlot()
    def show_observable(self):
        print(self.observable_windows)
        print(len(self.observable_windows))

        if(len(self.observable_windows) == 1):
            return
            
        observable_window = ObservableWindow()
        observable_window.show()
        self.observable_windows.append(observable_window)

if __name__ == "__main__":
    # Código del cliente.
    app = QtWidgets.QApplication(sys.argv)
    w = ManagerWindow()
    w.show()
    sys.exit(app.exec_())