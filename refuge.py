# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'refuge.ui'
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

class Ui_refuge(object):
    def setupUi(self, refuge):
        refuge.setObjectName(_fromUtf8("refuge"))
        refuge.resize(797, 568)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../prize-badge-with-paw-print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        refuge.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(refuge)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-image: url(\"/home/jimz/Downloads/Ingenieria_Software/fondoVet2.jpg\");\n"
"}\n"
"QLineEdit{\n"
"    background: #ffffff;\n"
"    \n"
"}\n"
"QLabel{\n"
"    background: rgba(255, 255, 255, 0); \n"
"}\n"
"QTableWidget{\n"
"    background: #ffffff;\n"
"}\n"
"QPushButton{\n"
"    background: #bbcbe5;\n"
"}\n"
"QGroupBox{\n"
"    background: rgba(255, 255, 255, 0); \n"
"}"))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.registerDDTableWidget = QtGui.QTableWidget(self.tab_2)
        self.registerDDTableWidget.setGeometry(QtCore.QRect(60, 270, 631, 192))
        self.registerDDTableWidget.setFrameShape(QtGui.QFrame.Box)
        self.registerDDTableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.registerDDTableWidget.setObjectName(_fromUtf8("registerDDTableWidget"))
        self.registerDDTableWidget.setColumnCount(4)
        self.registerDDTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.registerDDTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.registerDDTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.registerDDTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.registerDDTableWidget.setHorizontalHeaderItem(3, item)
        self.registerDDTableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.registerDDTableWidget.verticalHeader().setVisible(False)
        self.registerDDTableWidget.verticalHeader().setHighlightSections(False)
        self.imageDDLabel = QtGui.QLabel(self.tab_2)
        self.imageDDLabel.setGeometry(QtCore.QRect(30, 30, 287, 188))
        self.imageDDLabel.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"border: 2px solid black;\n"
