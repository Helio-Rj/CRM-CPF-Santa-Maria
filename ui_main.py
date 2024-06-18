# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cpf_cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 607)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.tab_cadastro = QWidget()
        self.tab_cadastro.setObjectName(u"tab_cadastro")
        self.frame_pes_cpf = QFrame(self.tab_cadastro)
        self.frame_pes_cpf.setObjectName(u"frame_pes_cpf")
        self.frame_pes_cpf.setGeometry(QRect(10, 20, 361, 69))
        self.frame_pes_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_pes_cpf.setFrameShape(QFrame.StyledPanel)
        self.frame_pes_cpf.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_pes_cpf)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_cpf_pesquisa = QLineEdit(self.frame_pes_cpf)
        self.txt_cpf_pesquisa.setObjectName(u"txt_cpf_pesquisa")
        self.txt_cpf_pesquisa.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"\n"
"font: 87 9pt \"Arial Black\";")
        self.txt_cpf_pesquisa.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cpf_pesquisa, 0, 1, 1, 1)

        self.pesquisa_label_cpf = QLabel(self.frame_pes_cpf)
        self.pesquisa_label_cpf.setObjectName(u"pesquisa_label_cpf")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.pesquisa_label_cpf.setFont(font)
        self.pesquisa_label_cpf.setStyleSheet(u"font: 87 9pt \"Arial Black\";\n"
"color: rgb(85, 0, 255);")

        self.gridLayout_2.addWidget(self.pesquisa_label_cpf, 0, 0, 1, 1)

        self.frame_main = QFrame(self.tab_cadastro)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(10, 110, 751, 401))
        self.frame_main.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(160, 160, 160);\n"
"border-radius: 5px;")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.txt_nome_mae = QLineEdit(self.frame_main)
        self.txt_nome_mae.setObjectName(u"txt_nome_mae")
        self.txt_nome_mae.setGeometry(QRect(10, 100, 720, 20))
        self.txt_nome_mae.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_nome_mae.setAlignment(Qt.AlignCenter)
        self.txt_logradouro = QLineEdit(self.frame_main)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setGeometry(QRect(11, 140, 600, 20))
        self.txt_logradouro.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)
        self.txt_municipio = QLineEdit(self.frame_main)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setGeometry(QRect(13, 220, 410, 20))
        self.txt_municipio.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_municipio.setAlignment(Qt.AlignCenter)
        self.txt_uf = QLineEdit(self.frame_main)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setGeometry(QRect(430, 220, 91, 20))
        self.txt_uf.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_uf.setAlignment(Qt.AlignCenter)
        self.txt_data_insta = QLineEdit(self.frame_main)
        self.txt_data_insta.setObjectName(u"txt_data_insta")
        self.txt_data_insta.setGeometry(QRect(150, 300, 161, 20))
        self.txt_data_insta.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_data_insta.setAlignment(Qt.AlignCenter)
        self.txt_aceite = QLineEdit(self.frame_main)
        self.txt_aceite.setObjectName(u"txt_aceite")
        self.txt_aceite.setGeometry(QRect(13, 300, 113, 20))
        self.txt_aceite.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_aceite.setAlignment(Qt.AlignCenter)
        self.txt_numero = QLineEdit(self.frame_main)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setGeometry(QRect(618, 140, 113, 20))
        self.txt_numero.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_numero.setAlignment(Qt.AlignCenter)
        self.txt_complemento = QLineEdit(self.frame_main)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setGeometry(QRect(11, 180, 550, 20))
        self.txt_complemento.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_complemento.setAlignment(Qt.AlignCenter)
        self.txt_data_nasc = QLineEdit(self.frame_main)
        self.txt_data_nasc.setObjectName(u"txt_data_nasc")
        self.txt_data_nasc.setGeometry(QRect(592, 60, 141, 20))
        self.txt_data_nasc.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_data_nasc.setAlignment(Qt.AlignCenter)
        self.txt_bairro = QLineEdit(self.frame_main)
        self.txt_bairro.setObjectName(u"txt_bairro")
        self.txt_bairro.setGeometry(QRect(570, 180, 160, 20))
        self.txt_bairro.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_bairro.setAlignment(Qt.AlignCenter)
        self.txt_cpf = QLineEdit(self.frame_main)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setGeometry(QRect(10, 20, 140, 20))
        self.txt_cpf.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_cpf.setAlignment(Qt.AlignCenter)
        self.txt_tel_cel = QLineEdit(self.frame_main)
        self.txt_tel_cel.setObjectName(u"txt_tel_cel")
        self.txt_tel_cel.setGeometry(QRect(10, 260, 381, 20))
        self.txt_tel_cel.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_tel_cel.setAlignment(Qt.AlignCenter)
        self.txt_nome = QLineEdit(self.frame_main)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(160, 20, 571, 20))
        self.txt_nome.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_nome.setAlignment(Qt.AlignCenter)
        self.txt_rg = QLineEdit(self.frame_main)
        self.txt_rg.setObjectName(u"txt_rg")
        self.txt_rg.setGeometry(QRect(10, 60, 170, 20))
        self.txt_rg.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_rg.setAlignment(Qt.AlignCenter)
        self.txt_orgao_exp = QLineEdit(self.frame_main)
        self.txt_orgao_exp.setObjectName(u"txt_orgao_exp")
        self.txt_orgao_exp.setGeometry(QRect(190, 60, 200, 20))
        self.txt_orgao_exp.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_orgao_exp.setAlignment(Qt.AlignCenter)
        self.txt_email = QLineEdit(self.frame_main)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(399, 260, 330, 20))
        self.txt_email.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_email.setAlignment(Qt.AlignCenter)
        self.txt_cep = QLineEdit(self.frame_main)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setGeometry(QRect(529, 220, 200, 20))
        self.txt_cep.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_cep.setAlignment(Qt.AlignCenter)
        self.txt_data_exp = QLineEdit(self.frame_main)
        self.txt_data_exp.setObjectName(u"txt_data_exp")
        self.txt_data_exp.setGeometry(QRect(400, 60, 181, 20))
        self.txt_data_exp.setStyleSheet(u"font: 87 7pt \"Arial Black\";\n"
"background-color: rgb(255, 255, 255);")
        self.txt_data_exp.setAlignment(Qt.AlignCenter)
        self.btn_salvar = QPushButton(self.frame_main)
        self.btn_salvar.setObjectName(u"btn_salvar")
        self.btn_salvar.setGeometry(QRect(560, 350, 160, 31))
        self.btn_salvar.setMinimumSize(QSize(160, 31))
        self.btn_salvar.setFont(font)
        self.btn_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(72, 144, 0);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"			\n"
