import PySide2
import PySide2.QtCore
# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtWidgets import QApplication, QWidget, QLabel
import sys
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QWidget()
    # window.resize(289, 170)
    window.resize(400, 500)
    window.setWindowTitle("이것은 나의 첫 QT어플리케이션")

    label = QLabel("Hello 정인", window)
    label.move(110, 80)

    window.show()
    app.exec_()
    print("끝!")