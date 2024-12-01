import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5 import QtWidgets, uic
from updated_calc import Ui_Dialog

class MainDialog(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("updated_calc.ui", self)


        self.submitpilihan.clicked.connect(self.navigate_to_page) # Set halaman pertama adalah page_welcome
        self.tombol_home.clicked.connect(self.go_to_home)

    def navigate_to_page (self) :
        selected_option = self.Opsimode.currentText()

        if selected_option == "Konversi Suhu" :
            self.stackedWidget.setCurrentIndex(1)

    def go_to_home (self):
        self.stackedWidget.setCurrentIndex(0)

# aritmatika page_suhu
    def konversi_suhu (self, suhu, selected_konversi):
        if selected_konversi == "Fahrenheit  |  Celcius" :
            return (suhu*9/5) + 32

# tombol page_suhu
    def tombol_angka_klik(self, angka):
        current_text = self.input_kanan.text()
        new_text = current_text + str(angka)
        self.input_kanan.setText(new_text)








class MainWindow(QMainWindow) :
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication([])
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())