import sys , os
from admin import Ui_Admin
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class Admin(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.adm = Ui_Admin()
		self.adm.setupUi(self)
		self.msg = QMessageBox()
		self.adm.entryAPushButton.clicked.connect(self.register_Adm)
		self.adm.searchALineEdit.returnPressed.connect(self.search_Adm)
		self.adm.editAPushButton.clicked.connect(self.edit_Adm)
		self.adm.deleteAPushButton.clicked.connect(self.remove_Adm)
		self.adm.clearAPushButton.clicked.connect(self.clear_Adm)

	def register_Adm(self):
		name = self.adm.nameALineEdit.text()
		lastN_1 = self.adm.lastname1ALineEdit.text()
		lastN_2 = self.adm.lastname2ALineEdit.text()
		address = self.adm.addressALineEdit.text()
		nss = self.adm.nssALineEdit.text()
		idE = self.adm.idALineEdit.text()
		rfc = self.adm.rfcALineEdit.text()
		phone = self.adm.phoneALineEdit.text()
		org = self.adm.orgAComboBox.currentText()
		passwd = self.adm.passALineEdit.text()
		try:
			query = "INSERT INTO admin(nombre,apellido1,apellido2,direccion,nss,id,rfc,telefono,organizacion,password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,lastN_1,lastN_2,address,nss,idE,rfc,phone,org,passwd)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Agregado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
			self.adm.nameALineEdit.clear()
			self.adm.lastname1ALineEdit.clear()
			self.adm.lastname2ALineEdit.clear()
			self.adm.addressALineEdit.clear()
			self.adm.nssALineEdit.clear()
			self.adm.idALineEdit.clear()
			self.adm.rfcALineEdit.clear()
			self.adm.phoneALineEdit.clear()
			self.adm.passALineEdit.clear()

	def search_Adm(self):
		search = self.adm.searchALineEdit.text()
		try:
			query = "SELECT * FROM admin WHERE nombre='%s'"%search
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			i = 0
			j = 0
			while sql.next():
				if sql.value(0) == search:
					if self.adm.registerATableWidget.rowCount() == 0: 
						self.adm.registerATableWidget.insertRow(self.adm.registerATableWidget.rowCount())
					while j < 10:
						self.adm.registerATableWidget.setItem(i,j,QTableWidgetItem(sql.value(j)))
						self.adm.nameALineEdit.setText(sql.value(0))
						self.adm.lastname1ALineEdit.setText(sql.value(1))
						self.adm.lastname2ALineEdit.setText(sql.value(2))
						self.adm.addressALineEdit.setText(sql.value(3))
						self.adm.nssALineEdit.setText(sql.value(4))
						self.adm.idALineEdit.setText(sql.value(5))
						self.adm.rfcALineEdit.setText(sql.value(6))
						self.adm.phoneALineEdit.setText(sql.value(7))
						self.adm.passALineEdit.setText(sql.value(9))
						j += 1
					i += 1
				else:
					self.msg.information(self,"informativo","El valor no existe")
		except:
			self.msg.information(self,"informativo","Error en la consulta")

	def edit_Adm(self):
		search = self.adm.searchALineEdit.text()
		name = self.adm.nameALineEdit.text()
		lastN_1 = self.adm.lastname1ALineEdit.text()
		lastN_2 = self.adm.lastname2ALineEdit.text()
		address = self.adm.addressALineEdit.text()
		nss = self.adm.nssALineEdit.text()
		idE = self.adm.idALineEdit.text()
		rfc = self.adm.rfcALineEdit.text()
		phone = self.adm.phoneALineEdit.text()
		org = self.adm.orgAComboBox.currentText()
		passwd = self.adm.passALineEdit.text()
		try:
			query = "UPDATE admin SET nombre='%s', apellido1='%s', apellido2='%s', direccion='%s', nss='%s', id='%s', rfc='%s', telefono='%s', organizacion='%s', password='%s' WHERE nombre='%s'"%(name,lastN_1,lastN_2,address,nss,idE,rfc,phone,org,passwd,search)
			sql = QSqlQuery()
			sql.prepare(query)
			state = sql.exec_()
			if state:
				self.msg.information(self,"informativo","Editado exitosamente!")
		except:
			self.msg.information(self,"informativo","Error al ingresar")
		finally:
		 	self.adm.searchALineEdit.clear() 
		 	self.adm.nameALineEdit.clear()
		 	self.adm.lastname1ALineEdit.clear()
		 	self.adm.lastname2ALineEdit.clear()
		 	self.adm.addressALineEdit.clear()
		 	self.adm.nssALineEdit.clear()
		 	self.adm.idALineEdit.clear()
		 	self.adm.rfcALineEdit.clear()
 			self.adm.phoneALineEdit.clear()
 			self.adm.orgAComboBox.clear()
	 		self.adm.passALineEdit.clear()
	 		self.adm.registerATableWidget.clear()

	def remove_Adm(self):
	 	search = self.adm.searchALineEdit.text()
	 	try:
	 		query = "DELETE FROM admin WHERE nombre='%s'"%(search)
	 		sql = QSqlQuery()
	 		sql.prepare(query)
	 		state = sql.exec_()
	 		if state:
	 			self.msg.information(self,"informativo","Eliminado exitosamente!")
	 	except:
	 		self.msg.information(self,"informativo","Error al ingresar")
	 	finally:
		 	self.adm.searchALineEdit.clear() 
		 	self.adm.nameALineEdit.clear()
		 	self.adm.lastname1ALineEdit.clear()
		 	self.adm.lastname2ALineEdit.clear()
		 	self.adm.addressALineEdit.clear()
		 	self.adm.nssALineEdit.clear()
		 	self.adm.idALineEdit.clear()
		 	self.adm.rfcALineEdit.clear()
 			self.adm.phoneALineEdit.clear()
 			self.adm.orgAComboBox.clear()
	 		self.adm.passALineEdit.clear()
	 		self.adm.registerATableWidget.clear()
	 		
	def clear_Adm(self):
		self.adm.searchALineEdit.clear() 
		self.adm.nameALineEdit.clear()
		self.adm.lastname1ALineEdit.clear()
		self.adm.lastname2ALineEdit.clear()
		self.adm.addressALineEdit.clear()
		self.adm.nssALineEdit.clear()
		self.adm.idALineEdit.clear()
		self.adm.rfcALineEdit.clear()
		self.adm.phoneALineEdit.clear()
		self.adm.orgAComboBox.clear()
		self.adm.passALineEdit.clear()
		self.adm.registerATableWidget.clear()




def main():
	app = QApplication(sys.argv)
	win_adm = Admin() 
	win_adm.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
