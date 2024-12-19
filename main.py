import sys
import math
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
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
        self.tombol_homeda.clicked.connect(self.go_to_home)
        self.tombol_home_m.clicked.connect(self.go_to_home)
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

        self.tombol_daya() #dipake di page_daya
        self.Da_ac.clicked.connect(self.clear_allDa)
        self.Da_c.clicked.connect(self.clearDa)
        self.Da_del.clicked.connect(self.deleteDa)
        self.convert_button_Daya.clicked.connect(self.konversi_daya)

        self.tombol_massa() #dipake di page_massa
        self.ac_m.clicked.connect(self.clear_allM)
        self.c_m.clicked.connect(self.clearM)
        self.del_m.clicked.connect(self.deleteM)
        self.konversi_m.clicked.connect(self.konversi_massa)

        self.tombol_kalkulator() # dipake di page_kalkulator
        self.SamaDengan.clicked.connect(self.hitung_hasil)
        self.tombol_homeK.clicked.connect(self.go_to_home)
        self.AC.clicked.connect(self.clearAllK)
        self.Delete.clicked.connect(self.DelK)
        self.Persen.clicked.connect(self.persen)
        self.Pangkat.clicked.connect(self.pangkat)
        self.Akar.clicked.connect(self.akar)
        self.Faktorial.clicked.connect(self.factorial)
        self.history_line.setReadOnly(True)
        self.history = []
        self.Input_Line.setAlignment(Qt.AlignRight)
        self.history_line.setAlignment(Qt.AlignRight)



    def navigate_to_page(self):
        selected_option = self.Opsimode.currentText()
        if selected_option == "Konversi Suhu":
            self.stackedWidget.setCurrentIndex(2)  # ke halaman suhu
        if selected_option == "Konversi Panjang":
            self.stackedWidget.setCurrentIndex(3) #ke halaman panjang
        if selected_option == "Konversi Data Digital":
            self.stackedWidget.setCurrentIndex(4) #ke halaman panjang
        if selected_option == "Konversi Daya":
            self.stackedWidget.setCurrentIndex(5) #ke halaman daya
        if selected_option == "Konversi Massa":
            self.stackedWidget.setCurrentIndex(6) #ke halaman daya
        if selected_option == "Kalkulator":
            self.stackedWidget.setCurrentIndex(1) #ke halaman daya
        if selected_option == "Kalkulator Scientific":
            self.stackedWidget.setCurrentIndex(7)  # ke halaman kalkulator semi-scientific

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







# ////////////////////////////////////////// halaman konversi daya ///////////////////////////////////////////////////////////////////////
    def tombol_daya(self):
        self.nomorDa_0.clicked.connect(lambda: self.masukin_inputDa("0"))
        self.nomorDa_1.clicked.connect(lambda: self.masukin_inputDa("1"))
        self.nomorDa_2.clicked.connect(lambda: self.masukin_inputDa("2"))
        self.nomorDa_3.clicked.connect(lambda: self.masukin_inputDa("3"))
        self.nomorDa_4.clicked.connect(lambda: self.masukin_inputDa("4"))
        self.nomorDa_5.clicked.connect(lambda: self.masukin_inputDa("5"))
        self.nomorDa_6.clicked.connect(lambda: self.masukin_inputDa("6"))
        self.nomorDa_7.clicked.connect(lambda: self.masukin_inputDa("7"))
        self.nomorDa_8.clicked.connect(lambda: self.masukin_inputDa("8"))
        self.nomorDa_9.clicked.connect(lambda: self.masukin_inputDa("9"))
    def clear_allDa(self):
        self.input_lineeditDa.clear()
        self.output_lineeditDa.clear()
    def clearDa(self):
        self.input_lineeditDa.setText("")
    def deleteDa(self):
        current_text = self.input_lineeditDa.text()
        self.input_lineeditDa.setText(current_text[:-1])


    def masukin_inputDa(self, value):
        current_text = self.input_lineeditDa.text()
        self.input_lineeditDa.setText(current_text + value)


    def konversi_daya(self):
        try:
            value = float(self.input_lineeditDa.text())
            input_unit = self.input_data_comboboxDa.currentText()
            output_unit = self.output_data_comboboxDa.currentText()

            # Conversion factors to Watts
            conversion_factors = {
                "W": 1,  # Watts
                "kW": 1000,  # Kilowatts
                "hp": 745.7,  # Horsepower
                "Btu/h": 0.293071,  # BTU per hour
                "ft-lb/s": 1.35582,  # Foot-pounds per second
                "J/s": 1  # Joules per second
            }

            # Convert to Watts
            value_in_watts = value * conversion_factors[input_unit]

            # Convert from Watts to the output unit
            converted_value = value_in_watts / conversion_factors[output_unit]
            self.output_lineeditDa.setText(str(converted_value))
        except ValueError:
            self.output_lineeditDa.setText("Invalid input")  # Handle invalid input

