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

from CreateRhythm import CreateRhythm
from TestGUI2 import MainWindow

createRhythm = CreateRhythm()

class step2Window(QWidget):
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

        self.bpmText = QLabel(self)
        self.bpmText.setText(f"The current BPM is: {createRhythm.getBPM()}")
        self.bpmText.move(60, 230)
    
    def _createButtons(self):
        self.nextButton = QPushButton("Next", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._callNextPage)

        self.submitButton = QPushButton("Submit", self)
        self.submitButton.setFixedSize(80,30)
        self.submitButton.move(330, 200)
        self.submitButton.setDisabled(True)
        self.submitButton.clicked.connect(self._setbpm)

    def _createLineEdit(self):
        self.bpm_Edit = QLineEdit(self)
        self.bpm_Edit.resize(250,30)
        self.bpm_Edit.move(60,200)
        self.bpm_Edit.textChanged.connect(self._checkIfNotEmpty)
    
    def _callNextPage(self):
        if self.checkedBPM:
            self.mainWindow = MainWindow()
            self.mainWindow.show()
        elif not self.checkedBPM:
            QMessageBox.information(self,"Checked BPM?","""
                                            <p>Have you checked the BPM?</P>
                                    <p>It is set as a default as 120</p>
                                    <p>Click the next button again if you are happy with 120 BPM</p>
                                    <p>Otherwise, submit your own</p>""",QMessageBox.StandardButton.Ok)
            self.checkedBPM = True

    def _checkIfNotEmpty(self, text):
        if text:
            self.submitButton.setDisabled(False)
        elif not text:
            self.submitButton.setDisabled(True)
        else:
            print("Error")

    def _setbpm(self):
        try:
            t = createRhythm.setBPM(int(self.bpm_Edit.text()))
            self.bpmText.setText(f"The current BPM is: {createRhythm.getBPM()}")
            self.checkedBPM = True
            QMessageBox.information(self, "bpm set to...",f"bpm set to {createRhythm.bpm}",QMessageBox.StandardButton.Ok)
        except:
            QMessageBox.critical(self,
                                      "Character Error",
                                      """<p>The characters inputted are invalid</p>
                                      <p>Please only input numbers</p>""",
                                      QMessageBox.StandardButton.Ok)
    


def main():
    app = QApplication(sys.argv)
    window = step2Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()