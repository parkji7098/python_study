
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QTextEdit, QComboBox,
                                QSpinBox, QSlider, QProgressBar, QHBoxLayout,
                                QCheckBox, QGroupBox
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator,
)

from PySide2.QtCore import Qt, QRegExp, QThread

import sys
import serial
import time

class WorkerSumP1(QThread):
    def __init__(self, low, high,  widget):
        super().__init__()

        self.low = low
        self.high = high
        self.widget:QTextEdit = widget

        # print("widget id2: ", id(self.widget))

    def run(self) -> None:

        while True:
            print(f'스레드 시작 {self.low}부터 {self.high}까지 더할거임')

            now = time.time()
            total = 0
            for i in range(self.low, self.high):
                total += i

            delta = time.time() - now

            resultMSG = f'스레드끝: 결과는 {total}, 걸린시간: {delta} sec'
            print(resultMSG)

            self.widget.append(resultMSG)


        

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.inputLineEdit = QLineEdit()
        self.printTextEdit = QTextEdit()
        self.printTextEdit.setReadOnly(True)

        self.inputLineEdit.returnPressed.connect(self.sendMessage)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.inputLineEdit)
        mainLayout.addWidget(self.printTextEdit)

        self.setLayout(mainLayout)
        self.setWindowTitle("시리얼 통신")
        self.setMinimumSize(500,500)

    def sendMessage(self):
        inputText = self.inputLineEdit.text()

        # 입력된 문구가 숫자인지 파악

        # 입력된 문구를 숫자로 변경

        # 입력된 문구가 일정 범위 안에 있는지 파악

        # 숫자를 문자로 변경

        # 시리얼 통신을 통해 문자를 전달

        # 스레드 없이 메인스레드에서 더하기 함수 실행 테스트
        # self.sum(1, 100000000)

        print("widget id1: ", id(self.printTextEdit))

        # 스레드생성 및 시작
        self.workerSumP1 = WorkerSumP1(1, 10000000000, self.printTextEdit)
        self.workerSumP1.start()

        # 출력공간에 문구 추가 테스트
        # # self.printTextEdit.setText(self.printTextEdit.toPlainText() + inputText)
        # self.printTextEdit.append(inputText)

        # 입력된 문구를 초기화(지우기)
        self.inputLineEdit.setText('')




PORT = "/dev/ttyUSB0" 
# PORT = "/dev/ttyUSB0" #리눅스, $ sudo chmod 666 /dev/ttyUSB0
BAUDRATE = 9600

# 시리얼 포트와 통신 준비
# ser = serial.Serial(PORT, baudrate=BAUDRATE)

ser:serial.Serial = None


def prepare():
    global ser

    ser = serial.Serial(PORT, baudrate=BAUDRATE)


    pass

if __name__ == '__main__':
    # prepare()

    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()