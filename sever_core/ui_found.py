# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'foundHFdYyi.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(844, 673)
        self.love = QPushButton(Dialog)
        self.love.setObjectName(u"love")
        self.love.setGeometry(QRect(610, 150, 151, 51))
        self.found2 = QPushButton(Dialog)
        self.found2.setObjectName(u"found2")
        self.found2.setGeometry(QRect(610, 80, 151, 51))
        self.found1 = QTextEdit(Dialog)
        self.found1.setObjectName(u"found1")
        self.found1.setGeometry(QRect(80, 80, 451, 70))
        self.table = QTableWidget(Dialog)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(80, 300, 681, 341))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.love.setText(QCoreApplication.translate("Dialog", u"\u6dfb\u52a0\u6536\u85cf", None))
        self.found2.setText(QCoreApplication.translate("Dialog", u"\u67e5\u627e", None))
    # retranslateUi

