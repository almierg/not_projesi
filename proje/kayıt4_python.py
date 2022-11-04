from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql

class Ui_kayit(object):
    def baglanti_yap(self):
        baglanti = sql.connect("hesap_kayitlari.db")
        self.cursor = baglanti.cursor()
        self.cursor.execute("CREATE TABLE If not exists uyeler (kuladi TEXT,sifre TEXT)")
        baglanti.commit()

    def kayit_2(self):
        adi = self.lineEdit.text()
        par = self.lineEdit_2.text()

        con = sql.connect('hesap_kayitlari.db')
        cur = con.cursor()
        cur.execute("CREATE TABLE If not exists uyeler(kuladi TEXT,sifre TEXT)")
        cur.execute("INSERT INTO uyeler VALUES(?,?)", (adi, par))

        con.commit()
        con.close()


    def setupUi(self, kayit):
        self.baglanti_yap()

        kayit.setObjectName("kayit")
        kayit.resize(600, 500)
        kayit.setMinimumSize(QtCore.QSize(600, 500))
        kayit.setStyleSheet("background-color: rgb(255, 253, 176);")
        self.centralwidget = QtWidgets.QWidget(kayit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 150, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200,270,11,20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 310, 111, 31))
        self.pushButton.clicked.connect(self.kayit_2)


        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(239, 239, 239);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 160, 113, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.lineEdit.setObjectName("lineEdit")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 220, 113, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")



        kayit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(kayit)
        self.statusbar.setObjectName("statusbar")
        kayit.setStatusBar(self.statusbar)

        self.retranslateUi(kayit)
        QtCore.QMetaObject.connectSlotsByName(kayit)

    def retranslateUi(self, kayit):
        _translate = QtCore.QCoreApplication.translate
        kayit.setWindowTitle(_translate("kayit", "kayıtool"))
        self.label.setText(_translate("kayit", "Kullanıcı adı:"))
        self.label_2.setText(_translate("kayit", "Şifre:"))
        self.pushButton.setText(_translate("kayit", "Kayıt Ol"))
        self.label_3.setText(_translate("kayit",""))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kayit_2 = QtWidgets.QMainWindow()
    ui = Ui_kayit()
    ui.setupUi(kayit_2)
    kayit_2.show()
    sys.exit(app.exec_())
