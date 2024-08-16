 # -*- coding: gb2312 -*-

# @Time    : 2023/9/25 22:03
# @Author  : MinChess
# @File    : main.py
# @Software: PyCharm

from ast import While
from gettext import find
import sys
def processPath(path):
    '''
    :param path: ����ڸ�Ŀ¼��·��
    :return: ƴ�Ӻõ�·��
    '''
    if getattr(sys, 'frozen', False):  # �ж��Ƿ��������frozen���Դ��ж��Ǵ���ĳ�����Դ���롣falseΪĬ��ֵ����û��frozen����ʱ����false
        base_path = sys._MEIPASS #������Ҳ�Ǵ������Ż��У�Դ���볢�Ի�ȡ�����Իᱨ��
    else:
        base_path = os.path.abspath(".") # ��Դ��������ʱʹ�ø�·��
    return os.path.join(base_path, path)

class DualOutput:
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        # ������ļ�
        with open(self.filename, 'a') as file:
            file.write(message)
        # ���������̨
        

    def flush(self):
        # �����ļ�����ͨ������Ҫ����
        sys.__stdout__.flush()

# ����һ�� DualOutput ʵ�������ض��� sys.stdout
sys.stdout = DualOutput('core.log')

# ʾ����ӡ���

import os

#from tkinter.messagebox import QUESTION
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtUiTools import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from init import *
import ui_login 
import ui_found

found = FindData()
poem=PoemRandom()
userc=users()
like=love('user.db')
bad_words=[';','"','?','+','=','-','_','[',']','{','}','|']


# ������������
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ����UI�ļ�
        loader = QUiLoader()
        ui_file = QFile(processPath("main.ui"))
        if not ui_file.open(QIODevice.ReadOnly):
            print("�޷���UI�ļ�")
            sys.exit(-1)
        self.modes=0  
        # ����UI�ļ���ʵ����Ϊ���ڶ���
        self.window = loader.load(ui_file)

        # �ر�UI�ļ�
        ui_file.close()
        self.question_textbox = self.window.findChild(QTextBrowser, "question")
        # ��ȡUI�ļ��е�С��������
        self.button1 = self.window.findChild(QPushButton, "ans1")
        self.button2 = self.window.findChild(QPushButton, "ans2")
        self.button3 = self.window.findChild(QPushButton, "ans3")
        self.button4 = self.window.findChild(QPushButton, "modeset")
        # �����źźͲ�
        action_about_mylike = self.window.findChild(QAction, "MyLike")
        action_about_mylike.triggered.connect(self.show_mylike_message)
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
        self.button4.clicked.connect(self.modeset)
    def loadNewPoem(self):
        self.poem_data = poem.init(self.modes)  # ��ȡ�µĹ�ʫ����
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
        login.userid=-1
        #login.window.show()
        login.exec()
    @Slot()
    def users(self):
        QMessageBox.information(self, "Users", "���ƣ�"+login.username) 
    @Slot()
    def found(self):
        finddd=findpoem()
        finddd.exec()
    @Slot()
    def modeset(self):
        self.modes = not self.modes
        self.loadNewPoem()
    def show_mylike_message(self):
        likee=Poemlike()
        likee.exec()
