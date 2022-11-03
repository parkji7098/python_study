
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QTextEdit, QComboBox, 
                                QSpinBox, QSlider, QProgressBar,
                                QCheckBox, QGroupBox,
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator
)

from PySide2.QtCore import Qt, QRegExp, QThread, Signal, Slot

import sys
import serial
import time
from serial.tools import list_ports
# import serial.tools.list_ports


BAUDRATES = [
    300,
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    74880,
    115200,
    230400,
    250000,
    500000,
    1000000,
    2000000,
]

ports = []

PORT = "COM3" #윈도우
# PORT = "/dev/ttyUSB0" #리눅스, $ sudo chmod 666 /dev/ttyUSB0
# /dev/ttyS*

BAUDRATE = 9600
# BAUDRATE = 115200

# 시리얼 포트와 통신 준비
# ser = serial.Serial(PORT, baudrate=BAUDRATE)

ser:serial.Serial = None

class WorkerSumP1(QThread):

    def __init__(self, low, high, widget):
        super().__init__()

        self.low = low
        self.high = high
        self.widget:QTextEdit = widget

        # print("widget id2: ", id(self.widget))

    def run(self) -> None:

        print(f'스레드시작: {self.low}부터 {self.high}까지 더할거임')
        now = time.time()

        total = 0
        for i in range(self.low, self.high):
            total += i

        delta = time.time() - now

        resultMSG = f'스레드끝: 결과는 {total}, 걸린시간: {delta} sec'
        print(resultMSG)

        self.widget.append(resultMSG)

        pass
    pass

class CallackHandler():

    def __init__(self):

        self.functions = []
        pass

    def connect(self, func):
        self.functions.append(func)

        # print('id(func): ', id(func))
        # print('id(self.functions last): ', id(self.functions[len(self.functions)-1]))

        # self.functions[0] = func

    def disconnect(self, func = None):

        # print('disconnect:: id(func): ', id(func))
        # print('disconnect:: id(self.functions last): ', id(self.functions[len(self.functions)-1]))

        if not func:
            self.functions.clear()
            return

        # self.functions.remove(func)

        funcs = self.functions[:]

        for f in self.functions:
            if f == func:
                funcs.pop(funcs.index(f))

        self.functions = funcs


        # for i in range(len(self.functions)):
        #     f = self.functions[i]
        #     # print('f is func: ', f is func)
        #     # print('id(f) == id(func): ', id(f) == id(func))
        #     # print('id(f): ', id(f))
        #     # print('f == func: ', f == func)
        #     if f == func:
        #     # if f is func:
        #     # if id(f) == id(func):
        #         self.functions.pop(i)


        # for f in self.functions:
        #     # f와 func 이 같다면 functions 안에서 제거
        #     if f is func:
        #         self.functions.remove(f)

        pass

    def emit(self, *args):

        for func in self.functions:
            func(args)
            pass

        pass

    pass

class WorkerSumP2(QThread):

    # callbackSignal = pyqtSignal(str) #pyqt5
    callbackSignal = Signal(str) #pyside2

    handler = CallackHandler()

    def __init__(self, low, high, callback):
        super().__init__()

        self.low = low
        self.high = high
        # self.callback = callback

        self.callbackSignal.connect(callback)

    def run(self) -> None:

        print(f'스레드시작: {self.low}부터 {self.high}까지 더할거임')
        now = time.time()

        total = 0
        for i in range(self.low, self.high):
            total += i

        delta = time.time() - now

        resultMSG = f'스레드끝: 결과는 {total}, 걸린시간: {delta} sec'
        print(resultMSG)

        # self.callback(resultMSG) # 권장되지 않는 방법

        # 시그널을 통해 Signal.connect(함수명) 된 함수를 호출 할땐 Signal.emit(매개변수) *시그널 사용 권장
        self.callbackSignal.emit(resultMSG)

        self.handler.emit(resultMSG)
        
        pass

    pass

class WorkerSerialRead(QThread):

    onRead = Signal(str)

    def __init__(self):
        super().__init__()

        self.working = True

        pass

    def run(self):
        # 시리얼통신을 통해 데이터를 읽어옴
        # while self.working:
        while True:
            print(f"Serial Read:: {time.time()}")

            if ser == None or ser.closed:
                # print(f"시리얼통신 미준비")
                time.sleep(1)
                continue

            try:
                # print(f"Serial Readline:: {time.time()}")
                line = ser.readline().decode().replace('\n', '').replace('\r', '')
                # line = ser.read().decode()
            
                # "" == False
                if not line:
                    # print(f"읽어온 데이터 없음")
                    # time.sleep(1)
                    continue
                
                # print("readline: " + line)
                self.onRead.emit(line)

            except Exception as e:
                print('error: e: ', e)

            # time.sleep(1)
            pass

    def stop(self):
        self.working = False
        self.quit()
        # self.wait(1000)

        pass

    pass




