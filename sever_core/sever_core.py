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
    :param path: 相对于根目录的路径
    :return: 拼接好的路径
    '''
    if getattr(sys, 'frozen', False):  # 判断是否存在属性frozen，以此判断是打包的程序还是源代码。false为默认值，即没有frozen属性时返回false
        base_path = sys._MEIPASS #该属性也是打包程序才会有，源代码尝试获取该属性会报错
    else:
        base_path = os.path.abspath(".") # 当源代码运行时使用该路径
    return os.path.join(base_path, path)

class DualOutput:
    def __init__(self, filename):
        self.filename = filename

    def write(self, message):
        # 输出到文件
        with open(self.filename, 'a') as file:
            file.write(message)
        # 输出到控制台
        

    def flush(self):
        # 兼容文件流，通常不需要处理
        sys.__stdout__.flush()

# 创建一个 DualOutput 实例，并重定向 sys.stdout
sys.stdout = DualOutput('core.log')

# 示例打印输出

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


# 定义主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 加载UI文件
        loader = QUiLoader()
        ui_file = QFile(processPath("main.ui"))
        if not ui_file.open(QIODevice.ReadOnly):
            print("无法打开UI文件")
            sys.exit(-1)
        self.modes=0  
        # 加载UI文件并实例化为窗口对象
        self.window = loader.load(ui_file)

        # 关闭UI文件
        ui_file.close()
        self.question_textbox = self.window.findChild(QTextBrowser, "question")
        # 获取UI文件中的小部件对象
        self.button1 = self.window.findChild(QPushButton, "ans1")
        self.button2 = self.window.findChild(QPushButton, "ans2")
        self.button3 = self.window.findChild(QPushButton, "ans3")
        self.button4 = self.window.findChild(QPushButton, "modeset")
        # 连接信号和槽
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
        self.poem_data = poem.init(self.modes)  # 获取新的古诗数据
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
        login.userid=-1
        #login.window.show()
        login.exec()
    @Slot()
    def users(self):
        QMessageBox.information(self, "Users", "名称："+login.username) 
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
        
        # 连接按钮的点击事件
        self.ui.init.clicked.connect(self.ans1_click)
        
    @Slot()
    def ans1_click(self):
        # 获取 QLineEdit 中的文本
        users = self.ui.users.text()
        key = self.ui.passwd.text()
        
        for word in bad_words:
            if word.lower() in users.lower():
                QMessageBox.warning(self, "Error", f"输入包含违禁词！！！{word.lower()}")
                return
        
        if not users or not key:
            QMessageBox.warning(self, "Error", "空输入！！！")
            return
        
        self.userid = userc.login(users, key)
        self.userid = userc.login(users, key)
        if self.userid != -1:
            self.username = users
            self.close()
            self.ui.users.clear()
            self.ui.passwd.clear()
            poem.poemlist=like.get_data_as_list(login.userid)
            QMessageBox.information(self, "OK", "登陆成功。")
        else:
            QMessageBox.information(self, "Error", "登陆失败。")
            self.ui.users.clear()
            self.ui.passwd.clear()
    
    @Slot()
    def closeEvent(self, event):
        # 阻止关闭窗口
        if self.userid == -1:
            event.ignore()
            QMessageBox.information(self, "Info", "请登录")
        else:
            event.accept()
    
    

   
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
        for word in bad_words:
            if word.lower() in poemname.lower():
                 QMessageBox.warning(self,"Error","输入包含违禁词！！！"+word.lower())
                 return 0
        # 从 FindData 查询数据
        
        founddata = found.ff(poemname)  # 假设 founddata 是 List[Tuple]
        
        # 清除旧数据
        self.ui.table.setRowCount(0)  # 清除所有行
        
        # 如果 founddata 为空，直接返回
        if not founddata:
            return
        
        # 定义颜色列表
        colors = [QColor("#f0f0f0"), QColor("#ffffff")]  # 隔行颜色：浅灰色和白色
        
        # 设置表格的行数和列数
        self.ui.table.setRowCount(len(founddata))
        self.ui.table.setColumnCount(4)  # 假设有 3 列：Title, Author, Content
        
        # 设置表头
        self.ui.table.setHorizontalHeaderLabels(["id","Title", "Author", "Content"])
        
        # 将查询结果添加到 QTableWidget 中
        for index, row in enumerate(founddata):
            for col, data in enumerate([row[0],row[1], row[2], row[13]]):  # Title, Author, Content
                item = QTableWidgetItem(str(data))
                item.setBackground(colors[index % 2])  # 设置背景颜色
                
                # 使文本换行
                item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
                item.setToolTip(str(data))  # 确保长文本可以被完全看到
                
                # 设置列宽自适应内容
                self.ui.table.resizeColumnToContents(col)
                
                self.ui.table.setItem(index, col, item)

    @Slot()
    def love(self):
        selected_items = self.ui.table.selectedItems()
        if selected_items:
            # 获取第一个选中的项的行号
            row = selected_items[0].row()
            item = self.ui.table.item(row, 0)
            like.update_pid(login.userid,item.text())
            QMessageBox.information(self, "OK", "添加成功。")
            poem.poemlist=like.get_data_as_list(login.userid)
            
        else:
            QMessageBox.warning(self, "Error!", "没有选中项")
class Poemlike(QDialog):
    def __init__(self):
        super().__init__()
        self.poemlist = poem.poemlist
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Poem List")
        self.setGeometry(100, 100, 400, 300)

        # 创建布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 创建不可编辑的 QListWidget
        self.list_widget = QListWidget()
        self.list_widget.setEditTriggers(QListWidget.NoEditTriggers)  # 禁用编辑
        
        layout.addWidget(self.list_widget)

        # 定义颜色列表
        colors = [QColor("#f0f0f0"), QColor("#ffffff")]  # 隔行颜色：浅灰色和白色
        
        for index, row in enumerate(self.poemlist):
            founddata = found.idfound(int(row))
            if not founddata:
                continue
            
            for data in founddata:
                item_text = f"ID: {data[0]}  Title: {data[1]}  Author: {data[2]}  Content: {data[13]}"
                item = QListWidgetItem(item_text)
                item.setBackground(colors[index % 2])  # 设置背景颜色
                item.setToolTip(item_text)  # 确保长文本可以被完全看到
                
                self.list_widget.addItem(item)

        # 添加关闭按钮
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
    
      