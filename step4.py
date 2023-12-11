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
    QLineEdit
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

class step4Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.checkedBPM = False
        self._initialiseUI()
    
    def _initialiseUI(self):
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("Images\\appLogo.png"))
        self._setUpMainWindow()
        self.show()

    def _setUpMainWindow(self):
        self._createLabels()
        self._createButtons()
        
    def _createLabels(self):
        titleLabel = QLabel(self)
        titleLabel.setText("Step 4")
        titleLabel.setFont(QFont("Arial", 35))
        titleLabel.move(self.windowSize//3, 30)

    def _createButtons(self):
        self.nextButton = QPushButton("Finish", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._finishRhythmChecker)
    
    def _finishRhythmChecker(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = step4Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