# //////////////////////////////////////// halaman konversi daya //////////////////////////////////////////////////////////////////////////














# ////////////////////////////////////// halaman konversi massa /////////////////////////////////////////////////////////////////////////////

    def tombol_massa(self):
        self.nomorm_0.clicked.connect(lambda: self.masukin_inputm("0"))
        self.nomorm_1.clicked.connect(lambda: self.masukin_inputm("1"))
        self.nomorm_2.clicked.connect(lambda: self.masukin_inputm("2"))
        self.nomorm_3.clicked.connect(lambda: self.masukin_inputm("3"))
        self.nomorm_4.clicked.connect(lambda: self.masukin_inputm("4"))
        self.nomorm_5.clicked.connect(lambda: self.masukin_inputm("5"))
        self.nomorm_6.clicked.connect(lambda: self.masukin_inputm("6"))
        self.nomorm_7.clicked.connect(lambda: self.masukin_inputm("7"))
        self.nomorm_8.clicked.connect(lambda: self.masukin_inputm("8"))
        self.nomorm_9.clicked.connect(lambda: self.masukin_inputm("9"))
        self.nomorm_titik.clicked.connect(lambda: self.masukin_inputm("."))
    def clear_allM(self):
        self.input_lineeditM.clear()
        self.output_lineeditM.clear()
    def clearM(self):
        self.input_lineeditM.setText("")
    def deleteM(self):
        current_text = self.input_lineeditM.text()
        self.input_lineeditM.setText(current_text[:-1])

    def masukin_inputm(self, value):
        current_text = self.input_lineeditM.text()
        self.input_lineeditM.setText(current_text + value)

    def konversi_massa(self):
        try:
            value = float(self.input_lineeditM.text())
            input_unit = self.input_data_comboboxM.currentText()
            output_unit = self.output_data_comboboxM.currentText()

            # Conversion factors relative to gram (g)
            conversion_massa = {
                "kg": 1000,  # 1 kg = 1000 g
                "hg": 100,  # 1 hg = 100 g
                "dag": 10,  # 1 dag = 10 g
                "g": 1,  # 1 g = 1 g
                "dg": 0.1,  # 1 dg = 0.1 g
                "cg": 0.01,  # 1 cg = 0.01 g
                "mg": 0.001,  # 1 mg = 0.001 g
            }

            # Convert input value to grams
            value_in_grams = value * conversion_massa[input_unit]

            # Convert from grams to the target unit
            converted_value = value_in_grams / conversion_massa[output_unit]

            # Display the result
            self.output_lineeditM.setText(str(converted_value))
        except ValueError:
            self.output_lineeditM.setText("Invalid input")  # Handle invalid input

# Handle invalid input
# //////////////////////////////////// halaman konversi massa ///////////////////////////////////////////////////////////////////////////////////////