class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        print("현재 사용가능한 시리얼포트를 조회")

        # 현재 사용가능한 시리얼포트를 조회
        comports = list_ports.comports()
        for comport in comports:

            device = comport.device
            if 'ttyS' in device:
                continue

            ports.append(device)
            pass



        self.inputLineEdit = QLineEdit()
        self.printTextEdit = QTextEdit()
        self.printTextEdit.setReadOnly(True)

        self.inputLineEdit.returnPressed.connect(self.sendMessage)


        # 두개의 콤보박스 (보드레이트, 포트)
        self.baudrateComboBox = QComboBox()
        self.baudrateComboBox.currentIndexChanged.connect(self.onChangedBaudrateAndPort)
        self.portComboBox = QComboBox()
        self.portComboBox.currentIndexChanged.connect(self.onChangedBaudrateAndPort)

        # 가로로 정렬된 모습으로 두개의 콤보박스를 추가
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.baudrateComboBox)
        hboxLayout.addWidget(self.portComboBox)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.inputLineEdit)
        mainLayout.addWidget(self.printTextEdit)
        mainLayout.addLayout(hboxLayout)


        self.setLayout(mainLayout)
        self.setWindowTitle("시리얼통신")
        self.setMinimumSize(500,500)

        # self.workerSerialRead = WorkerSerialRead()
        # self.workerSerialRead.onRead.connect(self.complete)
        # self.workerSerialRead.start()


        # 보드레이트 목록을 보드레이트 콤보의 선택가능한 항목(item)으로 추가
        # self.baudrateComboBox.addItems(BAUDRATES)
        for b in BAUDRATES:
            baudrateName = f'{b} 보드레이트'
            self.baudrateComboBox.addItem(baudrateName)

        # print('ports: ', ports)
        # 조회된 시리얼포트를 포트 콤보박스에 추가
        self.portComboBox.addItems(ports)

        pass

    def onChangedBaudrateAndPort(self):
        # 현재 선택된 보드레이트 인덱스를 읽어와서 사용할 보드레이트 값을 준비
        currentIndex = self.baudrateComboBox.currentIndex()
        print("onChangedBaudrate: currentIndex: ", currentIndex)

        if currentIndex < 0:
            return

        baudrate = BAUDRATES[currentIndex]

        # 현재 선택된 포트 인덱스를 읽어와서 사용할 포트 값을 준비
        currentIndex = self.portComboBox.currentIndex()
        print("onChangePort: currentIndex: ", currentIndex)

        if currentIndex < 0:
            return

        port = ports[currentIndex]

        global ser
        if ser != None:
            if ser.baudrate != baudrate:
                ser.baudrate = baudrate

            if ser.port != port:
                ser.port = port
            # ser.open()
        else:
            ser = serial.Serial(port, baudrate=baudrate, timeout=1) #시리얼통신이 연결 (시리얼 오픈)
            # ser.timeout = 

            self.workerSerialRead = WorkerSerialRead()
            self.workerSerialRead.onRead.connect(self.complete)
            self.workerSerialRead.start()


        # if ser:
        #     ser.close()

        # ser = serial.Serial(port, baudrate=baudrate)

        print("onChangePort: ready serial: ", ser)

        pass


    def sendMessage(self):
        
        # 스레드 없이 메인스레드에서 더하기 함수 실행 테스트
        # self.sum(1, 100000000)

        # print("widget id1: ", id(self.printTextEdit))

        # 스레드생성 및 시작
        # self.workerSumP1 = WorkerSumP1(1, 100000000, self.printTextEdit)
        # self.workerSumP1.start()

        # 절차적, 객체지향, 함수형 (순수함수)

        # self.workerSumP2 = WorkerSumP2(1, 100000000, self.complete)
        # self.workerSumP2.callbackSignal.connect(self.complete2) #외부에서 시그널 연결
        # self.workerSumP2.callbackSignal.disconnect(self.complete2)
        # self.workerSumP2.callbackSignal.disconnect()

        # self.workerSumP2.handler.connect(self.complete3)
        # self.workerSumP2.handler.connect(self.complete4)
        # self.workerSumP2.handler.connect(self.complete5)
        # self.workerSumP2.handler.disconnect(self.complete3)
        # self.workerSumP2.handler.disconnect(self.complete4)

        # self.workerSumP2.start()


        # 출력공간에 문구 추가 테스트
        # # self.printTextEdit.setText(self.printTextEdit.toPlainText() + inputText)
        # self.printTextEdit.append(inputText)

        # 시리얼통신을 통해 값을 전송
        inputText = self.inputLineEdit.text()
            # 입력된 문구가 숫자인지 파악
            # ½
        # if not inputText.isnumeric(): #숫자표현식도 포함
        # if not inputText.isdecimal(): #정수만
        if not inputText.isdigit(): #숫자
            print("입력된 값이 숫자가 아님")
            return

            # 입력된 문구를 숫자형으로 변경
        inputNum = int(inputText)

            # 입력된 숫자가 일정 범위 안에 있는지 파악 (0-180)
        if inputNum < 0 or inputNum > 180:
            print("입력된 값이 범위를 벗어남")
            return
        # 숫자를 문자로 변경
        # 시리얼 통신을 통해 문자를 전달
        ser.write(str(inputNum).encode())
        
        # 입력된 문구를 초기화 (지우기)
        # print("find: ", inputText.find('\n'))
        self.inputLineEdit.setText('')
        pass

    def complete(self, text):
        print("complete:: text: ", text)
        self.printTextEdit.append(text)
        pass

    def complete2(self, text):
        print("complete2:: text: ", text)
        pass

    def complete3(self, text):
        print("complete3:: text: ", text)
        pass
    def complete4(self, text):
        print("complete4:: text: ", text)
        pass
    def complete5(self, text):
        print("complete5:: text: ", text)
        pass

    def sum(self, low, high):

        total = 0
        for i in range(low, high):
            total += i
        print('sum: ', total)

        # while True:
        #     total = 0
        #     for i in range(low, high):
        #         total += i
        #     print('sum: ', total)

def prepare():


    global ser
    ser = serial.Serial(PORT, baudrate=BAUDRATE)

    pass

if __name__ == '__main__':
    # prepare()

    app = QApplication(sys.argv)
    # app.setStyleSheet("QCheckBox{font-size: 30pt;} QPushButton{font-size: 30pt;}")

    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()

    pass