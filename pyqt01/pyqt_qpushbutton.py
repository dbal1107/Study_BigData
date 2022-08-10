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
        self.setWindowTitle('QPushbutton')
        self.show()

    def addControls(self) -> None:
        btn1 = QPushButton('Click',self) 
        btn1.setGeometry(510, 350, 120, 40) # 창 크게하면 안따라감..

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