# /////////////////////////////////// halaman kalkulator ////////////////////////////////////////////////////////////////////////////////////////////

    def tombol_kalkulator (self) :
        self.Nomor_0.clicked.connect(lambda: self.masukin_input_K("0"))
        self.Nomor_00.clicked.connect(lambda: self.masukin_input_K("00"))
        self.Nomor_000.clicked.connect(lambda: self.masukin_input_K("000"))
        self.Nomor_1.clicked.connect(lambda: self.masukin_input_K("1"))
        self.Nomor_2.clicked.connect(lambda: self.masukin_input_K("2"))
        self.Nomor_3.clicked.connect(lambda: self.masukin_input_K("3"))
        self.Nomor_4.clicked.connect(lambda: self.masukin_input_K("4"))
        self.Nomor_5.clicked.connect(lambda: self.masukin_input_K("5"))
        self.Nomor_6.clicked.connect(lambda: self.masukin_input_K("6"))
        self.Nomor7.clicked.connect(lambda: self.masukin_input_K("7"))
        self.Nomor8.clicked.connect(lambda: self.masukin_input_K("8"))
        self.Nomor9.clicked.connect(lambda: self.masukin_input_K("9"))
        self.Kali.clicked.connect(lambda: self.masukin_input_K("*"))
        self.Tambah.clicked.connect(lambda: self.masukin_input_K("+"))
        self.Bagi.clicked.connect(lambda: self.masukin_input_K("/"))
        self.Kurang.clicked.connect(lambda: self.masukin_input_K("-"))
        self.Koma.clicked.connect(lambda: self.masukin_input_K("."))

        self.Persen.clicked.connect(lambda: self.masukin_input_K("%"))
        self.Pangkat.clicked.connect(lambda: self.masukin_input_K("^"))
        self.Akar.clicked.connect(lambda: self.masukin_input_K("√"))
        self.Faktorial.clicked.connect(lambda: self.masukin_input_K("!"))

        self.history_line.setReadOnly(True)
        
        self.ekspresi = ""
        self.new_input = False

    def clearAllK (self) :
        self.Input_Line.clear()
        self.history_line.clear()
        self.ekspresi = ""

        self.history = []  # Kosongkan list history
        self.history_line.setText("")

    def DelK (self):
        current_text = self.Input_Line.text()
        self.Input_Line.setText(current_text[:-1])
        self.ekspresi = current_text[:-1]

    def Cleark(self):
        current_text = self.Input_Line.text()
        self.Input_Line.setText(current_text[:-1])
        self.ekspresi = current_text[:-1]

    def factorial(self) :
        value = (self.Input_Line.text())
        if value < 0:
            result = "Error: Negative factorial"
        elif value == 0:
            result = 1
        else:
            result = value * self.factorial(value - 1)
        self.Input_Line.setText(str(result))

    def akar(self, value: float) -> float:
        if value < 0:
            return "Error: Negative square root"
        return math.sqrt(value)

    def persen(self):
        try:
            value = float(self.Input_Line.text())
            result = value / 100
            self.Input_Line.setText(str(result))  # Asumsikan ada label output
        except ValueError:
            self.Input_Line.setText("Masukkan angka yang valid")

    def pangkat(self, base: float, exponent: float) -> float:
        return base ** exponent

    def masukin_input_K(self, value: str):
        if self.new_input:  # Jika input baru dimulai, reset ekspresi
            self.ekspresi = ""
            self.new_input = False  # Reset flag

        if value in "*+-/":
            if self.ekspresi and self.ekspresi[-1] in "*+-/":
                return
            elif not self.ekspresi:
                return

        self.ekspresi += value
        self.Input_Line.setText(self.ekspresi)


    def hitung_hasil(self):
        result = self.evaluate_expression(self.ekspresi)
        self.Input_Line.setText(result)
        self.ekspresi = result if "Error" not in result else ""
        self.new_input = True
        self.history.append(self.ekspresi)
        self.history_line.setText(self.ekspresi)
        try:
            # Replace special symbols with function calls
            expression = self.ekspresi.replace("√", "akar")
            expression = expression.replace("^", "pangkat")
            expression = expression.replace("!", "factorial")
            result = eval(expression)
            self.Input_Line.setText(str(result))
            self.ekspresi = str(result)  # Store result as new expression
            self.new_input = True
        except ZeroDivisionError:
            self.Input_Line.setText("Error: Division by zero")
        except Exception as e:
            self.Input_Line.setText(f"Error: {str(e)}")

    def evaluate_expression(self, expression: str) -> str:
        try:
            result = eval(expression)
            return str(result)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Error: Invalid input"












# ////////////////////////////////// halaman kalkulator /////////////////////////////////////////////////////////////////////////////////////////////



if __name__ == "__main__":
    app = QApplication([])
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())
