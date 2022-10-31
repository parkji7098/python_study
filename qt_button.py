
from tokenize import group
import PySide2
import PySide2.QtCore

# print("PySide2 version: ", PySide2.__version__)
# print("QtCore version: ", PySide2.QtCore.qVersion())

from PySide2.QtCore import Qt
# from PySide2.QtGui import QIcon
# from PySide2.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QCheckBox, QGroupBox
from PySide2.QtWidgets import *
import sys

class MyForm(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Button Demo")

        self.button = QPushButton("OK", self)
        self.button.clicked.connect(self.okButtonClicked)

        self.checkBox = QCheckBox('Case Sensitivity', self)
        self.checkBox.toggled.connect(self.onCaseSensitivity)

        box = QGroupBox("Sex", self)

        self.button1 = QRadioButton("Male", box)
        self.button2 = QRadioButton("Female", box)
        self.button1.setChecked(True)

        groupBoxLayout = QVBoxLayout(box)
        groupBoxLayout.addWidget(self.button1)
        groupBoxLayout.addWidget(self.button2)
        self.button1.toggled.connect(self.onCaseSensitivity)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.button)
        mainLayout.addWidget(self.checkBox)
        mainLayout.addWidget(box)

        self.setLayout(mainLayout)
        pass

    def okButtonClicked(self):
        print("okButtonClicked")

    def onCaseSensitivity(self, toggle):
        print("onCaseSensitivity", toggle)
        print(self.checkBox.isChecked())

    def onMale(self, toggle):
        # print('male')
        print('onMale', toggle)

if __name__ == '__main__':
    app = QApplication(sys.argv)


    form = MyForm()
    form.show()

    app.exec_()
    print("끝!")