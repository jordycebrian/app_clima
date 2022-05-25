# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clima.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(400, 400)
        Form.setMaximumSize(QSize(400, 400))
        Form.setStyleSheet(u"QObject{\n"
"	background-color: #555;\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.lbl_titulo = QLabel(Form)
        self.lbl_titulo.setObjectName(u"lbl_titulo")
        self.lbl_titulo.setGeometry(QRect(0, 0, 401, 51))
        self.lbl_titulo.setStyleSheet(u"QObject{\n"
"	background-color: #999;\n"
"	color: black;\n"
"	font: 800 28pt \"Aria-Black\";\n"
"}")
        self.txt_buscar = QLineEdit(Form)
        self.txt_buscar.setObjectName(u"txt_buscar")
        self.txt_buscar.setGeometry(QRect(70, 70, 221, 20))
        self.txt_buscar.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"	color: black;\n"
"	font: 87 12pt \"Arial\";\n"
"	border-radius: 1px;\n"
"}")
        self.btn_buscar = QPushButton(Form)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(290, 70, 41, 21))
        self.btn_buscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_buscar.setStyleSheet(u"QObject{\n"
"	padding-bottom: 4px;\n"
"	font: 12pt \"Arial-black\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/busca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_buscar.setIcon(icon)
        self.btn_buscar.setCheckable(False)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 110, 361, 271))
        self.frame.setStyleSheet(u"background-color:#ccc;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_ciudad = QLabel(self.frame)
        self.lbl_ciudad.setObjectName(u"lbl_ciudad")
        self.lbl_ciudad.setStyleSheet(u"color: white;\n"
"font: 800 38pt \"Aria-Black\";")

        self.verticalLayout.addWidget(self.lbl_ciudad)

        self.lbl_grados = QLabel(self.frame)
        self.lbl_grados.setObjectName(u"lbl_grados")
        self.lbl_grados.setStyleSheet(u"color: white;\n"
"font: 800 40pt \"Aria-Black\";")

        self.verticalLayout.addWidget(self.lbl_grados)

        self.lbl_caracteristica = QLabel(self.frame)
        self.lbl_caracteristica.setObjectName(u"lbl_caracteristica")
        self.lbl_caracteristica.setStyleSheet(u"color: white;\n"
"font: 800 25pt \"Aria-Black\";")

        self.verticalLayout.addWidget(self.lbl_caracteristica)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Climex", None))
        self.lbl_titulo.setText(QCoreApplication.translate("Form", u"  Consulta del Clima", None))
        self.btn_buscar.setText("")
        self.lbl_ciudad.setText("")
        self.lbl_grados.setText("")
        self.lbl_caracteristica.setText("")
    # retranslateUi

