
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QLabel, QFrame, QSizePolicy, 
                                QPushButton, QFileDialog, QMessageBox,
                                QLineEdit, QComboBox,
                                QSpinBox, QSlider, QProgressBar, QHBoxLayout,
                                QCheckBox, QGroupBox
                                )

from PySide2.QtGui import (
    QPixmap, QImage, QColorSpace, 
    QIntValidator, QDoubleValidator, QRegExpValidator,
)

from PySide2.QtCore import Qt, QRegExp

import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.allChecked = False

        self.appleCheckBox = QCheckBox("apple")
        self.grapeCheckBox = QCheckBox("grape")
        self.bananaCheckBox = QCheckBox("banana")


        layout = QVBoxLayout()
        layout.addWidget(self.appleCheckBox)
        layout.addWidget(self.grapeCheckBox)
        layout.addWidget(self.bananaCheckBox)

        self.groupBox = QGroupBox("그룹")
        self.groupBox.setLayout(layout)
        # self.groupBox.setCheckable(True)

        self.button = QCheckBox("전체선택")
        self.button.clicked.connect(self.toggle)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.groupBox)
        mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)
        self.setWindowTitle("QGroupBox QFrame Example")
        # self.resize(500,500)
     
    def toggle(self):
        print("toggle::")   
        # self.groupBox.setChecked(True)
        print(self.allChecked)
        all = not self.allChecked

        # 반전
        # self.appleCheckBox.setChecked(not self.appleCheckBox.isChecked)

        self.appleCheckBox.setChecked(all)
        self.grapeCheckBox.setChecked(all)
        self.bananaCheckBox.setChecked(all)

        self.allChecked = all

        if all:
            self.button.setText("전체해제")

        else:
            self.button.setText("전체선택")



        


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    mainWindow = MainWindow()
    mainWindow.show()

    app.exec_()

