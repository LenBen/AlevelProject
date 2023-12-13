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

from step4 import step4Window
from RecordAndPlay import Audio

audio = Audio()

class step3Window(QWidget):
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
        titleLabel.setText("Step 3")
        titleLabel.setFont(QFont("Arial", 35))
        titleLabel.move(self.windowSize//3, 30)

        timeLabel = QLabel(self)
        timeLabel.setText("Recording Length:")
        timeLabel.move(20, 415)
    
    def _createButtons(self):
        self.nextButton = QPushButton("Next", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._callNextPage)

        self.recordButton = QPushButton(self)
        self.recordButton.setIcon(QIcon("Images\\record.png"))
        self.recordButton.setIconSize(QSize(400,250))
        self.recordButton.setFixedSize(400,250)
        self.recordButton.move(self.windowSize//8, self.windowSize//4)
        self.recordButton.clicked.connect(audio.record)

        self.submitButton = QPushButton("SUBMIT",self)
        self.submitButton.setFixedSize(80,30)
        self.submitButton.move(275, 435)
        self.submitButton.setDisabled(True)
        self.submitButton.clicked.connect(self._setTime)
    
    def _createLineEdit(self):
        self.timeEdit = QLineEdit(self)
        self.timeEdit.resize(250,30)
        self.timeEdit.move(20,435)
        self.timeEdit.textChanged.connect(self._checkIfNotEmpty)
    
    def _checkIfNotEmpty(self, text):
        if text:
            self.submitButton.setDisabled(False)
        elif not text:
            self.submitButton.setDisabled(True)
        else:
            print("Error")

    def _setTime(self):
        try:
            time = int(self.timeEdit.text())
            value = audio.setRecordTime(time)
            if value: 
                QMessageBox.information(self,"Accepted",
                                        f"""<p>Value accepted</p>
                                         <p>Time changed to {audio.getRecordTime()}s """,
                                        QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is not accepted</p> """,
                                     QMessageBox.StandardButton.Ok)
        except:
            QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is not accepted</p> """,
                                     QMessageBox.StandardButton.Ok)

    def _callNextPage(self):
        self.step4 = step4Window()
        self.step4.show()

def main():
    app = QApplication(sys.argv)
    window = step3Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()