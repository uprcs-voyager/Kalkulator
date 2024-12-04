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
        self.tombol_homep.clicked.connect(self.go_to_home)
        self.tombol_homeD.clicked.connect(self.go_to_home)
        self.tombol_konversi_suhu.clicked.connect(self.konversi_suhu)



        self.tombolsuhu() #dipake di page_suhu
        self.push_ac.clicked.connect(self.clear_all)
        self.push_c.clicked.connect(self.clear)
        self.push_del.clicked.connect(self.delete)


        self.tombol_panjang() #dipake di page_panjang
        self.convert_button_panjang.clicked.connect(self.konversi_panjang)
        self.p_ac.clicked.connect(self.clear_allP)
        self.p_c.clicked.connect(self.clearP)
        self.p_del.clicked.connect(self.deleteP)

        self.tombol_digital() #dipake di page_datadigital
        self.convert_button_Digital.clicked.connect(self.konversi_data_digital)
        self.acD.clicked.connect(self.clear_allD)
        self.cD.clicked.connect(self.delete_lastD)
        self.deletD.clicked.connect(self.clear_lastD)



    def navigate_to_page(self):
        selected_option = self.Opsimode.currentText()
        if selected_option == "Konversi Suhu":
            self.stackedWidget.setCurrentIndex(1)  # ke halaman suhu
        if selected_option == "Konversi Panjang":
            self.stackedWidget.setCurrentIndex(2) #ke halaman panjang
        if selected_option == "Konversi Data Digital":
            self.stackedWidget.setCurrentIndex(3) #ke halaman panjang

    def go_to_home(self):
        self.stackedWidget.setCurrentIndex(0)  # kembali ke halaman rumah




    # ///////////////////////////////halaman suhu////////////////////////////////////
    def tombolsuhu(self):

        self.nomor_0.clicked.connect(lambda: self.masukin_input("0"))
        self.nomor_1.clicked.connect(lambda: self.masukin_input("1"))
        self.nomor_2.clicked.connect(lambda: self.masukin_input("2"))
        self.nomor_3.clicked.connect(lambda: self.masukin_input("3"))
        self.nomor_4.clicked.connect(lambda: self.masukin_input("4"))
        self.nomor_5.clicked.connect(lambda: self.masukin_input("5"))
        self.nomor_6.clicked.connect(lambda: self.masukin_input("6"))
        self.nomor_7.clicked.connect(lambda: self.masukin_input("7"))
        self.nomor_8.clicked.connect(lambda: self.masukin_input("8"))
        self.nomor_9.clicked.connect(lambda: self.masukin_input("9"))
    def clear_all(self):
        self.InputKanan.clear()
        self.output_kiri.clear()
    def clear(self):
        self.InputKanan.setText("")
    def delete(self):
        current_text = self.InputKanan.text()
        self.InputKanan.setText(current_text[:-1])
    def masukin_input(self, value):
        current_text = self.InputKanan.text()
        self.InputKanan.setText(current_text + value)
    def konversi_suhu(self):
        try:
            # ambil info value
            value = float(self.InputKanan.text())
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





# //////////////////////////////////////halaman panjang//////////////////////////////////////////////

    def tombol_panjang(self):
        self.nomorp_0.clicked.connect(lambda: self.masukin_inputp("0"))
        self.nomorp_1.clicked.connect(lambda: self.masukin_inputp("1"))
        self.nomorp_2.clicked.connect(lambda: self.masukin_inputp("2"))
        self.nomorp_3.clicked.connect(lambda: self.masukin_inputp("3"))
        self.nomorp_4.clicked.connect(lambda: self.masukin_inputp("4"))
        self.nomorp_5.clicked.connect(lambda: self.masukin_inputp("5"))
        self.nomorp_6.clicked.connect(lambda: self.masukin_inputp("6"))
        self.nomorp_7.clicked.connect(lambda: self.masukin_inputp("7"))
        self.nomorp_8.clicked.connect(lambda: self.masukin_inputp("8"))
        self.nomorp_9.clicked.connect(lambda: self.masukin_inputp("9"))

    def masukin_inputp(self, value):
        current_text = self.input_lineedit.text()
        self.input_lineedit.setText(current_text + value)

    def clear_allP(self):
        self.input_lineedit.clear()
        self.output_lineedit.clear()
    def clearP(self):
        self.input_lineedit.setText("")
    def deleteP(self):
        current_text = self.input_lineedit.text()
        self.input_lineedit.setText(current_text[:-1])

    def konversi_panjang (self) :
        try:
            value = float(self.input_lineedit.text())
            input_unit = self.input_unit_combobox.currentText()
            output_unit = self.output_unit_combobox.currentText()

            # Conversion factors
            conversion_factors = {
                "KM": 1000,
                "HM": 100,
                "DAM": 10,
                "M": 1,
                "DM": 0.1,
                "CM": 0.01,
                "MM": 0.001,
                "inch": 0.0254,
                "foot": 0.3048,
                "yard": 0.9144,
                "nm": 1e-9,
                "nmi": 1.852,
            }

            # Convert to meters
            value_in_meters = value * conversion_factors[input_unit]

            # Convert from meters to the output unit
            converted_value = value_in_meters / conversion_factors[output_unit]
            self.output_lineedit.setText(str(converted_value))
        except ValueError:
            self.output_lineedit.setText("Invalid input")  # Handle invalid input
