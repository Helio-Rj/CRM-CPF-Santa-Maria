from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from ui_main import Ui_MainWindow
from cep_Api import postal
from cpf_Api import cpf_cad
from database import Data_base
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

        ###############################################################################################
        # PREENCHER AUTOMATICAMENTE OS DADOS DO CPF
        self.txt_cpf_pesquisa.editingFinished.connect(self.consulta_cpf)
        ###############################################################################################

    def consulta_cep(self):
        campos = postal(self.txt_cep_pesquisa.text())

        self.txt_logradouro.setText(campos[0])
        self.txt_bairro.setText(campos[1])
        self.txt_municipio.setText(campos[2])
        self.txt_uf.setText(campos[3])
        self.txt_cep.setText(campos[4])

    def consulta_cpf(self):
        cad = cpf_cad(self.txt_cpf_pesquisa.text())

    def cadastrar_cliente(self):
        db = Data_base()
        db.connect()

        fullDataSet = (

            self.txt_cpf.text(), self.txt_nome.text(), self.txt_rg.text(), self.txt_orgao_exp.text(),
            self.txt_data_exp.text(), self.txt_data_nasc.text(), self.txt_nome_mae.text(), self.txt_logradouro.text(),
            self.txt_numero.text(), self.txt_complemento.text(), self.txt_bairro.text(), self.txt_municipio.text(),
            self.txt_uf.text(), self.txt_cep.text(), self.txt_tel_cel.text().strip(), self.txt_email.text(),
            self.txt_aceite.text(), self.txt_data_insta.text(),
        )

        # CADASTRAR NO BANCO DE DADOS
        resp = db.register_cliente(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return


if __name__ == "__main__":
    db = Data_base()
    db.connect()
    db.create_table_cliente()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
