# -*- coding: GB2312 -*-
import sys
from tabnanny import check
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from data import PoemRandom

class PoemApp(QWidget):
    def __init__(self):
        super().__init__()
        self.poem_generator = PoemRandom()  # 初始化 PoemRandom 类获取数据
        self.currentIndex = 0  # 当前显示的古诗索引

        self.initUI()
        self.loadNewPoem()  # 初始化时加载第一首古诗

    def initUI(self):
        self.setWindowTitle('随机古诗问答')
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)

        self.button1.clicked.connect(lambda: self.checkAnswer(1))
        self.button2.clicked.connect(lambda: self.checkAnswer(2))
        self.button3.clicked.connect(lambda: self.checkAnswer(3))

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def loadNewPoem(self):
        self.poem_data = self.poem_generator.init()  # 获取新的古诗数据
        self.updateUI()

    def updateUI(self):
        self.label.setText(self.poem_data[0])
        self.button1.setText(self.poem_data[1])
        self.button2.setText(self.poem_data[2])
        self.button3.setText(self.poem_data[3])

    def checkAnswer(self, button_index):
        #correct_index = self.poem_data[0]  # 正确答案的索引（假设在列表第五个位置）

        if self.poem_generator.check(button_index) :
            QMessageBox.information(self, '结果', '回答正确！')
        else:
            QMessageBox.critical(self, '结果', '回答错误！')

        self.loadNewPoem()  # 检查完答案后，加载新的古诗数据

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PoemApp()
    window.show()
    sys.exit(app.exec())