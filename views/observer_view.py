# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ObserverView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from observer.abstract import Observable
from observer.abstract import Observer

class ObserverView(QtWidgets.QDialog):
    def setupUi(self, ObserverView):
        # view
        ObserverView.setObjectName("ObserverView")
        ObserverView.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ObserverView.sizePolicy().hasHeightForWidth())
        ObserverView.setSizePolicy(sizePolicy)
        ObserverView.setMinimumSize(QtCore.QSize(300, 200))
        ObserverView.setMaximumSize(QtCore.QSize(300, 200))
        ObserverView.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./imagenes/manager.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ObserverView.setWindowIcon(icon)
        ObserverView.setWindowTitle("Observer")

        # label tipo de display
        self.lbl_display = QtWidgets.QLabel(ObserverView)
        self.lbl_display.setGeometry(QtCore.QRect(40, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lbl_display.setFont(font)
        self.lbl_display.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_display.setObjectName("lbl_display")
        self.lbl_display.setText("tipo display")

        # label state
        self.lbl_state = QtWidgets.QLabel(ObserverView)
        self.lbl_state.setGeometry(QtCore.QRect(40, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lbl_state.setFont(font)
        self.lbl_state.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_state.setObjectName("lbl_state")
        self.lbl_state.setText("estado informado")

        # bot??n detach
        self.btn_detach = QtWidgets.QPushButton(ObserverView)
        self.btn_detach.setGeometry(QtCore.QRect(70, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.btn_detach.setFont(font)
        self.btn_detach.setObjectName("btn_detach")
        self.btn_detach.setText("Detach")
        self.btn_detach.clicked.connect(self.detach_me)

        QtCore.QMetaObject.connectSlotsByName(ObserverView)

        ObserverView.show()

    def detach_me(self):
        self.observable.detach(self.observer)
        self.destroy()

    @property
    def observer(self) -> Observer:
        return self._observer

    @observer.setter
    def observer(self, valor):
        self._observer = valor

    @property
    def observable(self) -> Observable:
        return self._observable

    @observable.setter
    def observable(self, valor):
        self._observable = valor
