from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from ui_main import Ui_MainWindow
from cep_Api import postal
import sys


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CRM Santa Maria - Customer Relationship Management - Version 1.0.2.4")
        appIcon = QIcon(u"")  # Configuração do Favicon
        self.setWindowIcon(appIcon)

        ###############################################################################################
        # PREENCHER AUTOMATICAMENTE OS DADOS DO CEP
        self.txt_cep_pesquisa.editingFinished.connect(self.consulta_cep)
        ###############################################################################################

    def consulta_cep(self):

        campos = postal(self.txt_cep_pesquisa.text())

        self.txt_logradouro.setText(campos[0])
        self.txt_bairro.setText(campos[1])
        self.txt_municipio.setText(campos[2])
        self.txt_uf.setText(campos[3])
        self.txt_cep.setText(campos[4])









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