"	\n"
"	\n"
"	font: 87 9pt \"Arial Black\";	\n"
"	\n"
"	\n"
"	background-color: rgb(0, 255, 127);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}\n"
"")
        self.label_info_rodape_2 = QLabel(self.tab_cadastro)
        self.label_info_rodape_2.setObjectName(u"label_info_rodape_2")
        self.label_info_rodape_2.setGeometry(QRect(10, 530, 201, 16))
        self.label_info_rodape_2.setStyleSheet(u"font: 25 9pt \"Yu Gothic\";")
        self.frame_pes_cep = QFrame(self.tab_cadastro)
        self.frame_pes_cep.setObjectName(u"frame_pes_cep")
        self.frame_pes_cep.setGeometry(QRect(380, 20, 381, 69))
        self.frame_pes_cep.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_pes_cep.setFrameShape(QFrame.StyledPanel)
        self.frame_pes_cep.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_pes_cep)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.txt_cep_pesquisa = QLineEdit(self.frame_pes_cep)
        self.txt_cep_pesquisa.setObjectName(u"txt_cep_pesquisa")
        self.txt_cep_pesquisa.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"\n"
"font: 87 9pt \"Arial Black\";")
        self.txt_cep_pesquisa.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txt_cep_pesquisa, 0, 1, 1, 1)

        self.pesquisa_label_cep = QLabel(self.frame_pes_cep)
        self.pesquisa_label_cep.setObjectName(u"pesquisa_label_cep")
        self.pesquisa_label_cep.setFont(font)
        self.pesquisa_label_cep.setStyleSheet(u"font: 87 9pt \"Arial Black\";\n"
"color: rgb(85, 0, 255);")

        self.gridLayout_4.addWidget(self.pesquisa_label_cep, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_cadastro, "")
        self.tab_consulta = QWidget()
        self.tab_consulta.setObjectName(u"tab_consulta")
        self.frame_cadastro = QFrame(self.tab_consulta)
        self.frame_cadastro.setObjectName(u"frame_cadastro")
        self.frame_cadastro.setGeometry(QRect(10, 110, 751, 441))
        self.frame_cadastro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QFrame.Raised)
        self.tabela_cadastro = QTableWidget(self.frame_cadastro)
        if (self.tabela_cadastro.columnCount() < 18):
            self.tabela_cadastro.setColumnCount(18)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabela_cadastro.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        self.tabela_cadastro.setObjectName(u"tabela_cadastro")
        self.tabela_cadastro.setGeometry(QRect(10, 11, 731, 401))
        self.tabela_cadastro.setStyleSheet(u"QHeaderView::section{\n"
"	\n"
"	background-color: rgb(148, 148, 148);\n"
"\n"
"	color: rgb(255, 255, 255);	\n"
"\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"\n"
"	\n"
"	\n"
"	background-color: rgb(247, 255, 202);\n"
"\n"
"}")
        self.label_info_rodape_4 = QLabel(self.frame_cadastro)
        self.label_info_rodape_4.setObjectName(u"label_info_rodape_4")
        self.label_info_rodape_4.setGeometry(QRect(0, 420, 201, 16))
        self.label_info_rodape_4.setStyleSheet(u"font: 25 9pt \"Yu Gothic\";")
        self.frame_top = QFrame(self.tab_consulta)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(10, 20, 751, 80))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_top.sizePolicy().hasHeightForWidth())
        self.frame_top.setSizePolicy(sizePolicy)
        self.frame_top.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_top)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 721, 32))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_info = QLabel(self.layoutWidget)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 85, 255);")

        self.horizontalLayout.addWidget(self.label_info)

        self.btn_excel = QPushButton(self.layoutWidget)
        self.btn_excel.setObjectName(u"btn_excel")
        self.btn_excel.setMinimumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_excel.setFont(font1)
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton:hover{	\n"
"	\n"
"	background-color: rgb(171, 255, 165);	\n"
"\n"
"	border-radius: 15px;	\n"
"\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";\n"
"	\n"
"	background-color: rgb(66, 206, 41);	\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.layoutWidget)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(50, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 211, 52);\n"
"	\n"
"	border-radius: 15px;\n"
"	\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";	\n"
"	\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.layoutWidget)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(50, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{		\n"
"	\n"
";\n"
"	background-color: rgb(255, 164, 164);\n"
"\n"
"	border-radius: 15px;	\n"
"\n"
"	color: #fff\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 87 8pt \"Arial Black\";		\n"
"	\n"
"	background-color: rgb(255, 120, 120);\n"
"\n"
"	border-radius: 15px;\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.tabWidget.addTab(self.tab_consulta, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_cpf_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CPF aqui", None))
        self.pesquisa_label_cpf.setText(QCoreApplication.translate("MainWindow", u"Pesquisa por CPF", None))
        self.txt_nome_mae.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da M\u00e3e", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_data_insta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data da Instala\u00e7\u00e3o", None))
        self.txt_aceite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Aceite", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_data_nasc.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_tel_cel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tel/Cel", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.txt_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.txt_orgao_exp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Org\u00e3o Expeditor", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_data_exp.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Data Expedi\u00e7\u00e3o", None))
        self.btn_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_info_rodape_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Puritoka Zaybatsu 2024", None))
        self.txt_cep_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite o CEP aqui", None))
        self.pesquisa_label_cep.setText(QCoreApplication.translate("MainWindow", u"Pesquisa por CEP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        ___qtablewidgetitem = self.tabela_cadastro.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem1 = self.tabela_cadastro.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_cadastro.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem3 = self.tabela_cadastro.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Org\u00e3o Expeditor", None));
        ___qtablewidgetitem4 = self.tabela_cadastro.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data da Expedi\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.tabela_cadastro.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem6 = self.tabela_cadastro.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nome da M\u00e3e", None));
        ___qtablewidgetitem7 = self.tabela_cadastro.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Logradouro", None));
        ___qtablewidgetitem8 = self.tabela_cadastro.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00b0", None));
        ___qtablewidgetitem9 = self.tabela_cadastro.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem10 = self.tabela_cadastro.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem11 = self.tabela_cadastro.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None));
        ___qtablewidgetitem12 = self.tabela_cadastro.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem13 = self.tabela_cadastro.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem14 = self.tabela_cadastro.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tel/Cel", None));
        ___qtablewidgetitem15 = self.tabela_cadastro.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None));
        ___qtablewidgetitem16 = self.tabela_cadastro.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Aceite", None));
        ___qtablewidgetitem17 = self.tabela_cadastro.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Data Instala\u00e7\u00e3o", None));
        self.label_info_rodape_4.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Puritoka Zaybatsu 2024", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"Listagem de Clientes", None))
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_consulta), QCoreApplication.translate("MainWindow", u"Consulta", None))
    # retranslateUi

