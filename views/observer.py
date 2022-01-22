# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'observer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class UiObserver(object):
    def setupUi(self, observer):
        observer.setObjectName("observer")
        observer.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(observer.sizePolicy().hasHeightForWidth())
        observer.setSizePolicy(sizePolicy)
        observer.setMinimumSize(QtCore.QSize(300, 200))
        observer.setMaximumSize(QtCore.QSize(300, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagenes/manager.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        observer.setWindowIcon(icon)
        self.lbl_display = QtWidgets.QLabel(observer)
        self.lbl_display.setGeometry(QtCore.QRect(40, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lbl_display.setFont(font)
        self.lbl_display.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_display.setObjectName("lbl_display")
        self.lbl_state = QtWidgets.QLabel(observer)
        self.lbl_state.setGeometry(QtCore.QRect(40, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.lbl_state.setFont(font)
        self.lbl_state.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_state.setObjectName("lbl_state")
        self.btn_detach = QtWidgets.QPushButton(observer)
        self.btn_detach.setGeometry(QtCore.QRect(70, 140, 161, 41))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(12)
        self.btn_detach.setFont(font)
        self.btn_detach.setObjectName("btn_detach")

        self.retranslate_ui(observer)
        QtCore.QMetaObject.connectSlotsByName(observer)

    def retranslate_ui(self, observer):
        _translate = QtCore.QCoreApplication.translate
        observer.setWindowTitle(_translate("observer", "observer"))
        self.lbl_display.setText(_translate("observer", "display"))
        self.lbl_state.setText(_translate("observer", "state"))
        self.btn_detach.setText(_translate("observer", "Detach"))

    def __init__(self, titulo, display_type, state):
        self._titulo = titulo
        self._display_type = display_type
        self._state = state

    @property
    def titulo(self):
        return self._titulo

    @property
    def display_type(self):
        return self._display_type

    @property
    def state(self):
        return self.state

    def show_window(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_display.setText(_translate("observer", self.display_type))
        self.lbl_state.setText(_translate("observer", self.state))
        self.setWindowTitle(_translate("observer", self.titulo))

#if __name__ == "__main__":
#    app = QtWidgets.QApplication(sys.argv)
#    observer = QtWidgets.QDialog()
#    ui = UiObserver()
#    ui.setupUi(observer)
#    observer.show()
#    sys.exit(app.exec_())
