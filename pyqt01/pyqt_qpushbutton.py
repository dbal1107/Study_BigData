# class에서 show 불러와서 실행
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: # class는 함수 자신을 지정해야한다. exec -> 생성자는 보통 return 값이 없다. None / str이면 return을 str로 해야한다.
        super().__init__() # QWidget에 있는걸 호출
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400)
        self.setWindowTitle('QPushbutton 예제')
        self.show()

    def addControls(self) -> None:
        self.label =QLabel('메세지 :', self)
        self.label.setGeometry(10, 10, 600, 40)
        self.btn1 = QPushButton('클릭',self) 
        self.btn1.setGeometry(510, 350, 120, 40) # 창 크게하면 안따라감..
        # self.btn1.click # 누르는 순간
        self.btn1.clicked.connect(self.btn1_clicked) # 눌렀다 떼는 순간 / 시그널 연결

    # event(선택, 타이핑, 클릭...) = signal (in python)
    def btn1_clicked(self):
        self.label.setText('메세지 : btn1 버튼 클릭!!')
        QMessageBox.information(self, 'signal', 'btn1_clicked!!!') # 내용 없을때 오류 :not enough arguments

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

