import sys , os
from veterinary import Ui_veterinary
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
from PyQt4.QtNetwork import *

PORTS = (9998, 9999)
PORT = 9999
SIZEOF_UINT32 = 4

class Veterinary(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.socket = QTcpSocket()
		self.nextBlockSize = 0
		self.request = None
		self.vet = Ui_veterinary()
		self.vet.setupUi(self)
		self.msg = QMessageBox()
		self.file = ""
		self.charge_Cli()
		self.charge_Dog()
		self.vet.entryCPushButton.clicked.connect(self.register_Cli)
		self.vet.searchCLineEdit.returnPressed.connect(self.search_Cli) #---
		self.vet.editCPushButton.clicked.connect(self.edit_Cli)
		self.vet.deleteCPushButton.clicked.connect(self.remove_Cli)
		self.vet.clearCPushButton.clicked.connect(self.clear_Cli)
		self.vet.entryDPushButton.clicked.connect(self.register_Dog)
		self.vet.searchDLineEdit.returnPressed.connect(self.search_Dog)#---
		self.vet.uploadDPushButton.clicked.connect(self.upload_file)
		self.vet.editDPushButton.clicked.connect(self.edit_Dog)
		self.vet.deleteDPushButton.clicked.connect(self.remove_Dog)
		self.vet.clearDPushButton.clicked.connect(self.clear_Dog)
		self.connectToServer()
		self.vet.chatLineEdit.returnPressed.connect(self.issueRequest)
		self.socket.readyRead.connect(self.readFromServer)
		self.socket.disconnected.connect(self.serverHasStopped)
		self.connect(self.socket,
                     SIGNAL("error(QAbstractSocket::SocketError)"),
                     self.serverHasError)
		
#|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°
	# REGISTRO CLIENTES #

	def connect_Account(self):
		db = QSqlDatabase.addDatabase('QSQLITE')
		db.setDatabaseName('database.db')
		if db.open() == False:
			self.msg.information(self,"informativo","No se conecto la base de datos")

	def charge_Cli(self):
		try:
			query = "SELECT nombre FROM clientes"
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			while sql.next():
				self.vet.nameOwnerDComboBox.addItem(sql.value(0))
		except:
			self.msg.information(self,"informativo","Solicitud invalida")

	def register_Cli(self):
		name = self.vet.nameCLineEdit.text()
		lastN_1 = self.vet.lastname1CLineEdit.text()
		lastN_2 = self.vet.lastname2CLineEdit.text()
		address = self.vet.addressCLineEdit.text()
		cel = self.vet.celphoneCLineEdit.text()
		cp = self.vet.cpCLineEdit.text()
		email = self.vet.emailCLineEdit.text()
		phone = self.vet.phoneCLineEdit.text()
		self.vet.nameOwnerDComboBox.addItem(name)
		try:
			query = "INSERT INTO clientes(nombre,apellido1,apellido2,direccion,celular,cp,email,telefono) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(name,lastN_1,lastN_2,address,cel,cp,email,phone)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Agregado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameCLineEdit.clear()
			self.vet.lastname1CLineEdit.clear()
			self.vet.lastname2CLineEdit.clear()
			self.vet.addressCLineEdit.clear()
			self.vet.celphoneCLineEdit.clear()
			self.vet.cpCLineEdit.clear()
			self.vet.emailCLineEdit.clear()
			self.vet.phoneCLineEdit.clear()

	def search_Cli(self):
		search = self.vet.searchCLineEdit.text()
		try:
			query = "SELECT * FROM clientes WHERE id like '%{0}%' or nombre like '%{0}%' or apellido1 like '%{0}%' or apellido2 like '%{0}%' or direccion like '%{0}%' or celular like '%{0}%' or cp like '%{0}%' or email like '%{0}%' or telefono like '%{0}%' ".format(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0 
			self.vet.registerCTableWidget.clear()
			while sql.next():
				if self.vet.registerCTableWidget.rowCount() < sql.at()+1:		
					self.vet.registerCTableWidget.insertRow(sql.at()) # to compare sql.at()+1 with number of rows
				while j < 9:
					self.vet.registerCTableWidget.setItem(i,j,QTableWidgetItem(str(sql.value(j))))
					self.vet.nameCLineEdit.setText(sql.value(0))
					self.vet.lastname1CLineEdit.setText(sql.value(1))
					self.vet.lastname2CLineEdit.setText(sql.value(2))
					self.vet.addressCLineEdit.setText(sql.value(3))
					self.vet.celphoneCLineEdit.setText(sql.value(4))
					self.vet.cpCLineEdit.setText(sql.value(5))
					self.vet.emailCLineEdit.setText(sql.value(6))
					self.vet.phoneCLineEdit.setText(sql.value(7))
					j += 1
				j = 0
				i += 1
		except:
			self.msg.information(self,"informativo","Error en la consulta")	

	def edit_Cli(self):
		search = self.vet.searchCLineEdit.text()
		name = self.vet.nameCLineEdit.text()
		lastN_1= self.vet.lastname1CLineEdit.text()
		lastN_2= self.vet.lastname2CLineEdit.text()
		address= self.vet.addressCLineEdit.text()
		cel = self.vet.celphoneCLineEdit.text()
		cp = self.vet.cpCLineEdit.text()
		email = self.vet.emailCLineEdit.text()
		phone = self.vet.phoneCLineEdit.text()
		try:
			query = "UPDATE clientes SET nombre='%s', apellido1='%s', apellido2='%s', direccion='%s', celular='%s', cp='%s', email='%s', telefono='%s' WHERE id='%s'"%(name,lastN_1,lastN_2,address,cel,cp,email,phone,search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Editado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameCLineEdit.clear()
			self.vet.lastname1CLineEdit.clear()
			self.vet.lastname2CLineEdit.clear()
			self.vet.addressCLineEdit.clear()
			self.vet.celphoneCLineEdit.clear()
			self.vet.cpCLineEdit.clear()
			self.vet.emailCLineEdit.clear()
			self.vet.phoneCLineEdit.clear()
			self.vet.registerCTableWidget.clear()
			self.vet.searchCLineEdit.clear()

	def remove_Cli(self):
		search = self.vet.searchCLineEdit.text()
		try:
			query = "DELETE FROM clientes WHERE id='%s'"%(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Eliminado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameCLineEdit.clear()
			self.vet.lastname1CLineEdit.clear()
			self.vet.lastname2CLineEdit.clear()
			self.vet.addressCLineEdit.clear()
			self.vet.celphoneCLineEdit.clear()
			self.vet.cpCLineEdit.clear()
			self.vet.emailCLineEdit.clear()
			self.vet.phoneCLineEdit.clear()
			self.vet.registerCTableWidget.clear()
			self.vet.searchCLineEdit.clear()
			
	def clear_Cli(self):
		self.vet.nameCLineEdit.clear()
		self.vet.lastname1CLineEdit.clear()
		self.vet.lastname2CLineEdit.clear()
		self.vet.addressCLineEdit.clear()
		self.vet.celphoneCLineEdit.clear()
		self.vet.cpCLineEdit.clear()
		self.vet.emailCLineEdit.clear()
		self.vet.phoneCLineEdit.clear()
		self.vet.searchCLineEdit.clear()
		self.vet.registerCTableWidget.clear()
		
#|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°|||°°°
	# REGISTRO PERROS #

	def register_Dog(self):
		name = self.vet.nameDogDLineEdit.text()
		race = self.vet.raceDLineEdit.text()
		age = self.vet.ageDLineEdit.text()
		gender = self.vet.genderDLineEdit.text()
		nameOw = self.vet.nameOwnerDComboBox.currentText()
		try:
			query = "INSERT INTO perros(nombre,raza,edad,sexo,dueno,carpeta) values('%s','%s','%s','%s','%s','%s')"%(name,race,age,gender,nameOw,self.file)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Agregado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameDogDLineEdit.clear()
			self.vet.raceDLineEdit.clear()
			self.vet.ageDLineEdit.clear()
			self.vet.genderDLineEdit.clear()
			self.vet.file = ""
			self.vet.imageDLabel.clear()

	def charge_Dog(self):
		try:
			query = "SELECT nombrePerro FROM clientes"
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			while sql.next():
				self.vet.nameDogDComboBox.addItem(sql.value(0))
		except:
			self.msg.information(self,"informativo","Solicitud invalida")

	def upload_file(self):
		self.file = QFileDialog.getOpenFileName(self,'Open file','C:\\Users\\user\\Google Drive\\Sem. Ing. Software 2','Image files (*.jpg *.gif *.png)')
		self.vet.imageDLabel.setPixmap(QPixmap(self.file))

	def search_Dog(self):
		search = self.vet.searchDLineEdit.text()
		try:
			query = "SELECT * FROM perros WHERE nombre like '%{0}%' or raza like '%{0}%' or edad like '%{0}%' or sexo like '%{0}%' or dueno like '%{0}%' or id like '%{0}%' ".format(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0
			self.vet.registerDTableWidget.clear()
			self.vet.imageDLabel.clear()
			while sql.next():
				if self.vet.registerDTableWidget.rowCount() < sql.at()+1:		
					self.vet.registerDTableWidget.insertRow(sql.at())
				while j < 7:
					self.vet.registerDTableWidget.setItem(i,j,QTableWidgetItem(str(sql.value(j))))
					self.vet.nameDogDLineEdit.setText(sql.value(0))
					self.vet.raceDLineEdit.setText(sql.value(1))
					self.vet.ageDLineEdit.setText(sql.value(2))
					self.vet.genderDLineEdit.setText(sql.value(3))
					self.file = sql.value(6)
					self.vet.imageDLabel.setPixmap(QPixmap(self.file))
					j += 1
				j = 0
				i += 1
		except:
			self.msg.information(self,"informativo","Error en la consulta")

	def edit_Dog(self):
		search = self.vet.searchDLineEdit.text()
		name = self.vet.nameDogDLineEdit.text()
		race = self.vet.raceDLineEdit.text()
		age = self.vet.ageDLineEdit.text()
		gender = self.vet.genderDLineEdit.text()
		nameOw = self.vet.nameOwnerDComboBox.currentText()
		try:
			query   = "UPDATE perros SET nombre='%s', raza='%s', edad='%s', sexo='%s', dueno='%s', carpeta='%s' WHERE id='%s'"%(name,race,age,gender,nameOw,self.file,search)
			sql     = QSqlQuery()
			sql.prepare(query)
			state   = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Editado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameDogDLineEdit.clear()
			self.vet.raceDLineEdit.clear()
			self.vet.ageDLineEdit.clear()
			self.vet.genderDLineEdit.clear()
			self.vet.file = ""
			self.vet.imageDLabel.clear()
			self.vet.registerDTableWidget.clear()
			self.vet.searchDLineEdit.clear()


	def remove_Dog(self):
		search = self.vet.searchDLineEdit.text()
		try:
			query = "DELETE FROM perros WHERE id='%s'"%(search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Eliminado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.vet.nameDogDLineEdit.clear()
			self.vet.raceDLineEdit.clear()
			self.vet.ageDLineEdit.clear()
			self.vet.genderDLineEdit.clear()
			self.vet.file = ""
			self.vet.imageDLabel.clear()
			self.vet.registerDTableWidget.clear()
			self.vet.searchDLineEdit.clear()
			
	def clear_Dog(self):
		self.vet.nameDogDLineEdit.clear()
		self.vet.raceDLineEdit.clear()
		self.vet.ageDLineEdit.clear()
		self.vet.genderDLineEdit.clear()
		self.vet.file = ""
		self.vet.imageDLabel.clear()
		self.vet.registerDTableWidget.clear()
		self.vet.searchDLineEdit.clear()

	def connectToServer(self):
		self.socket.connectToHost("localhost", PORT)
	
	def issueRequest(self):
		self.request = QByteArray()
		stream = QDataStream(self.request, QIODevice.WriteOnly)
		stream.setVersion(QDataStream.Qt_4_2)
		stream.writeUInt32(0)
		stream.writeQString(self.vet.chatLineEdit.text())
		stream.device().seek(0)
		stream.writeUInt32(self.request.size() - SIZEOF_UINT32)
		self.socket.write(self.request)
		self.nextBlockSize = 0
		self.request = None
		self.vet.chatLineEdit.clear()
	
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
			self.vet.chatTextBrowser.append(textFromServer) # output
			self.nextBlockSize = 0

	def serverHasStopped(self):
		self.socket.close()
		self.connectButton.setEnabled(True)

	def serverHasError(self):
		self.vet.chatTextBrowser.append("Error: {}".format(
        				self.socket.errorString()))
		self.socket.close()



def main():
	app = QApplication(sys.argv)
	win_vet = Veterinary() 
	win_vet.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
