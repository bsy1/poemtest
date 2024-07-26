# -*- coding: gb2312 -*-

# @Time    : 2023/9/25 22:03
# @Author  : MinChess
# @File    : main.py
# @Software: PyCharm
from ast import While
import sys
from tkinter.messagebox import QUESTION
from PySide6.QtCore import QFile, QIODevice, Slot
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QTextBrowser
from PySide6.QtGui import QAction

from data import PoemRandom
poem=PoemRandom()
c=poem.init()
ques=c[1]
# ������������
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ����UI�ļ�
        loader = QUiLoader()
        ui_file = QFile("main.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print("�޷���UI�ļ�")
            sys.exit(-1)

        # ����UI�ļ���ʵ����Ϊ���ڶ���
        self.window = loader.load(ui_file)

        # �ر�UI�ļ�
        ui_file.close()
        self.question_textbox = self.window.findChild(QTextBrowser, "question")
        # ��ȡUI�ļ��е�С��������
        self.button1 = self.window.findChild(QPushButton, "ans1")
        self.button2 = self.window.findChild(QPushButton, "ans2")
        self.button3 = self.window.findChild(QPushButton, "ans3")
        
        # �����źźͲ�
        action_about_my = self.window.findChild(QAction, "my")
        action_about_my.triggered.connect(self.show_my_message)
        self.loadNewPoem()
        self.button1.clicked.connect(self.ans1_click)
        self.button2.clicked.connect(self.ans2_click)
        self.button3.clicked.connect(self.ans3_click)
    def loadNewPoem(self):
        self.poem_data = poem.init()  # ��ȡ�µĹ�ʫ����
        self.updateUI()

    def updateUI(self):
        self.question_textbox.setText(self.poem_data[0])
        self.button1.setText(self.poem_data[1])
        self.button2.setText(self.poem_data[2])
        self.button3.setText(self.poem_data[3])
    # ��ť����¼�������
    @Slot()
              
    def ans1_click(self):
         if poem.check(1):
            QMessageBox.information(self, '���', '�ش���ȷ��')
         else:
            QMessageBox.critical(self, '���', '�ش����')
         self.loadNewPoem()
    @Slot()
    def ans2_click(self):
         if poem.check(2):
            QMessageBox.information(self, '���', '�ش���ȷ��')
         else:
            QMessageBox.critical(self, '���', '�ش����')
         self.loadNewPoem()
    @Slot()
    def ans3_click(self):
         if poem.check(3):
            QMessageBox.information(self, '���', '�ش���ȷ��')
         else:
            QMessageBox.critical(self, '���', '�ش����')
         self.loadNewPoem()
    @Slot()
    def show_my_message(self):
        QMessageBox.information(self, "About My", "��hsbsy��ƿ�����github��https://github.com/bsy1/poemtest")    


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.window.show()
    app.exec()
    
        

