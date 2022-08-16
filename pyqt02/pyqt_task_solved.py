# class에서 show 불러와서 실행
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI 스레드와 작업스레드 분리 # 화면그리는것, 실행되는것 분리
class Worker(QThread): # 백그라운드
    # Q스레드는 화면을 그릴 권한이 없다.
    # 대신 통신을 통해서 ui스레드가 그림을 그릴 수 있도록 통신 수행 = signal
    valChangeSignal = pyqtSignal(int)

    def __init__(self, parent): # qTemplate이 부를거임
        super().__init__(parent)
        self.parent = parent
        self.working = True # class 내부변수 working을 만들어서 지정해줌
    
    def run(self): # 스레드는 항상 run 이라는 함수를 필요로 한다.
        while self.working: # working이 true인 동안 계속
            for i in range(0, 10000000): # 응답없음 발생
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i) # q스레드는 ui 그리는 권한 없다. 버튼눌러도 동작안함
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i) # ui스레드가 화면 그리도록 시그널 보냄
                time.sleep(0.0001) # 1 micro sec
                
# 클래스 OOP
class qTemplate(QWidget): # ui 그리는 권환있음
    # 생성자
    def __init__(self) -> None: # class는 함수 자신을 지정해야한다. exec -> 생성자는 보통 return 값이 없다. None / str이면 return을 str로 해야한다.
        super().__init__() # QWidget에 있는걸 호출
        uic.loadUi('./pyqt02/ttask.ui',self)
        self.initUI()
    
    def initUI(self) -> None:
        self.addControls()
        self.show()

    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btnStart_clicked) # 눌렀다 떼는 순간 / 시그널 연결
        # Worker 클래스 생성 후 동작
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress) # 스레드에서 보낸 시그널을 받아 updateprogress 함수에서 처리해줌

    @pyqtSlot(int) # pyqtslot으로 부르겠다.
    def updateProgress(self, val): # val: worker스레드에서 전달받은 반복값
        self.pgbTask.setValue(val) # i 대신 val
        self.txbLog.append(f'출력 > {val}') # 분리했기 때문에 응답없음 안뜸
        if val == 999999 :
            self.worker.working = False # 999999 면 동작 안하도록
            
    def btnStart_clicked(self):
        self.txbLog.append('실행!!')
        self.pgbTask.setRange(0, 999999)
        self.worker.start()
        self.worker.working = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplate()
    app.exec_()

