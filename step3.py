import sys
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMessageBox,
    QLineEdit
)
from PyQt6.QtGui import(
    QIcon,
    QFont

)

from PyQt6.QtCore import (
    QSize,
)

from step4 import Step4Window
from comparison import getDifference
import step2

gd = getDifference()

class step3Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.checkedRecLength = False
        self.recorded = False
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
        timeLabel.setText(f"Recording Length: {step2.audio.getRecordTime()}")
        print(step2.audio.getRecordTime())
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
        self.recordButton.clicked.connect(self._record)

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
    
    def _record(self):
        step2.audio.record()
        self.recorded = True

    def _setTime(self):
        try:
            if self.checkedRecLength:
                time = float(self.timeEdit.text())
                value = step2.audio.setRecordTime(time)
                if value: 
                    QMessageBox.information(self,"Accepted",
                                        f"""<p>Value accepted</p>
                                         <p>Time changed to {step2.audio.getRecordTime()}s</p> """,
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is out of range</p> """,
                                     QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.question(self,"Are you sure?",
                                     f"""<p>The recording length is automatically set according to the information given</p>
                                     <p>The current recording length is {step2.audio.getRecordTime()}s</p>
                                     <p>Changing the lenght of the recording may have an effect on the rhythm comparison</p>
                                      <p>If you are sure you want to change the value submit again</p> """,
                                      QMessageBox.StandardButton.Yes)
                self.checkedRecLength = True
        except:
            QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is not accepted</p> """,
                                     QMessageBox.StandardButton.Ok)

    def _callNextPage(self):
        if self.recorded:
            try:
                self._callFuncs()
                self.step4 = Step4Window()
                self.step4.show()
            except Exception as e:
                print(e)
        else:
            QMessageBox.critical(self,"Not Recording",
                                     """<p>The rhythm checker can't check when there is no recording!</p> """,
                                     QMessageBox.StandardButton.Ok)

    def _callFuncs(*args):
        gd.getModelTimes()
        gd.compareTimes()
        print(gd.modelArray)
        print(gd.audioArray)

def main():
    app = QApplication(sys.argv)
    window = step3Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
