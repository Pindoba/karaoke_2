# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karaoke.ui'
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
        Form.resize(1097, 681)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(765, 681))
        Form.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"karaoke.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(67, 23, 23);\n"
"background-color: rgb(85, 87, 83);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Keraleeyam")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 75 italic 10pt \"Keraleeyam\";")

        self.verticalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 2)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(370, 0))
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
"border-color: rgba(191, 64, 64, 0);\n"
"Qframe{\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.frame_6)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(0, 4))
        font1 = QFont()
        font1.setPointSize(13)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(136, 138, 133);")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_8.setFont(font3)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet(u"color: rgb(115, 210, 22);")
        self.label_8.setTextFormat(Qt.AutoText)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(22)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(100, 41))
        font4 = QFont()
        font4.setPointSize(27)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_4.setFont(font4)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet(u"color: rgb(138, 226, 52);\n"
"border-color: rgb(136, 138, 133);")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.frame_2)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font6 = QFont()
        font6.setPointSize(11)
        self.tableWidget.setFont(font6)
        self.tableWidget.setStyleSheet(u"alternate-background-color: rgb(245, 121, 0);\n"
"gridline-color: rgb(136, 138, 133);\n"
"border-color: rgb(255, 255, 255);\n"
"selection-color: rgb(92, 53, 102);\n"
"color: rgb(255, 255, 255);")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(195)
        self.tableWidget.verticalHeader().setMinimumSectionSize(24)
        self.tableWidget.verticalHeader().setDefaultSectionSize(32)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setStyleSheet(u"background-color: rgb(85, 87, 83);")
        self.frame.setInputMethodHints(Qt.ImhNone)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 10, 231, 231))
        self.frame_4.setStyleSheet(u"border-color: rgba(191, 64, 64, 0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 200, 61))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(138, 226, 52);")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 80, 200, 45))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QRect(20, 130, 200, 45))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(239, 41, 41);")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 180, 200, 45))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 320, 231, 221))
        self.label_2.setPixmap(QPixmap(u"logokaraoke.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 570, 211, 20))
        self.label_3.setStyleSheet(u"color:rgb(26, 103, 252)")

        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)

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
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#e9b96e;\">KARAOKE RAUL ROCK BAR &amp; CAF\u00c9</span></p></body></html>", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Insira um nome", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Adicionar", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Atualizar", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"  HOR\u00c1RIO   ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u" 00:00 ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Falta...", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Obs.:", None));
        self.pushButton.setText(QCoreApplication.translate("Form", u"Cantou!", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Excluir", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Hist\u00f3rico", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><a href=\"https://www.linkedin.com/in/welton-moura-23a897230\"><span style=\" text-decoration: underline; color:#8ae234;\">CREATED BY WELTON MOURA</span></a></p></body></html>", None))
    # retranslateUi