"background: #ffffff;"))
        self.imageDDLabel.setFrameShape(QtGui.QFrame.Box)
        self.imageDDLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.imageDDLabel.setText(_fromUtf8(""))
        self.imageDDLabel.setObjectName(_fromUtf8("imageDDLabel"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(350, 50, 181, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.servDDComboBox = QtGui.QComboBox(self.groupBox)
        self.servDDComboBox.setGeometry(QtCore.QRect(30, 80, 131, 31))
        self.servDDComboBox.setFrame(False)
        self.servDDComboBox.setObjectName(_fromUtf8("servDDComboBox"))
        self.servDDComboBox.addItem(_fromUtf8(""))
        self.servDDComboBox.addItem(_fromUtf8(""))
        self.servDDComboBox.addItem(_fromUtf8(""))
        self.servDDComboBox.addItem(_fromUtf8(""))
        self.servDDComboBox.addItem(_fromUtf8(""))
        self.searchDDLineEdit = QtGui.QLineEdit(self.groupBox)
        self.searchDDLineEdit.setGeometry(QtCore.QRect(30, 30, 131, 31))
        self.searchDDLineEdit.setFrame(False)
        self.searchDDLineEdit.setObjectName(_fromUtf8("searchDDLineEdit"))
        self.entryDDPushButton = QtGui.QPushButton(self.tab_2)
        self.entryDDPushButton.setGeometry(QtCore.QRect(540, 50, 71, 51))
        self.entryDDPushButton.setAutoDefault(True)
        self.entryDDPushButton.setObjectName(_fromUtf8("entryDDPushButton"))
        self.deleteDDPushButton = QtGui.QPushButton(self.tab_2)
        self.deleteDDPushButton.setGeometry(QtCore.QRect(540, 140, 71, 51))
        self.deleteDDPushButton.setAutoDefault(True)
        self.deleteDDPushButton.setObjectName(_fromUtf8("deleteDDPushButton"))
        self.outDDPushButton = QtGui.QPushButton(self.tab_2)
        self.outDDPushButton.setGeometry(QtCore.QRect(640, 50, 71, 51))
        self.outDDPushButton.setObjectName(_fromUtf8("outDDPushButton"))
        self.clearDDPushButton = QtGui.QPushButton(self.tab_2)
        self.clearDDPushButton.setGeometry(QtCore.QRect(640, 140, 71, 51))
        self.clearDDPushButton.setAutoDefault(True)
        self.clearDDPushButton.setObjectName(_fromUtf8("clearDDPushButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.registerDCTableWidget = QtGui.QTableWidget(self.tab_3)
        self.registerDCTableWidget.setGeometry(QtCore.QRect(60, 140, 661, 301))
        self.registerDCTableWidget.setFrameShape(QtGui.QFrame.Box)
        self.registerDCTableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.registerDCTableWidget.setObjectName(_fromUtf8("registerDCTableWidget"))
        self.registerDCTableWidget.setColumnCount(9)
        self.registerDCTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.registerDCTableWidget.setHorizontalHeaderItem(8, item)
        self.registerDCTableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.registerDCTableWidget.verticalHeader().setVisible(False)
        self.registerDCTableWidget.verticalHeader().setHighlightSections(False)
        self.buscarDCLineEdit = QtGui.QLineEdit(self.tab_3)
        self.buscarDCLineEdit.setGeometry(QtCore.QRect(300, 90, 201, 31))
        self.buscarDCLineEdit.setFrame(False)
        self.buscarDCLineEdit.setObjectName(_fromUtf8("buscarDCLineEdit"))
        self.clearDCPushButton = QtGui.QPushButton(self.tab_3)
        self.clearDCPushButton.setGeometry(QtCore.QRect(370, 10, 71, 51))
        self.clearDCPushButton.setObjectName(_fromUtf8("clearDCPushButton"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.chatLineEdit = QtGui.QLineEdit(self.tab_4)
        self.chatLineEdit.setGeometry(QtCore.QRect(110, 430, 551, 41))
        self.chatLineEdit.setAutoFillBackground(False)
        self.chatLineEdit.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"border: 2px solid black;\n"
"background: #ffffff;"))
        self.chatLineEdit.setText(_fromUtf8(""))
        self.chatLineEdit.setObjectName(_fromUtf8("chatLineEdit"))
        self.chatTextBrowser = QtGui.QTextBrowser(self.tab_4)
        self.chatTextBrowser.setGeometry(QtCore.QRect(30, 20, 711, 391))
        self.chatTextBrowser.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"border: 2px solid black;\n"
"background: #ffffff;"))
        self.chatTextBrowser.setObjectName(_fromUtf8("chatTextBrowser"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)
        refuge.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(refuge)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        refuge.setStatusBar(self.statusbar)
        self.actionCerrar_sesion = QtGui.QAction(refuge)
        self.actionCerrar_sesion.setObjectName(_fromUtf8("actionCerrar_sesion"))
        self.actionCerrar = QtGui.QAction(refuge)
        self.actionCerrar.setObjectName(_fromUtf8("actionCerrar"))

        self.retranslateUi(refuge)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(refuge)
        refuge.setTabOrder(self.searchDDLineEdit, self.servDDComboBox)
        refuge.setTabOrder(self.servDDComboBox, self.entryDDPushButton)
        refuge.setTabOrder(self.entryDDPushButton, self.outDDPushButton)
        refuge.setTabOrder(self.outDDPushButton, self.deleteDDPushButton)
        refuge.setTabOrder(self.deleteDDPushButton, self.registerDDTableWidget)
        refuge.setTabOrder(self.registerDDTableWidget, self.buscarDCLineEdit)
        refuge.setTabOrder(self.buscarDCLineEdit, self.registerDCTableWidget)
        refuge.setTabOrder(self.registerDCTableWidget, self.chatTextBrowser)
        refuge.setTabOrder(self.chatTextBrowser, self.chatLineEdit)

    def retranslateUi(self, refuge):
        refuge.setWindowTitle(_translate("refuge", "Refugio", None))
        item = self.registerDDTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("refuge", "Ingreso", None))
        item = self.registerDDTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("refuge", "Salida", None))
        item = self.registerDDTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("refuge", "ID", None))
        item = self.registerDDTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("refuge", "Servicio", None))
        self.groupBox.setTitle(_translate("refuge", "Servicios", None))
        self.servDDComboBox.setItemText(0, _translate("refuge", "Tratamiento medico", None))
        self.servDDComboBox.setItemText(1, _translate("refuge", "Enfermedad general", None))
        self.servDDComboBox.setItemText(2, _translate("refuge", "Vacunas", None))
        self.servDDComboBox.setItemText(3, _translate("refuge", "Estetica", None))
        self.servDDComboBox.setItemText(4, _translate("refuge", "Guarderia", None))
        self.searchDDLineEdit.setText(_translate("refuge", "Buscar | Ingresar", None))
        self.entryDDPushButton.setText(_translate("refuge", "Ingreso", None))
        self.deleteDDPushButton.setText(_translate("refuge", "Eliminar", None))
        self.outDDPushButton.setText(_translate("refuge", "Salida", None))
        self.clearDDPushButton.setText(_translate("refuge", "Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("refuge", "Datos perro", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("refuge", "Nombre", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("refuge", "Apellido1", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("refuge", "Apellido2", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("refuge", "Direccion", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("refuge", "Celular", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("refuge", "C.P", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("refuge", "E-mail", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("refuge", "Telefono", None))
        item = self.registerDCTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("refuge", "ID", None))
        self.clearDCPushButton.setText(_translate("refuge", "Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("refuge", "Datos cliente", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("refuge", "Chat", None))
        self.actionCerrar_sesion.setText(_translate("refuge", "Cerrar sesion", None))
        self.actionCerrar.setText(_translate("refuge", "Cerrar", None))


class refuge(QtGui.QMainWindow, Ui_refuge):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)