class user_login(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = ui_login.Ui_Dialog()
        self.ui.setupUi(self)
        self.username = ""
        self.userid = -1
        
        # ���Ӱ�ť�ĵ���¼�
        self.ui.init.clicked.connect(self.ans1_click)
        
    @Slot()
    def ans1_click(self):
        # ��ȡ QLineEdit �е��ı�
        users = self.ui.users.text()
        key = self.ui.passwd.text()
        
        for word in bad_words:
            if word.lower() in users.lower():
                QMessageBox.warning(self, "Error", f"�������Υ���ʣ�����{word.lower()}")
                return
        
        if not users or not key:
            QMessageBox.warning(self, "Error", "�����룡����")
            return
        
        self.userid = userc.login(users, key)
        self.userid = userc.login(users, key)
        if self.userid != -1:
            self.username = users
            self.close()
            self.ui.users.clear()
            self.ui.passwd.clear()
            poem.poemlist=like.get_data_as_list(login.userid)
            QMessageBox.information(self, "OK", "��½�ɹ���")
        else:
            QMessageBox.information(self, "Error", "��½ʧ�ܡ�")
            self.ui.users.clear()
            self.ui.passwd.clear()
    
    @Slot()
    def closeEvent(self, event):
        # ��ֹ�رմ���
        if self.userid == -1:
            event.ignore()
            QMessageBox.information(self, "Info", "���¼")
        else:
            event.accept()
    
    

   
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
        for word in bad_words:
            if word.lower() in poemname.lower():
                 QMessageBox.warning(self,"Error","�������Υ���ʣ�����"+word.lower())
                 return 0
        # �� FindData ��ѯ����
        
        founddata = found.ff(poemname)  # ���� founddata �� List[Tuple]
        
        # ���������
        self.ui.table.setRowCount(0)  # ���������
        
        # ��� founddata Ϊ�գ�ֱ�ӷ���
        if not founddata:
            return
        
        # ������ɫ�б�
        colors = [QColor("#f0f0f0"), QColor("#ffffff")]  # ������ɫ��ǳ��ɫ�Ͱ�ɫ
        
        # ���ñ�������������
        self.ui.table.setRowCount(len(founddata))
        self.ui.table.setColumnCount(4)  # ������ 3 �У�Title, Author, Content
        
        # ���ñ�ͷ
        self.ui.table.setHorizontalHeaderLabels(["id","Title", "Author", "Content"])
        
        # ����ѯ�����ӵ� QTableWidget ��
        for index, row in enumerate(founddata):
            for col, data in enumerate([row[0],row[1], row[2], row[13]]):  # Title, Author, Content
                item = QTableWidgetItem(str(data))
                item.setBackground(colors[index % 2])  # ���ñ�����ɫ
                
                # ʹ�ı�����
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
                item.setToolTip(str(data))  # ȷ�����ı����Ա���ȫ����
                
                # �����п�����Ӧ����
                self.ui.table.resizeColumnToContents(col)
                
                self.ui.table.setItem(index, col, item)

    @Slot()
    def love(self):
        selected_items = self.ui.table.selectedItems()
        if selected_items:
            # ��ȡ��һ��ѡ�е�����к�
            row = selected_items[0].row()
            item = self.ui.table.item(row, 0)
            like.update_pid(login.userid,item.text())
            QMessageBox.information(self, "OK", "��ӳɹ���")
            poem.poemlist=like.get_data_as_list(login.userid)
            
        else:
            QMessageBox.warning(self, "Error!", "û��ѡ����")
class Poemlike(QDialog):
    def __init__(self):
        super().__init__()
        self.poemlist = poem.poemlist
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Poem List")
        self.setGeometry(100, 100, 400, 300)

        # ��������
        layout = QVBoxLayout()
        self.setLayout(layout)

        # �������ɱ༭�� QListWidget
        self.list_widget = QListWidget()
        self.list_widget.setEditTriggers(QListWidget.NoEditTriggers)  # ���ñ༭
        
        layout.addWidget(self.list_widget)

        # ������ɫ�б�
        colors = [QColor("#f0f0f0"), QColor("#ffffff")]  # ������ɫ��ǳ��ɫ�Ͱ�ɫ
        
        for index, row in enumerate(self.poemlist):
            founddata = found.idfound(int(row))
            if not founddata:
                continue
            
            for data in founddata:
                item_text = f"ID: {data[0]}  Title: {data[1]}  Author: {data[2]}  Content: {data[13]}"
                item = QListWidgetItem(item_text)
                item.setBackground(colors[index % 2])  # ���ñ�����ɫ
                item.setToolTip(item_text)  # ȷ�����ı����Ա���ȫ����
                
                self.list_widget.addItem(item)

        # ��ӹرհ�ť
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)
if __name__ == "__main__":
    
    app = QApplication([])
    main_window = MainWindow()
    login=user_login()
    
    main_window.window.show()
    login.exec()
    app.exec()
    
      