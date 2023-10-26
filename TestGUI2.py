import sys
import subprocess as sp
import os
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QProcess
from PyQt6.QtGui import (
     QFont,
     QPixmap,
) 
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QLabel,
    QMessageBox,
    )
from functools import partial


from RecordAndPlay import Audio
from CreateRhythm import CreateRhythm


audio = Audio()
createRhythm = CreateRhythm()


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.displaySize = 40
        self.buttonSize = 60
        self._initialiseUI()
    
    def _initialiseUI(self):
        self.setFixedSize(self.windowSize,self.windowSize)
        self.setWindowTitle("Record and Play")
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self): # Calls the functions to create labels, line edits and buttons
        self._createButtons()
        self._createLineEditTime()
        self._createLabels()

    def _createLabels(self): # creates labels
        title_label = QLabel(self)
        title_label.setText("Record and Play audio")
        title_label.setFont(QFont("Arial", 20))
        title_label.move(self.windowSize//4,30)

        bottom_label = QLabel(self)
        bottom_label.setText("Like a digital Cassette recorder/player!")
        bottom_label.move(15,self.windowSize-20)

        self.time_label = QLabel(self)
        self.time_label.move(80,230)
        self.time_label.setText(f"The record length is set to {audio.getRecordTime()} seconds")
    
    def _createButtons(self): # creates buttons
        self.buttonR = QPushButton("Record", self)
        self.buttonR.move(80,110)
        self.buttonR.setFixedSize(self.buttonSize,self.buttonSize)
        self.buttonR.clicked.connect(audio.record)

        self.buttonP = QPushButton("Play", self)
        self.buttonP.move(80,310)
        self.buttonP.setFixedSize(self.buttonSize,self.buttonSize)
        self.buttonP.clicked.connect(audio.PlayMusic)

        self.buttonC = QPushButton("Enter",self)
        self.buttonC.move(300,208)
        self.buttonC.clicked.connect(self._acceptTime)
        self.buttonC.setDisabled(True)

        self.buttond = QPushButton("Enter",self)
        self.buttond.move(300,455)
        self.buttond.clicked.connect(self._setbpm)

        self.buttonTest = QPushButton("Run the command that runs the library", self)
        self.buttonTest.move(300,300)
        self.buttonTest.clicked.connect(self._runOrchestra)



    def _createLineEditTime(self): # creates the Line
        QLabel("Please enter the recording length below (seconds).",self).move(80,190)

        self.time_edit = QLineEdit(self)
        self.time_edit.resize(210,20)
        self.time_edit.move(80,210)
        self.time_edit.textChanged.connect(self._checkIfNotEmpty)

        self.bpm_edit = QLineEdit(self)
        self.bpm_edit.resize(210,20)
        self.bpm_edit.move(80,460)

    
    def _acceptTime(self):
            t = audio.setRecordTime(self.time_edit.text()) # passes the value of the line edit through to the setter of record_audio

            if not t: # returns an error message if the data is incorrect
                QMessageBox.critical(self,
                                      "Character Error",
                                      """<p>The characters inputted are invalid</p>
                                      <p>Please only input numbers</p>""",
                                      QMessageBox.StandardButton.Ok)
            if t: # if the data is correct it updates the text
                self.time_label.setText(f"The record length is set to {audio.getRecordTime()} seconds")
    
    def _setbpm(self):
        try:
            t = createRhythm.setBPM(int(self.bpm_edit.text()))
            print(createRhythm.bpm)
        except:
            print("no")
        try:
            QMessageBox.information(self, "bpm set to...",f"bpm set to {createRhythm.bpm}",QMessageBox.StandardButton.Ok)
        except:
            print("err")

    
    def _checkIfNotEmpty(self, text): # checks if the line edit is empty. If so the submit button is disabled
        if text:
            self.buttonC.setDisabled(False)
        elif not text:
            self.buttonC.setDisabled(True)
        else:
            print("Error")

    def _runOrchestra(self):
        try:
            a = sp.run(["python", "Orchestra/main.py", "O_Input", "O_Output"])
            a.check_returncode()
        except sp.CalledProcessError as err:
            print(err)
    
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()
        