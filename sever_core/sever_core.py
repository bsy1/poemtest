# -*- coding: GB2312 -*-
import sys
from tabnanny import check
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from data import PoemRandom

class PoemApp(QWidget):
    def __init__(self):
        super().__init__()
        self.poem_generator = PoemRandom()  # ��ʼ�� PoemRandom ���ȡ����
        self.currentIndex = 0  # ��ǰ��ʾ�Ĺ�ʫ����

        self.initUI()
        self.loadNewPoem()  # ��ʼ��ʱ���ص�һ�׹�ʫ

    def initUI(self):
        self.setWindowTitle('�����ʫ�ʴ�')
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
        self.poem_data = self.poem_generator.init()  # ��ȡ�µĹ�ʫ����
        self.updateUI()

    def updateUI(self):
        self.label.setText(self.poem_data[0])
        self.button1.setText(self.poem_data[1])
        self.button2.setText(self.poem_data[2])
        self.button3.setText(self.poem_data[3])

    def checkAnswer(self, button_index):
        #correct_index = self.poem_data[0]  # ��ȷ�𰸵��������������б�����λ�ã�

        if self.poem_generator.check(button_index) :
            QMessageBox.information(self, '���', '�ش���ȷ��')
        else:
            QMessageBox.critical(self, '���', '�ش����')

        self.loadNewPoem()  # �����𰸺󣬼����µĹ�ʫ����

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PoemApp()
    window.show()
    sys.exit(app.exec())