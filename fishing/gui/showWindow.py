import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import coordinate as coord

class myWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 현 상황 출력하는 라벨 추가
        label = QLabel('낚시 포인트를 지정해보아요!', self)
        label.move(10, 0)
        # label1 = QLabel('F12로 fishing point 10개 지정', self)
        # label2 = QLabel('Screenshot 버튼으로 느낌표 사진 저장 후 파일 넣기', self)
        # label3 = QLabel('낚시할 곳', self)

        # 좌표 입력 버튼 추가
        buttonCoordinate = QPushButton('낚시 포인트 지정', self)
        buttonCoordinate.clicked.connect(self.buttonCoordinate_clicked)



        # 느낌표 사진 저장 버튼 추가
        buttonExclamation = QPushButton('느낌표 사진 추가하기')

        # 저장한 좌표 불러오기, 콤보박스로 선택
        savedCoordinate = QComboBox(self)
        savedCoordinate.addItem('Option1')
        savedCoordinate.addItem('Option2')

        vbox = QVBoxLayout()
        vbox.addWidget(buttonCoordinate)
        vbox.addWidget(buttonExclamation)
        vbox.addWidget(savedCoordinate)
        self.setLayout(vbox)

    def buttonCoordinate_clicked(self):
        # 낚시터 이름 지정, Qdialog 이용
        self.target = QLineEdit(self)
        text, ok = QInputDialog.getText(self, '낚시 포인트 지정', '낚시터 이름 정해주세요: ')
        if ok:
            self.target.setText(str(text))
        # 함수에 낚시터 이름 및 포인트 전달
        coord.writeFishingPos(self.target)

        # name =
        # 좌표 뜨기

        # QMessageBox.about(self, "message", "clicked")


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        wg = myWidget()
        self.setCentralWidget(wg)
        self.datetime = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        # 창 이름 및 창 아이콘 설정
        self.setWindowTitle('LostArk 낚시 매크로 ver 1.0.0')
        self.setWindowIcon(QIcon('./img/lostark_icon.png'))

        # 창 위치 설정, 앞 두 매개변수는 x,y 위치, 뒤 두 매개변수는 너비와 높이
        self.setGeometry(500, 500, 400, 200)

        # 현재 날짜 상태바에 출력
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleLongDate) + ' ' + '낚시 준비 끝!')

        '''
        # 낚시할 좌표 뜨는 버튼 추가
        self.label = QLabel('label')
        buttonCoordinate = QPushButton('낚시 포인트 지정', self)
        buttonCoordinate.clicked.connect(self.buttonCoordinate_clicked)
        buttonExecution = QPushButton('낚시 시작~', self)
        buttonExecution.clicked.connect(self.buttonExecution_clicked) 
        
        
        # cetral위젯
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.buttonCoordinate)
        layout.addWidget(self.buttonExecution)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        '''

        # 메뉴바에 들어갈 종료 기능 추가
        exitAction = QAction(QIcon('./img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('앱 종료')
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바 추가
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # 툴바 추가
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # File 앞의 &는 단축키 -> Alt + F = 파일 메뉴의 단축키
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)



        '''
        # 닫기 버튼
        btn = QPushButton('닫기', self)
        btn.move(320, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)'''

        # 닫기 버튼 툴팁 나타내기
        # QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('누르면 앱이 종료됩니다.')

        # 상태바 추가
        # self.statusBar().showMessage('낚시 준비 끝!')

        self.show()

    def buttonCoordinate_clicked(self):
        self.label.setText('Clicked')

    def buttonExecution_clicked(self):
        self.label.setText('')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())