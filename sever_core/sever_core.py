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
    @Slot()
    def user_quit (self):
        #print(1)
        login=user_login()
        #login.window.show()
        login.exec()
    @Slot()
    def users(self):
        QMessageBox.information(self, "Users", "���ƣ�"+user) 
    @Slot()
    def found(self):
        finddd=findpoem()
        finddd.exec()
class user_login(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui=ui_login.Ui_Dialog()
        self.ui.setupUi(self)
        

        # �ر�UI�ļ�
        
        # ����UI�ļ�
        
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

        # ���Ӱ�ť����¼�
        self.ui.found2.clicked.connect(self.findd)
        self.ui.love.clicked.connect(self.love)

    def findd(self):
        poemname = self.ui.found1.toPlainText().strip()
        if not poemname:
            return
        # �� FindData ��ѯ����
        found = FindData()
        founddata = found.ff(poemname)  # ���� founddata �� List[Tuple]
        
        # ���������
        self.ui.list.clear()
        
        # ��� founddata Ϊ�գ�ֱ�ӷ���
        if not founddata:
            return
        
        # ����ѯ�����ӵ� QListWidget ��
        for index, row in enumerate(founddata, start=1):
            item_text = f"{index}. {' | '.join(map(str, row))}"
            item = QListWidgetItem(item_text)
            self.ui.list.addItem(item)

    @Slot()
    def love(self):
        # ���� 'love' ��ť�ĵ���¼�
        selected_items = self.ui.list.selectedItems()
        if selected_items:
            # ��ȡ��һ��ѡ�е��������
            item = selected_items[0]
            row = self.ui.list.row(item)
            print(f"Selected item is at row: {row + 1}")
        else:
            QMessageBox.warning(self, "Error!", "û��ѡ����")   
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.window.show()
    app.exec()
    
      