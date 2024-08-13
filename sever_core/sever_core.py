 # -*- coding: gb2312 -*-

# @Time    : 2023/9/25 22:03
# @Author  : MinChess
# @File    : main.py
# @Software: PyCharm
from ast import While
from gettext import find
import sys
from tkinter.messagebox import QUESTION
from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QIODevice, Slot,Qt
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction,QStandardItemModel, QStandardItem
from data import PoemRandom,FindData
import ui_login 
import ui_found
user=""
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
        action_users_quit=self.window.findChild(QAction,"quit")
        action_users_quit.triggered.connect(self.user_quit)
        action_information=self.window.findChild(QAction,"information")
        action_information.triggered.connect(self.users)
        action_find = self.window.findChild(QAction, "Found")
        action_find.triggered.connect(self.found)
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
    @Slot()
    def user_quit (self):
        #print(1)
        login=user_login()
        #login.window.show()
        login.exec()
    @Slot()
    def users(self):
        QMessageBox.information(self, "Users", "名称："+user) 
    @Slot()
    def found(self):
        finddd=findpoem()
        finddd.exec()
class user_login(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui=ui_login.Ui_Dialog()
        self.ui.setupUi(self)
        

        # 关闭UI文件
        
        # 加载UI文件
        
        self.ui.init.clicked.connect(self.ans1_click)
        
    @Slot()
    def ans1_click(self):
        users=self.ui.users.toPlainText()
        key=self.ui.passwd.toPlainText()
        print(users+" "+key)
class findpoem(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = ui_found.Ui_Dialog()
        self.ui.setupUi(self)

        # 连接按钮点击事件
        self.ui.found2.clicked.connect(self.findd)
        self.ui.love.clicked.connect(self.love)

    def findd(self):
        poemname = self.ui.found1.toPlainText().strip()
        if not poemname:
            return
        # 从 FindData 查询数据
        found = FindData()
        founddata = found.ff(poemname)  # 假设 founddata 是 List[Tuple]
        
        # 清除旧数据
        self.ui.list.clear()
        
        # 如果 founddata 为空，直接返回
        if not founddata:
            return
        
        # 将查询结果添加到 QListWidget 中
        for index, row in enumerate(founddata, start=1):
            item_text = f"{index}. {' | '.join(map(str, row))}"
            item = QListWidgetItem(item_text)
            self.ui.list.addItem(item)

    @Slot()
    def love(self):
        # 处理 'love' 按钮的点击事件
        selected_items = self.ui.list.selectedItems()
        if selected_items:
            # 获取第一个选中的项的索引
            item = selected_items[0]
            row = self.ui.list.row(item)
            print(f"Selected item is at row: {row + 1}")
        else:
            QMessageBox.warning(self, "Error!", "没有选中项")   
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.window.show()
    app.exec()
    
      