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
# 定义主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 加载UI文件
        loader = QUiLoader()
        ui_file = QFile("main.ui")
        if not ui_file.open(QIODevice.ReadOnly):
            print("无法打开UI文件")
            sys.exit(-1)

        # 加载UI文件并实例化为窗口对象
        self.window = loader.load(ui_file)

        # 关闭UI文件
        ui_file.close()
        self.question_textbox = self.window.findChild(QTextBrowser, "question")
        # 获取UI文件中的小部件对象
        self.button1 = self.window.findChild(QPushButton, "ans1")
        self.button2 = self.window.findChild(QPushButton, "ans2")
        self.button3 = self.window.findChild(QPushButton, "ans3")
        
        # 连接信号和槽
        action_about_my = self.window.findChild(QAction, "my")
        action_about_my.triggered.connect(self.show_my_message)
        self.loadNewPoem()
        self.button1.clicked.connect(self.ans1_click)
        self.button2.clicked.connect(self.ans2_click)
        self.button3.clicked.connect(self.ans3_click)
    def loadNewPoem(self):
        self.poem_data = poem.init()  # 获取新的古诗数据
        self.updateUI()

    def updateUI(self):
        self.question_textbox.setText(self.poem_data[0])
        self.button1.setText(self.poem_data[1])
        self.button2.setText(self.poem_data[2])
        self.button3.setText(self.poem_data[3])
    # 按钮点击事件处理函数
    @Slot()
              
    def ans1_click(self):
         if poem.check(1):
            QMessageBox.information(self, '结果', '回答正确！')
         else:
            QMessageBox.critical(self, '结果', '回答错误！')
         self.loadNewPoem()
    @Slot()
    def ans2_click(self):
         if poem.check(2):
            QMessageBox.information(self, '结果', '回答正确！')
         else:
            QMessageBox.critical(self, '结果', '回答错误！')
         self.loadNewPoem()
    @Slot()
    def ans3_click(self):
         if poem.check(3):
            QMessageBox.information(self, '结果', '回答正确！')
         else:
            QMessageBox.critical(self, '结果', '回答错误！')
         self.loadNewPoem()
    @Slot()
    def show_my_message(self):
        QMessageBox.information(self, "About My", "由hsbsy设计开发，github：https://github.com/bsy1/poemtest")    


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.window.show()
    app.exec()
    
        

