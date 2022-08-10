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
    
    # 화면정의를 위한 사용자 함수 initUI 변경가능
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300, 200, 640, 400)
        self.setWindowTitle('QLabel!!!!')
        self.show()
    
    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./pyqt01/images/lion.png')) # 윈도우아이콘 지정
        label1 = QLabel('', self)
        label2 = QLabel('', self)
        label1.setStyleSheet(
            ('border-width: 3px;'
             'border-style: solid;' # 경계 실선
             'border-color: blue;' # 실선 색
             'image: url(./pyqt01/images/image1.png)') # py 상대경로
        )
        label2.setStyleSheet(
            ('border-width: 3px;'
             'border-style: dot-dot-dash;' # 경계 실선
             'border-color: green;' # 실선 색
             'image: url(./pyqt01/images/image2.png)') # py 상대경로
        )
        # box = QVBoxLayout()
        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

