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

class step1Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self._initialiseUI()
    
    def _initialiseUI(self):
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("appLogo.png"))
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self):
        self._createLabels()
    
    def _createLabels(self):
        title_label = QLabel(self)
        title_label.setText("The Rhythm 1")
        title_label.setFont(QFont("Arial", 35))
        title_label.move(self.windowSize//12,30)
    
    def _createButtons(self):
        self.nextButton = QPushButton("Next", self)

def main():
    app = QApplication(sys.argv)
    window = step1Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()