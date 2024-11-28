import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5 import QtWidgets, uic
from updated_calc import Ui_Dialog

class MainDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Inisialisasi UI
        self.ui.setupUi(self)  # Menyiapkan UI


        self.ui.submitpilihan.clicked.connect(self.navigate_to_page) # Set halaman pertama adalah page_welcome

    def navigate_to_page (self) :
        selected_option = self.ui.Opsimode.currentText()

        if selected_option == "Konversi Suhu" :
            self.ui.stackedWidget.setCurrentIndex(1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_dialog = MainDialog()
    main_dialog.show()
    sys.exit(app.exec_())