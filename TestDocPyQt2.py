import sys                  # Import all the libraries and classes for the program

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMessageBox,
    QLineEdit,
)
from PyQt6.QtGui import(
    QIcon,
    QFont,

)

from PyQt6.QtCore import (
    QSize,
)

from RecordAndPlay import Audio

from TestDocPyQt import Step4Window

audio = Audio()


class step3Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize : int = 512
        self.recorded : bool = False
        self.checkedRecLength : bool = False
        self._initialiseUI()
    
    def _initialiseUI(self) -> None:        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker 3")
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

        self.timeLabel = QLabel(self)
        self.timeLabel.setText(f"Recording Length: {audio.getRecordTime()} s")
        self.timeLabel.move(20, 415)

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
    
    def _checkIfNotEmpty(self, text) -> None:
        if text:
            self.submitButton.setDisabled(False)
        elif not text:
            self.submitButton.setDisabled(True)
        else:
            print("Error")
    
    def _record(self) -> None:
        audio.record()
        self.recorded = True
    
    def _setTime(self) -> None:
        try:
            if self.checkedRecLength:
                time = int(self.timeEdit.text(), 0)
                value = audio.setRecordTime(time)
                if value: 
                    QMessageBox.information(self,"Accepted",
                                        f"""<p>Value accepted</p>
                                         <p>Time changed to {audio.getRecordTime()}s</p> """,
                                        QMessageBox.StandardButton.Ok)
                    self.timeLabel.setText(f"Recording Length: {audio.getRecordTime()} s")
                else:
                    QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is out of range</p> """,
                                     QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.question(self,"Are you sure?",
                                     f"""<p>The recording length is automatically set according to the information given</p>
                                     <p>The current recording length is {audio.getRecordTime()}s</p>
                                     <p>Changing the lenght of the recording may have an effect on the rhythm comparison</p>
                                      <p>If you are sure you want to change the value submit again</p> """,
                                      QMessageBox.StandardButton.Yes)
                self.checkedRecLength = True
        except:
            QMessageBox.critical(self,"Not Accepted",
                                     """<p>The value given is not accepted</p> """,
                                     QMessageBox.StandardButton.Ok)

    def _callNextPage(self) -> None:
        if self.recorded:
            self.step4 = Step4Window()
            self.step4.show()
        else:
            QMessageBox.critical(self,"Not Recording",
                                     """<p>The rhythm checker can't check when there is no recording!</p> """,
                                     QMessageBox.StandardButton.Ok)

        
def main():         # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = step3Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()