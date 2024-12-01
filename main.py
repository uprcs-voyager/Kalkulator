import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5 import QtWidgets, uic
from updated_calc import Ui_Dialog

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("updated_calc.ui", self)  # Load the main UI

        # Initial setup
        self.stackedWidget.setCurrentIndex(0)  # mulai di page welcome
        self.submitpilihan.clicked.connect(self.navigate_to_page)
        self.tombol_home.clicked.connect(self.go_to_home)
        self.tombol_konversi.clicked.connect(self.konversi_suhu)

    def navigate_to_page(self):
        selected_option = self.Opsimode.currentText()
        if selected_option == "Konversi Suhu":
            self.stackedWidget.setCurrentIndex(1)  # ke halaman suhu

    def go_to_home(self):
        self.stackedWidget.setCurrentIndex(0)  # kembali ke halaman rumah



    # ///////////////////////////////halaman suhu////////////////////////////////////
    def konversi_suhu(self):
        try:
            # ambil info value
            value = float(self.input_kanan.text())
            dari_satuan = self.combo_input.currentText()
            ke_satuan = self.combo_output.currentText()

            # ke proses
            hasil = self.proses_konversi(value, dari_satuan, ke_satuan)
            self.output_kiri.setText(str(round(hasil, 2)))
        except ValueError:
            self.output_kiri.setText("Invalid input")  # Handle non-numeric input

    @staticmethod
    def proses_konversi(value, dari_satuan, ke_satuan):

        if dari_satuan == ke_satuan:
            return value

        # ke celciuus
        if dari_satuan == "Fahrenheit":
            value = (value - 32) * 5 / 9
        elif dari_satuan == "Kelvin":
            value = value - 273.15

        # celcius ke konversi target
        if ke_satuan == "Fahrenheit":
            return (value * 9 / 5) + 32
        elif ke_satuan == "Kelvin":
            return value + 273.15
        return value

#     ///////////////////////halaman suhu/////////////////////////////////////////////////////////

if __name__ == "__main__":
    app = QApplication([])
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())
