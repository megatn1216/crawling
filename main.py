from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        # label text
        self.label = QLabel("Hello World!")
        self.label.setFont(QtGui.QFont('Hack', 13))

        # button
        btn1 = QPushButton('btn1', self)
        btn1.setStyleSheet('background:lightgrey;')
        btn1.setMaximumHeight(100)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton('닫기', self)
        btn2.setStyleSheet('background:lightgrey;')
        btn2.setMaximumHeight(100)
        btn2.clicked.connect(self.btn_win_close)

        # layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.label, alignment=Qt.AlignCenter)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        self.setLayout(vbox)

        # window 셋팅
        self.setGeometry(600, 500, 300, 200)
        self.setWindowTitle("Crawling_oord")

    def btn_win_close(self):
        self.close()

    def btn1_clicked(self):
        print("클릭")

 
app = QApplication(sys.argv)
root = Window()
root.show()
 
sys.exit(app.exec_())