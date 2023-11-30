import sys
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QStatusBar,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QMessageBox,
)
from PyQt6.QtGui import(
    QAction,
    QIcon,
    QFont,

)

from PyQt6.QtCore import (
    Qt,
    QSize,
)

class MenuScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.displaySize = 40
        self._initialiseUI()

    def _initialiseUI(self):
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("appLogo.png"))
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self):
        self._createLabels()
        self._createButton()
    
    def _createLabels(self):
        title_label = QLabel(self)
        title_label.setText("The Rhythm Checker")
        title_label.setFont(QFont("Arial", 35))
        title_label.move(self.windowSize//12,30)

        desc_label = QLabel(self)
        desc_label.setText("Input sheet music and compare with your playing!")
        desc_label.setFont(QFont("Arial",10))
        desc_label.move(self.windowSize//4, 95)

    def _createButton(self):
        self.startButton = QPushButton("Start the rhythm checker!",self)
        self.startButton.setFixedSize(400, 200)
        self.startButton.move(self.windowSize//8,self.windowSize//3)

def main():
    app = QApplication(sys.argv)
    window = MenuScreen()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()