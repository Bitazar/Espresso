# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 500)
        Form.setMinimumSize(QSize(500, 330))
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.filebutton = QPushButton(Form)
        self.filebutton.setObjectName(u"filebutton")
        self.gridLayout_3.addWidget(self.filebutton, 1, 0, 1, 1)
        self.fcube = QWidget(Form)
        self.fcube.setObjectName(u"fcube")
        self.verticalLayout = QVBoxLayout(self.fcube)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.fcube)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)
        self.ledit = QLineEdit(self.fcube)
        self.ledit.setObjectName(u"ledit")
        self.verticalLayout.addWidget(self.ledit)
        self.gridLayout_3.addWidget(self.fcube, 2, 0, 1, 1)
        self.rcube = QWidget(Form)
        self.rcube.setObjectName(u"rcube")
        self.verticalLayout_2 = QVBoxLayout(self.rcube)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.rcube)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.redit = QLineEdit(self.rcube)
        self.redit.setObjectName(u"redit")
        self.verticalLayout_2.addWidget(self.redit)
        self.gridLayout_3.addWidget(self.rcube, 3, 0, 1, 1)
        self.stack = QStackedWidget(Form)
        self.stack.setObjectName(u"stack")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.list = QListWidget(self.page)
        self.list.setObjectName(u"list")
        self.gridLayout.addWidget(self.list, 1, 0, 1, 2)
        self.comboBox = QComboBox(self.page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        self.savebutton = QPushButton(self.page)
        self.savebutton.setObjectName(u"savebutton")
        self.gridLayout.addWidget(self.savebutton, 2, 1, 1, 1)
        self.timelabel = QLabel(self.page)
        self.timelabel.setObjectName(u"timelabel")
        self.timelabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gridLayout.addWidget(self.timelabel, 0, 1, 1, 1)
        self.stack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.err = QLabel(self.page_2)
        self.err.setObjectName(u"err")
        self.err.setAlignment(Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.err, 0, 0, 1, 1)
        self.stack.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stack, 4, 0, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.methodbox = QComboBox(Form)
        self.methodbox.addItem("")
        self.methodbox.addItem("")
        self.methodbox.setObjectName(u"methodbox")
        self.horizontalLayout.addWidget(self.methodbox)
        self.process = QPushButton(Form)
        self.process.setObjectName(u"process")
        self.horizontalLayout.addWidget(self.process)
        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        self.retranslateUi(Form)
        self.stack.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Ekspansja - Espresso", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Mateusz Jaracz", None))
        self.filebutton.setText(QCoreApplication.translate("Form", u"Otw\u00f3rz z pliku", None))
        self.label.setText(QCoreApplication.translate("Form", u"Jedynki funkcji (F):", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Zera funkcji (R):", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Wyniki", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Matematyczny", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Logiczny", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Alternatywne logiczne", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Programowanie z u\u017cyciem wato\u015bci boolowskich", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Programowanie z u\u017cyciem bit\u00f3w", None))
        self.savebutton.setText(QCoreApplication.translate("Form", u"Zapisz do pliku", None))
        self.timelabel.setText("")
        self.err.setText("")
        self.methodbox.setItemText(0, QCoreApplication.translate("Form", u"Ekspansja systematyczna", None))
        self.methodbox.setItemText(1, QCoreApplication.translate("Form", u"Ekspansja heurystyczna", None))
        self.process.setText(QCoreApplication.translate("Form", u"Minimalizuj", None))
    # retranslateUi