# //////////////////////////////////halaman panjang/////////////////////////////////////////////////////////





# ////////////////////////////////halaman konversi data digital//////////////////////////////////
    def tombol_digital(self):
        self.nomorD_0.clicked.connect(lambda: self.masukin_inputD("0"))
        self.nomorD_1.clicked.connect(lambda: self.masukin_inputD("1"))
        self.nomorD_2.clicked.connect(lambda: self.masukin_inputD("2"))
        self.nomorD_3.clicked.connect(lambda: self.masukin_inputD("3"))
        self.nomorD_4.clicked.connect(lambda: self.masukin_inputD("4"))
        self.nomorD_5.clicked.connect(lambda: self.masukin_inputD("5"))
        self.nomorD_6.clicked.connect(lambda: self.masukin_inputD("6"))
        self.nomorD_7.clicked.connect(lambda: self.masukin_inputD("7"))
        self.nomorD_8.clicked.connect(lambda: self.masukin_inputD("8"))
        self.nomorD_9.clicked.connect(lambda: self.masukin_inputD("9"))

    def masukin_inputD(self, value):
        current_text = self.input_lineeditD.text()
        self.input_lineeditD.setText(current_text + value)

    def clear_allD(self):
        self.input_lineeditD.clear()
        self.output_lineeditD.clear()
    def clear_lastD(self):
        current_text = self.input_lineeditD.text()
        self.input_lineeditD.setText(current_text[:-1])
    def delete_lastD(self):
        self.input_lineeditD.setText("")

    def konversi_data_digital(self):
        try:
            value = float(self.input_lineeditD.text())
            input_unit = self.input_data_comboboxD.currentText()
            output_unit = self.output_data_comboboxD.currentText()

            # Conversion factors for digital data
            conversion_factors = {
                'b': 1,  # bit
                'B': 8,  # byte 'Kib': 1024,  # kibibit
                'kb': 1000,  # kilobit
                'Kib': 1024,  # kibibit
                'KiB': 1024 * 8,  # kibibyte
                'kB': 1000 * 8,  # kilobyte
                'Mib': 1024 * 1024,  # mebibit
                'Mb': 1000 * 1000,  # megabit
                'MiB': 1024 * 1024 * 8,  # mebibyte
                'MB': 1000 * 1000 * 8,  # megabyte
                'Gib': 1024 * 1024 * 1024,  # gibibit
                'Gb': 1000 * 1000 * 1000,  # gigabit
                'GiB': 1024 * 1024 * 1024 * 8,  # gibibyte
                'GB': 1000 * 1000 * 1000 * 8,  # gigabyte
                'Tib': 1024 * 1024 * 1024 * 1024,  # tebibit
                'Tb': 1000 * 1000 * 1000 * 1000,  # terabit
                'TiB': 1024 * 1024 * 1024 * 1024 * 8,  # tebibyte
                'TB': 1000 * 1000 * 1000 * 1000 * 8,  # terabyte
                'Pib': 1024 * 1024 * 1024 * 1024 * 1024,  # pebibit
                'Pb': 1000 * 1000 * 1000 * 1000 * 1000,  # petabit
                'PiB': 1024 * 1024 * 1024 * 1024 * 1024 * 8,  # pebibyte
                'PB': 1000 * 1000 * 1000 * 1000 * 1000 * 8,  # petabyte
            }

            # Convert to bits
            value_in_bits = value * conversion_factors[input_unit]

            # Convert from bits to the output unit
            converted_value = value_in_bits / conversion_factors[output_unit]
            self.output_lineeditD.setText(str(converted_value))
        except ValueError:
            self.output_lineeditD.setText("Invalid input")  # Handle invalid input

# /////////////////////////////////////////// halaman konversi data digital /////////////////////////////////////////////////////////////
        





if __name__ == "__main__":
    app = QApplication([])
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())
