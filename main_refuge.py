import sys , os
from refuge import Ui_refuge
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from PyQt4.QtNetwork import *


PORTS = (9998, 9999)
PORT = 9999
SIZEOF_UINT32 = 4

class Refuge(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.socket = QTcpSocket()
		self.nextBlockSize = 0
		self.request = None
		self.ref = Ui_refuge()
		self.ref.setupUi(self)
		self.msg = QMessageBox()
		self.date = QDate.currentDate()
		self.ref.buscarDCLineEdit.returnPressed.connect(self.display_Cli)
		self.ref.entryDDPushButton.clicked.connect(self.entry_DD)
		self.ref.outDDPushButton.clicked.connect(self.out_DD)
		self.ref.searchDDLineEdit.returnPressed.connect(self.search_DD)
		self.ref.deleteDDPushButton.clicked.connect(self.remove_DD)
		self.ref.clearDDPushButton.clicked.connect(self.clear_DD)
		self.ref.clearDCPushButton.clicked.connect(self.clear_DC)
		self.connectToServer()
		self.ref.chatLineEdit.returnPressed.connect(self.issueRequest)
		self.socket.readyRead.connect(self.readFromServer)
		self.socket.disconnected.connect(self.serverHasStopped)
		self.connect(self.socket,
                     SIGNAL("error(QAbstractSocket::SocketError)"),
                     self.serverHasError)

#|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°
	# REGISTRO SERVICIOS #
	
	def connect_Account(self):
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('database.db')
		if db.open() == False:
			self.msg.information(self,"informativo","No se conecto la base de datos")

	def entry_DD(self):
		entry = self.date.getDate()
		out = ''
		idD = self.ref.searchDDLineEdit.text()
		serv = self.ref.servDDComboBox.currentText()
		try:
			query = "INSERT INTO servicios(fecha_ingreso,fecha_salida,id,tipo_servicio) values('%s','%s','%s','%s')"%(entry,out,idD,serv)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Agregado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.ref.searchDDLineEdit.clear()
			self.ref.registerDDTableWidget.clear()
			self.ref.imageDDLabel.clear()

	def out_DD(self):
		search = self.ref.searchDDLineEdit.text()
		out = self.date.getDate()
		try:
			query = "UPDATE servicios SET fecha_salida='%s' WHERE id='%s'"%(out,search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Agregado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.ref.searchDDLineEdit.clear()
			self.ref.registerDDTableWidget.clear()
			self.ref.imageDDLabel.clear()

	def search_DD(self):
		search = self.ref.searchDDLineEdit.text()
		self.ref.registerDDTableWidget.clear()
		try:
			query = "SELECT * FROM servicios WHERE id='%s'"%(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0
			while sql.next():
				if self.ref.registerDDTableWidget.rowCount() < sql.at()+1:		
					self.ref.registerDDTableWidget.insertRow(sql.at())
				while j < 4:
					self.ref.registerDDTableWidget.setItem(i,j,QTableWidgetItem(str(sql.value(j))))
					j += 1
				i += 1
		except:
			self.msg.information(self,"informativo","Error en la consulta")
		try:
			query = "SELECT id, carpeta FROM perros WHERE id='%s'"%search
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0
			while sql.next():
				if sql.value(0) == search:
					self.ref.imageDDLabel.setPixmap(QPixmap(sql.value(1)))
				else:
					self.msg.information(self,"informativo","El valor no existe")
		except:
			self.msg.information(self,"informativo","Error en la consulta")

	def remove_DD(self):
		search = self.ref.searchDDLineEdit.text()
		try:
			query = "DELETE FROM servicios WHERE id='%s'"%(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			print(state)
			if state:
				self.msg.information(self,"informativo","Eliminado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.ref.searchDDLineEdit.clear()
			self.ref.registerDDTableWidget.clear()
			self.ref.imageDDLabel.clear()
			
	def clear_DD(self):
		self.ref.searchDDLineEdit.clear()
		self.ref.registerDDTableWidget.clear()
		self.ref.imageDDLabel.clear()
#|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°
	# DATOS CLIENTES #

	def display_Cli(self):
		search = self.ref.buscarDCLineEdit.text() # search by client name.
		try:
			query = "SELECT * FROM clientes WHERE id like '%{0}%' or nombre like '%{0}%' or apellido1 like '%{0}%' or apellido2 like '%{0}%' or direccion like '%{0}%' or celular like '%{0}%' or cp like '%{0}%' or email like '%{0}%' or telefono like '%{0}%' ".format(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0
			self.ref.registerDCTableWidget.clear()
			while sql.next():
				if self.ref.registerDCTableWidget.rowCount() < sql.at()+1:
					self.ref.registerDCTableWidget.insertRow(sql.at())
				while j < 9:
					self.ref.registerDCTableWidget.setItem(i,j,QTableWidgetItem(str(sql.value(j))))
					j += 1
				j = 0
				i += 1
		except:
			self.msg.information(self,"informativo","Error en la consulta")
			
	def clear_DC(self):
		self.ref.registerDCTableWidget.clear()
		self.ref.buscarDCLineEdit.clear()

	def connectToServer(self):
		self.socket.connectToHost("localhost", PORT)
	
	def issueRequest(self):
		self.request = QByteArray()
		stream = QDataStream(self.request, QIODevice.WriteOnly)
		stream.setVersion(QDataStream.Qt_4_2)
		stream.writeUInt32(0)
		stream.writeQString(self.ref.chatLineEdit.text())
		stream.device().seek(0)
		stream.writeUInt32(self.request.size() - SIZEOF_UINT32)
		self.socket.write(self.request)
		self.nextBlockSize = 0
		self.request = None
		self.ref.chatLineEdit.clear()
	
	def readFromServer(self):
		stream = QDataStream(self.socket)
		stream.setVersion(QDataStream.Qt_4_2)
		while True:
			if self.nextBlockSize == 0:
				if self.socket.bytesAvailable() < SIZEOF_UINT32:
					break
				self.nextBlockSize = stream.readUInt32()
			if self.socket.bytesAvailable() < self.nextBlockSize:
				break
			textFromServer = stream.readQString()
			self.ref.chatTextBrowser.append(textFromServer) # output
			self.nextBlockSize = 0

	def serverHasStopped(self):
		self.socket.close()
		self.connectButton.setEnabled(True)

	def serverHasError(self):
		self.ref.chatTextBrowser.append("Error: {}".format(
        				self.socket.errorString()))
		self.socket.close()

def main():
	app = QApplication(sys.argv)
	win_ref = Refuge() 
	win_ref.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
