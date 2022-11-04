import os
from PyQt5 import QtCore, QtGui, QtWidgets
from not6_python import Ui_Ui_nott
from kayıt4_python import Ui_kayit
import webbrowser
import sqlite3

class Ui_MainWindow(object):
    def baglanti_yap(self):
        baglanti = sqlite3.connect("hesap_kayitlari.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists uyeler (kuladi TEXT,sifre TEXT)")
        baglanti.commit()

    def onay(self):
        adi = self.lineEdit.text()
        par = self.lineEdit_2.text()

        self.cursor.execute("SELECT*FROM uyeler where kuladi=? and sifre=?", (adi, par))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.label_4.setText("Böyle bir kullanıcı yok\n Tekrar deneyin")
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Ui_nott()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.hide()

    def hesap(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_kayit()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def link(self):
        webbrowser.open('https://www.instagram.com/aalmila_ergin', new=2)

    def link2(self):
        webbrowser.open('www.linkedin.com/in/almilaergin02', new=2)

    def setupUi(self, MainWindow):

        self.baglanti_yap()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(818, 679)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(818, 679))
        MainWindow.setMaximumSize(QtCore.QSize(818, 679))
        MainWindow.setStyleSheet("background-color: rgb(162, 255, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.onay)

        self.pushButton.setGeometry(QtCore.QRect(360, 440, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 310, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 370, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 300, 171, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 370, 171, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(0, 580, 221, 41))
        self.commandLinkButton.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton.clicked.connect(self.link2)

        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(0, 620, 291, 48))
        self.commandLinkButton_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_2.clicked.connect(self.link)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 301, 131))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(252, 255, 192);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.hesap)

        self.pushButton_2.setGeometry(QtCore.QRect(360, 490, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 410, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(162, 255, 168);")
         #self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "aszm"))
        self.pushButton.setText(_translate("MainWindow", "Giriş Yap"))
        self.label.setText(_translate("MainWindow", "Kullanıcı adı:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.commandLinkButton.setText(_translate("MainWindow", "Linkedln: almilaergin02"))
        self.commandLinkButton_2.setText(_translate("MainWindow", "İnstagram: aalmila_ergin"))
        self.label_3.setText(_translate("MainWindow", "NO-OT"))
        self.pushButton_2.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_4.setText(_translate("MainWindow", ""))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
