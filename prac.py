import sys
from PyQt5.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

        self.setGeometry(300, 100, 350, 150)  # x, y, width, height
        self.setWindowTitle("QWidget")
        self.show()


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle("QDialog")
        self.show()


class MyMainWindow(QMainWindow):
    """
    틀린방법...

    ** QWidget, QDialog 처럼 layout 사용 못함.
    """

    def __init__(self):
        super().__init__()
        btn1 = QPushButton('1')
        btn2 = QPushButton('2')

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

        self.setGeometry(300, 500, 350, 150)
        self.setWindowTitle("QMainWindow 틀린 방법")
        self.show()


class MyMainWindow2(QMainWindow):
    """
    옳은 방법...

    QWidget, QDialog 와 달리 QMainWindow 는 자체적으로 layout 가지고 있다.
    central widget 을 반드시 필요로함.
    """

    def __init__(self):
        super().__init__()
        wg = MyWidget()
        # wg = MyWidget2()   # placeholder -- QWidget 상속하여 만든것으로 추후 교체하면 됨.
        self.setCentralWidget(wg)  # 반드시 필요함.

        self.setGeometry(300, 700, 350, 150)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    # ex2 = MyMainWindow()
    # ex3 = MyDialog()
    ex4 = MyMainWindow2()
    sys.exit(app.exec_())