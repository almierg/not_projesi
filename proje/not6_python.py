import sys
import os
from PyQt5.QtWidgets import qApp, QWidget, QApplication, QTextEdit, QLabel, QPushButton, QFileDialog,  QMainWindow, QFontDialog, QColorDialog, QDialog, QMessageBox, QTextEdit, QFormLayout
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

class Ui_Ui_nott(object):
    def tema_dialog(self):
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Tema Ayarla")
        arka_label = QLabel("Arka Plan: ", self.dialog)
        self.arkarenk_label = QLabel("", self.dialog)
        ön_label = QLabel("Yazı Rengi: ", self.dialog)
        self.önrenk_label = QLabel("", self.dialog)
        gözAt_butonu = QPushButton("Göz At", self.dialog)
        gözAt_butonu.clicked.connect(self.ayarla)
        self.tamam_butonu = QPushButton("Tamam", self.dialog)
        self.tamam_butonu.clicked.connect(self.tamam)
        self.tamam_butonu.setEnabled(False)

        form = QFormLayout(self.dialog)
        form.addRow(arka_label, self.arkarenk_label)
        form.addRow(ön_label, self.önrenk_label)
        form.addRow(gözAt_butonu, self.tamam_butonu)

        self.dialog.exec()

    def ayarla(self):

        arkaDialog = QColorDialog()
        arkaRenk = arkaDialog.getColor(self.textEdit.textBackgroundColor())
        self.arkaRenk = arkaRenk.name()
        self.arkarenk_label.setText(str(self.arkaRenk))
        arkaDialog.close()

        önDialog = QColorDialog()
        önRenk = önDialog.getColor(self.textEdit.textBackgroundColor())
        self.önRenk = önRenk.name()
        self.önrenk_label.setText(str(self.önRenk))
        self.tamam_butonu.setEnabled(True)

    def tamam(self):
        try:
            self.textEdit.setStyleSheet("background-color: " + self.arkaRenk + ";color: " + self.önRenk)
            self.dialog.close()

        except Exception:
            # noinspection PyTypeChecker
            QMessageBox.warning(self, "Uyarı", "İki Renk Seçmediniz!")

    def font(self):
        font, durum = QFontDialog.getFont()
        if durum:
            self.textEdit.setFont(font)

    def temizle(self):
        self.textEdit.clear()

    def ac(self):
        dosya_yolu = tk.filedialog.askopenfilename()
        dosya = open(dosya_yolu, "r")
        self.textEdit.setText(dosya.read())

    def kaydet(self):
        dosya_yolu = tk.filedialog.asksaveasfilename()
        dosya = open(dosya_yolu, "w")
        dosya.write(self.textEdit.toPlainText())

    def cikis(self):
        qApp.quit()

    def setupUi(self, Ui_nott):


        Ui_nott.setObjectName("Ui_nott")
        Ui_nott.resize(818, 679)
        Ui_nott.setMinimumSize(QtCore.QSize(818, 679))
        Ui_nott.setMaximumSize(QtCore.QSize(818, 679))
        Ui_nott.setStyleSheet("background-color: rgb(255, 250, 221);")
        self.centralwidget = QtWidgets.QWidget(Ui_nott)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.ac)

        self.pushButton.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushButton.setStyleSheet("background-color: rgb(197, 255, 231);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.kaydet)

        self.pushButton_2.setGeometry(QtCore.QRect(310,10,93,28))
        self.pushButton_2.setStyleSheet("background-color: rgb(196, 255, 231);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.clicked.connect(self.temizle)

        self.pushButton_3.setGeometry(QtCore.QRect(110, 10, 93, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(196, 255, 231);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.clicked.connect(self.cikis)
        self.pushButton_4.setGeometry(QtCore.QRect(510,10,93,28))
        self.pushButton_4.setStyleSheet("background-color: rgb(196, 255, 231);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.clicked.connect(self.font)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 10, 93, 28))
        self.pushButton_5.setStyleSheet("background-color: rgb(196, 255, 231);")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.clicked.connect(self.tema_dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(410,10,93,28))
        self.pushButton_6.setStyleSheet("background-color: rgb(196, 255, 231);")
        self.pushButton_6.setObjectName("pushButton_6")


        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 46, 801, 601))
        self.textEdit.setStyleSheet("background-color: rgb(239, 239, 239);\n""background-color: rgb(248, 248, 248);")
        self.textEdit.setObjectName("textEdit")

        Ui_nott.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Ui_nott)
        self.statusbar.setObjectName("statusbar")
        Ui_nott.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_nott)
        QtCore.QMetaObject.connectSlotsByName(Ui_nott)


    def retranslateUi(self, Ui_nott):
        _translate = QtCore.QCoreApplication.translate
        Ui_nott.setWindowTitle(_translate("Ui_nott", "aszm"))
        self.pushButton.setText(_translate("Ui_nott", "Dosya Aç"))
        self.pushButton_2.setText(_translate("Ui_nott", "Dosya Kaydet"))
        self.pushButton_3.setText(_translate("Ui_nott", "Temizle"))
        self.pushButton_4.setText(_translate("Ui_nott", "Çıkış"))
        self.pushButton_5.setText(_translate("Ui_nott", "Font"))
        self.pushButton_6.setText(_translate("Ui_nott", "Tema"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Ui_nott = QtWidgets.QMainWindow()
    ui = Ui_Ui_nott()
    ui.setupUi(Ui_nott)
    Ui_nott.show()
    sys.exit(app.exec_())
