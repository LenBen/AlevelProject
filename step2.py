import sys                      #Importing all of the libraries and classes used in the program

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QMessageBox
)
from PyQt6.QtGui import(
    QIcon,
    QFont,
)

from CreateRhythm import CreateRhythm
from RecordAndPlay import Audio

from step3 import step3Window

cr = CreateRhythm()
audio = Audio()


class Step2Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.checkedBPM = False
        self._initialiseUI()

    def _initialiseUI(self) -> None:        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker 2")
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
        self.bpmText.setText(f"The current BPM is: {cr.getBPM()}")
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
    
    def _checkIfNotEmpty(self, text):
        if text:
            self.submitButton.setDisabled(False)
        elif not text:
            self.submitButton.setDisabled(True)
        else:
            print("Error")
    
    def _setbpm(self) -> None:
        try:
            cr.setBPM(int(self.bpm_Edit.text(), 0))
            self.bpmText.setText(f"The current BPM is: {cr.getBPM()}")
            self.checkedBPM = True
            QMessageBox.information(self, "bpm set to...",f"bpm set to {cr.bpm}",QMessageBox.StandardButton.Ok)
        except:
            QMessageBox.critical(self,
                                      "Character Error",
                                      """<p>The characters inputted are invalid</p>
                                      <p>Please only input numbers</p>""",
    
                                      QMessageBox.StandardButton.Ok)

    def _callNextPage(self):
        if self.checkedBPM:
            working = self.callFuncs()
            if working:
                self.step3 = step3Window()
                self.step3.show()
            else:
                QMessageBox.critical(self,"Critical Error","""There is a critical error try the program again""")
        elif not self.checkedBPM:
            QMessageBox.information(self,"Checked BPM?","""
                                            <p>Have you checked the BPM?</P>
                                    <p>It is set as a default as 120</p>
                                    <p>Click the next button again if you are happy with 120 BPM</p>
                                    <p>Otherwise, submit your own</p>""",QMessageBox.StandardButton.Ok)
            self.checkedBPM = True
    
    def callFuncs(*args) -> bool:
        try:
            cr.GetMusic()
            print("1")
            cr.calculateBeatLength()
            print("2")
            cr.calculateRecLength()
            print()
            audio.setRecordTime(cr.recLength)
            print("4")
            print(audio.record_time)
            return True
        except:
            print("error") 
            return False



    

def main():     # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = Step2Window()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()