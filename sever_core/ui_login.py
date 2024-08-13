# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginryTABG.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 171)
       
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 71, 21))
        self.passwd = QTextEdit(Dialog)
        self.passwd.setObjectName(u"textEdit_2")
        self.passwd.setGeometry(QRect(110, 70, 271, 41))
        self.init = QPushButton(Dialog)
        self.init.setObjectName(u"init")
        self.init.setGeometry(QRect(160, 120, 151, 41))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 54, 16))
        self.users = QTextEdit(Dialog)
        self.users.setObjectName(u"users")
        self.users.setGeometry(QRect(110, 20, 271, 41))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        
        self.label.setText(QCoreApplication.translate("Dialog", u"\u7528\u6237\u540d", None))
        self.init.setText(QCoreApplication.translate("Dialog", u"\u767b\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5bc6\u7801", None))
    # retranslateUi

