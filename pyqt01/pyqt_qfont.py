# class에서 show 불러와서 실행
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 클래스 OOP
class qTemplate(QWidget):
    # 생성자
    def __init__(self) -> None: # class는 함수 자신을 지정해야한다. exec -> 생성자는 보통 return 값이 없다. None / str이면 return을 str로 해야한다.
        super().__init__() # QWidget에 있는걸 호출
        self.initUI()
    
    # 화면정의를 위한 사용자 함수 initUI 변경가능
    def initUI(self) -> None:
        self.setGeometry(300, 200, 640, 400)
        self.setWindowTitle('QTemplate!!!!')
        self.text = 'What a wonderful world~'
        self.show()
    
    def paintEvent(self, event) -> None: # 창 위치옮기면 좌표바뀌기 때문에 다시 그림
        paint = QPainter()
        paint.begin(self)
        # 그리는 함수 추가
        self.drawText(event, paint)
        paint.end
    
    # 텍스트 그리기 위한 사용자함수
    def drawText(self, event, paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('MaruBuri',30))
        paint.drawText(105, 100, 'HELLo WORLD~~')
        paint.setPen(QColor(0,100,30))
        paint.setFont(QFont('MaruBuri',15))
        # paint.setFont(QFont('Impact',15))
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

