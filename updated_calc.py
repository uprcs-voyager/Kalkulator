# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updated_calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(497, 697)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 499, 699))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_welcome = QtWidgets.QWidget()
        self.page_welcome.setStyleSheet("QWidget#page_welcome{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.102, x2:1, y2:1, stop:0 rgba(205, 165, 255, 255), stop:0.675393 rgba(156, 229, 219, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.page_welcome.setObjectName("page_welcome")
        self.welcome = QtWidgets.QLabel(self.page_welcome)
        self.welcome.setGeometry(QtCore.QRect(67, 135, 391, 81))
        self.welcome.setStyleSheet("font: 63 30pt \"Bahnschrift SemiBold\"; color:rgb(31, 86, 146)")
        self.welcome.setObjectName("welcome")
        self.welcome2 = QtWidgets.QLabel(self.page_welcome)
        self.welcome2.setGeometry(QtCore.QRect(90, 210, 321, 31))
        self.welcome2.setStyleSheet("font: 63 14pt \"Bahnschrift SemiBold\"; color:rgb(31, 86, 146)")
        self.welcome2.setObjectName("welcome2")
        self.Opsimode = QtWidgets.QComboBox(self.page_welcome)
        self.Opsimode.setGeometry(QtCore.QRect(120, 334, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Opsimode.setFont(font)
        self.Opsimode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Opsimode.setStyleSheet("")
        self.Opsimode.setObjectName("Opsimode")
        self.Opsimode.addItem("")
        self.Opsimode.addItem("")
        self.Opsimode.addItem("")
        self.Opsimode.addItem("")
        self.Opsimode.addItem("")
        self.Opsimode.addItem("")
        self.submitpilihan = QtWidgets.QPushButton(self.page_welcome)
        self.submitpilihan.setGeometry(QtCore.QRect(207, 476, 93, 28))
        self.submitpilihan.setObjectName("submitpilihan")
        self.stackedWidget.addWidget(self.page_welcome)
        self.page_suhu = QtWidgets.QWidget()
        self.page_suhu.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.page_suhu.setObjectName("page_suhu")
        self.pushButton = QtWidgets.QPushButton(self.page_suhu)
        self.pushButton.setGeometry(QtCore.QRect(0, 638, 498, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.nomor_1 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_1.setGeometry(QtCore.QRect(1, 570, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_1.setFont(font)
        self.nomor_1.setObjectName("nomor_1")
        self.nomor_2 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_2.setGeometry(QtCore.QRect(169, 570, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_2.setFont(font)
        self.nomor_2.setObjectName("nomor_2")
        self.nomor_3 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_3.setGeometry(QtCore.QRect(337, 570, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_3.setFont(font)
        self.nomor_3.setObjectName("nomor_3")
        self.nomor_5 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_5.setGeometry(QtCore.QRect(168, 490, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_5.setFont(font)
        self.nomor_5.setObjectName("nomor_5")
        self.nomor_4 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_4.setGeometry(QtCore.QRect(0, 490, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_4.setFont(font)
        self.nomor_4.setObjectName("nomor_4")
        self.nomor_6 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_6.setGeometry(QtCore.QRect(336, 490, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_6.setFont(font)
        self.nomor_6.setObjectName("nomor_6")
        self.nomor_9 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_9.setGeometry(QtCore.QRect(336, 410, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_9.setFont(font)
        self.nomor_9.setObjectName("nomor_9")
        self.nomor_8 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_8.setGeometry(QtCore.QRect(168, 410, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_8.setFont(font)
        self.nomor_8.setObjectName("nomor_8")
        self.nomor_7 = QtWidgets.QPushButton(self.page_suhu)
        self.nomor_7.setGeometry(QtCore.QRect(0, 410, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nomor_7.setFont(font)
        self.nomor_7.setObjectName("nomor_7")
        self.push_c = QtWidgets.QPushButton(self.page_suhu)
        self.push_c.setGeometry(QtCore.QRect(168, 330, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push_c.setFont(font)
        self.push_c.setObjectName("push_c")
        self.push_ac = QtWidgets.QPushButton(self.page_suhu)
        self.push_ac.setGeometry(QtCore.QRect(0, 330, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push_ac.setFont(font)
        self.push_ac.setObjectName("push_ac")
        self.push_del = QtWidgets.QPushButton(self.page_suhu)
        self.push_del.setGeometry(QtCore.QRect(336, 330, 161, 73))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push_del.setFont(font)
        self.push_del.setObjectName("push_del")
        self.frame = QtWidgets.QFrame(self.page_suhu)
        self.frame.setGeometry(QtCore.QRect(240, 140, 16, 71))
        self.frame.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(9)
        self.frame.setObjectName("frame")
        self.suhu_kiri = QtWidgets.QComboBox(self.page_suhu)
        self.suhu_kiri.setGeometry(QtCore.QRect(80, 240, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.suhu_kiri.setFont(font)
        self.suhu_kiri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.suhu_kiri.setStyleSheet("QComboBox#suhu_kiri {\n"
"border: none;\n"
"}")
        self.suhu_kiri.setObjectName("suhu_kiri")
        self.suhu_kiri.addItem("")
        self.suhu_kiri.addItem("")
        self.suhu_kiri.addItem("")
        self.suhu_kiri.addItem("")
        self.tombol_home = QtWidgets.QPushButton(self.page_suhu)
        self.tombol_home.setGeometry(QtCore.QRect(380, 10, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tombol_home.setFont(font)
        self.tombol_home.setObjectName("tombol_home")
        self.inputt_kanan = QtWidgets.QLineEdit(self.page_suhu)
        self.inputt_kanan.setGeometry(QtCore.QRect(280, 120, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.inputt_kanan.setFont(font)
        self.inputt_kanan.setAlignment(QtCore.Qt.AlignCenter)
        self.inputt_kanan.setObjectName("inputt_kanan")
        self.input_kiri = QtWidgets.QLineEdit(self.page_suhu)
        self.input_kiri.setGeometry(QtCore.QRect(30, 120, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.input_kiri.setFont(font)
        self.input_kiri.setAlignment(QtCore.Qt.AlignCenter)
        self.input_kiri.setReadOnly(True)
        self.input_kiri.setObjectName("input_kiri")
        self.stackedWidget.addWidget(self.page_suhu)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "Selamat Datang"))
        self.welcome2.setText(_translate("Dialog", "Silahkan pilih mode kalkulator"))
        self.Opsimode.setItemText(0, _translate("Dialog", "Kalkulator sederhana"))
        self.Opsimode.setItemText(1, _translate("Dialog", "Konversi Suhu"))
        self.Opsimode.setItemText(2, _translate("Dialog", "Konversi Panjang"))
        self.Opsimode.setItemText(3, _translate("Dialog", "Konversi Massa"))
        self.Opsimode.setItemText(4, _translate("Dialog", "Konversi Waktu"))
        self.Opsimode.setItemText(5, _translate("Dialog", "Konversi kecepatan"))
        self.submitpilihan.setText(_translate("Dialog", "Pilih"))
        self.pushButton.setText(_translate("Dialog", "0"))
        self.nomor_1.setText(_translate("Dialog", "1"))
        self.nomor_2.setText(_translate("Dialog", "2"))
        self.nomor_3.setText(_translate("Dialog", "3"))
        self.nomor_5.setText(_translate("Dialog", "5"))
        self.nomor_4.setText(_translate("Dialog", "4"))
        self.nomor_6.setText(_translate("Dialog", "6"))
        self.nomor_9.setText(_translate("Dialog", "9"))
        self.nomor_8.setText(_translate("Dialog", "8"))
        self.nomor_7.setText(_translate("Dialog", "7"))
        self.push_c.setText(_translate("Dialog", "C"))
        self.push_ac.setText(_translate("Dialog", "AC"))
        self.push_del.setText(_translate("Dialog", "Del"))
        self.suhu_kiri.setItemText(0, _translate("Dialog", "Fahrenheit  |  Celcius"))
        self.suhu_kiri.setItemText(1, _translate("Dialog", "Celcius       |  Fahrenheit"))
        self.suhu_kiri.setItemText(2, _translate("Dialog", "Celcius       |  Kelvin"))
        self.suhu_kiri.setItemText(3, _translate("Dialog", "Kelvin         |  Celcius"))
        self.tombol_home.setText(_translate("Dialog", "Home"))
