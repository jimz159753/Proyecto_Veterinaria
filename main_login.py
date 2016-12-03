import sys , os
from login import Ui_login
from main_veterinary import Veterinary
from main_refuge import Refuge
from main_admin import Admin
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from PyQt4.QtNetwork import *

class Login(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.msg = QMessageBox()
		self.connect_Account()
		self.login = Ui_login()
		self.login.setupUi(self)
		self.vet = Veterinary()
		self.adm = Admin()
		self.ref = Refuge()
		self.connections = []
		self.login.loginPushButton.clicked.connect(self.compare_Account)
		self.tcpServer = QTcpServer()
		self.tcpServer.listen(QHostAddress("0.0.0.0"),9999)
		self.tcpServer.newConnection.connect(self.addConnections)

	def addConnections(self):
		clientConnection = self.tcpServer.nextPendingConnection()
		clientConnection.nextBlockSize = 0
		self.connections.append(clientConnection)
		self.connect(clientConnection, SIGNAL("readyRead()"), 
                self.receiveMessage)
	
	def receiveMessage(self):
		for s in self.connections:
			if s.bytesAvailable() > 0:
				stream = QDataStream(s)
				stream.setVersion(QDataStream.Qt_4_2)
				if s.nextBlockSize == 0:
					if s.bytesAvailable() < 4:
						return
					s.nextBlockSize = stream.readUInt32()
				if s.bytesAvailable() < s.nextBlockSize:
					return

				textFromClient = stream.readQString()
				s.nextBlockSize = 0
				self.sendMessage(textFromClient, 
                                 s.socketDescriptor())
				s.nextBlockSize = 0

	def sendMessage(self, text, socketId):
		for s in self.connections:
			if s.socketDescriptor() == socketId:
				message = "Tu> {}".format(text)
			else:
				message = "{}> {}".format(socketId, text)
			reply = QByteArray()
			stream = QDataStream(reply, QIODevice.WriteOnly)
			stream.setVersion(QDataStream.Qt_4_2)
			stream.writeUInt32(0)
			stream.writeQString(message)
			stream.device().seek(0)
			stream.writeUInt32(reply.size() - 4)
			s.write(reply)
		
	def connect_Account(self):
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('database.db')
		if db.open() == False:
			self.msg.information(self,"informativo","No se conecto la base de datos")

	def compare_Account(self):
		try:
			query = "SELECT * FROM admin"
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			sig = False
			while sql.next():
				if self.login.userLineEdit.text() == sql.value(5) and self.login.passLineEdit.text() == sql.value(9) and self.login.loginComboBox.currentText() == 'Veterinaria':
					sig = True	
					self.vet.show()					
				elif self.login.userLineEdit.text() == sql.value(5) and self.login.passLineEdit.text() == sql.value(9) and self.login.loginComboBox.currentText() == 'Adm':
					self.adm.show()
					sig = True					
				elif self.login.userLineEdit.text() == sql.value(5) and self.login.passLineEdit.text() == sql.value(9) and self.login.loginComboBox.currentText() == 'Refugio':
					self.ref.show()
					sig = True	
			if sig == False:
				self.msg.information(self,"informativo","usuario o contraseña erronea")
				self.login.userLineEdit.setFocus()
		except:
			self.msg.information(self,"informativo","Error en la consulta")
		finally:
			self.login.userLineEdit.clear()
			self.login.passLineEdit.clear()

def main():
	app       = QApplication(sys.argv)
	win_login = Login() 
	win_login.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
