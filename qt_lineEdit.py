
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator,
)


from PySide2.QtCore import QRegExp

import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.lineEdit = QLineEdit()
        self.lineEdit.setReadOnly(True)

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setPlaceholderText("비밀번호를 입력해주세요")
        # self.passwordEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        # self.passwordEdit.setText("asdfasfdaf")
        # self.passwordEdit.text()
        self.passwordEdit.textChanged.connect(self.textChanged)
        self.passwordEdit.editingFinished.connect(self.editingFinished)
        self.passwordEdit.returnPressed.connect(self.returnPressed)

        self.comboBox = QComboBox()
        self.comboBox.addItem("사과")
        self.comboBox.addItem("딸기")
        self.comboBox.addItem("수박")
        self.comboBox.addItem("배")
        # self.comboBox.setEditable(True)
        self.comboBox.setEditable(False)
        self.comboBox.currentIndexChanged.connect(self.onSelected)

        self.validatorLineEdit1 = QLineEdit()
        self.validatorLineEdit1.setValidator(QIntValidator(self))
        self.validatorLineEdit1.setPlaceholderText("정수만 입력하세요")

        self.validatorLineEdit2 = QLineEdit()
        self.validatorLineEdit2.setValidator(QDoubleValidator(self)) 
        self.validatorLineEdit2.setPlaceholderText("실수만 가능합니다")

        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")
        regExp1 = QRegExp("[A-Za-z]*")
        regExp2 = QRegExp("[0-9]*")
        regExp3 = QRegExp("[A-Za-z0-9]*")
        # [ \{\}\[\]\/?.,;:|\)*~`!^\-_+┼<>@\#$%&\'\"\\\(\=]
        self.validatorLineEdit3 = QLineEdit()
        # self.validatorLineEdit3.setValidator(QRegExpValidator(regExp,self)) 
        # self.validatorLineEdit3.setValidator(QRegExpValidator(regExp1,self)) 
        # self.validatorLineEdit3.setValidator(QRegExpValidator(regExp2,self)) 
        self.validatorLineEdit3.setValidator(QRegExpValidator(regExp3,self)) 
        self.validatorLineEdit3.setPlaceholderText("정규식")

        
        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.validatorLineEdit1)
        layout.addWidget(self.validatorLineEdit2)
        layout.addWidget(self.validatorLineEdit3)


        self.setLayout(layout)

        pass

    def textChanged(self):
        text = self.passwordEdit.text()
        print("textChanged:: text:", text)
        self.lineEdit.setText(text)
        pass

    def editingFinished(self):
        print("editingFinished::")
        pass

    def returnPressed(self):
        print("returnPressed::")
        pass

    def onSelected(self):
        print("onSelected::")

        currentIndex = self.comboBox.currentIndex()
        currentText = self.comboBox.currentText()
        p = f"onSelected:: currentIndex: {currentIndex}, currentText: {currentText}"
        print(p)
        pass


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()

