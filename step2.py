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

class step2Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
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
        self._createLineEdit()
    
    def _createLabels(self):
        titleLabel = QLabel(self)
        titleLabel.setText("Step 2")
        titleLabel.setFont(QFont("Arial", 35))
        titleLabel.move(self.windowSize//3, 30)

        bpmLabel = QLabel(self)
        bpmLabel.setText("BPM:")
        bpmLabel.setFont(QFont("Arial",20))
        bpmLabel.move(60,160)
    
    def _createButtons(self):
        self.nextButton = QPushButton("Next", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._callNextPage)

        self.submitButton = QPushButton("Submit", self)
        self.submitButton.setFixedSize(80,30)
        self.submitButton.move(330, 200)

    def _createLineEdit(self):
        self.bpm_Edit = QLineEdit(self)
        self.bpm_Edit.resize(250,30)
        self.bpm_Edit.move(60,200)
    
    def _callNextPage(self):
        pass

    def _checkIfNotEMpty(self, text):
        if text:
            self.buttonC.setDisabled(False)
        elif not text:
            self.buttonC.setDisabled(True)
        else:
            print("Error")

def main():
    app = QApplication(sys.argv)
    window = step2Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()