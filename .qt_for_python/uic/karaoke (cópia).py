# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karaoke (cópia).ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(781, 664)
        Form.setMinimumSize(QSize(781, 664))
        Form.setMaximumSize(QSize(781, 664))
        icon = QIcon()
        icon.addFile(u"karaoke.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(530, 60, 251, 601))
        self.frame.setStyleSheet(u"background-color: rgb(85, 87, 83);")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 231, 231))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 200, 61))
        font = QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(138, 226, 52);")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 80, 200, 45))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QRect(20, 130, 200, 45))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(239, 41, 41);")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 180, 200, 45))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 370, 231, 221))
        self.label_2.setPixmap(QPixmap(u"logokaraoke.png"))
        self.label_2.setScaledContents(True)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 260, 171, 111))
        self.frame_3.setStyleSheet(u"Qframe{\n"
"border:3px solid #ff007f;\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 40, 181, 71))
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(138, 226, 52);\n"
"border-color: rgb(136, 138, 133);")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, -10, 181, 51))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"color: rgb(115, 210, 22);")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 50, 531, 611))
        self.frame_2.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, -1, -1, -1)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 60))
        self.frame_6.setStyleSheet(u"background-color: rgb(85, 87, 83);\n"
"Qframe{\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(390, 10, 101, 36))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(290, 10, 96, 36))
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(18, 10, 261, 36))
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font4 = QFont()
        font4.setBold(True)
        font4.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font5 = QFont()
        font5.setPointSize(11)
        self.tableWidget.setFont(font5)
        self.tableWidget.setStyleSheet(u"alternate-background-color: rgb(245, 121, 0);\n"
"gridline-color: rgb(136, 138, 133);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(92, 53, 102);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-30, 0, 811, 47))
        self.frame_5.setStyleSheet(u"background-color: rgb(67, 23, 23);\n"
"background-color: rgb(85, 87, 83);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamily(u"Keraleeyam")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(True)
        font6.setWeight(9)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"font: 75 italic 10pt \"Keraleeyam\";")

        self.verticalLayout.addWidget(self.label)

        QWidget.setTabOrder(self.lineEdit, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton)

        self.retranslateUi(Form)
        self.lineEdit.editingFinished.connect(self.pushButton_5.click)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Lista do Karaok\u00ea", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Cantou!", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Excluir", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Hist\u00f3rico", None))
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"---", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"HORA:", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Atualizar", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Adicionar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Falta...", None));
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#e9b96e;\">KARAOKE RAUL ROCK BAR &amp; CAF\u00c9</span></p></body></html>", None))
    # retranslateUi

