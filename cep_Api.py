from PySide6.QtWidgets import (QMessageBox)
import requests


def postal(cep):
    if len(cep) == 8:
        link = f'http://viacep.com.br/ws/{cep}/json'
        requisicao = requests.get(link)
        resp = requisicao.json()

        return resp['logradouro'], resp['bairro'], resp['localidade'], resp['uf'], resp['cep']
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("ERROR")
        msg.setText("Erro !!! Certifique-se que digitou os 8 dígitos do cep corretamente")
        msg.exec()
