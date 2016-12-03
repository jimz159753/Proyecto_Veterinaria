# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.resize(374, 210)
        login.setAutoFillBackground(False)
        login.setStyleSheet(_fromUtf8("QWidget{\n"
"background-image: url(\"/home/jimz/Downloads/Ingenieria_Software/login.jpg\");\n"
"}\n"
"QLineEdit{\n"
"    background: #ffffff;\n"
"}\n"
"QPushButton{\n"
"background: #bbcbe5;\n"
"}\n"
""))
        self.passLineEdit = QtGui.QLineEdit(login)
        self.passLineEdit.setGeometry(QtCore.QRect(110, 70, 151, 20))
        self.passLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.passLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.passLineEdit.setText(_fromUtf8(""))
        self.passLineEdit.setFrame(False)
        self.passLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passLineEdit.setObjectName(_fromUtf8("passLineEdit"))
        self.loginComboBox = QtGui.QComboBox(login)
        self.loginComboBox.setGeometry(QtCore.QRect(110, 110, 151, 21))
        self.loginComboBox.setObjectName(_fromUtf8("loginComboBox"))
        self.loginComboBox.addItem(_fromUtf8(""))
        self.loginComboBox.addItem(_fromUtf8(""))
        self.loginComboBox.addItem(_fromUtf8(""))
        self.userLineEdit = QtGui.QLineEdit(login)
        self.userLineEdit.setEnabled(True)
        self.userLineEdit.setGeometry(QtCore.QRect(110, 32, 151, 20))
        self.userLineEdit.setAutoFillBackground(False)
        self.userLineEdit.setStyleSheet(_fromUtf8(""))
        self.userLineEdit.setText(_fromUtf8(""))
        self.userLineEdit.setFrame(False)
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.loginPushButton = QtGui.QPushButton(login)
        self.loginPushButton.setEnabled(True)
        self.loginPushButton.setGeometry(QtCore.QRect(140, 150, 101, 31))
        self.loginPushButton.setAcceptDrops(False)
        self.loginPushButton.setAutoDefault(True)
        self.loginPushButton.setObjectName(_fromUtf8("loginPushButton"))

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        login.setTabOrder(self.userLineEdit, self.passLineEdit)
        login.setTabOrder(self.passLineEdit, self.loginComboBox)
        login.setTabOrder(self.loginComboBox, self.loginPushButton)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "Login", None))
        self.loginComboBox.setItemText(0, _translate("login", "Veterinaria", None))
        self.loginComboBox.setItemText(1, _translate("login", "Adm", None))
        self.loginComboBox.setItemText(2, _translate("login", "Refugio", None))
        self.loginPushButton.setText(_translate("login", "Aceptar", None))


class login(QtGui.QWidget, Ui_login):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

