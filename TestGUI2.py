import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
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

import pyaudio
import wave
import vlc

from RecordAndPlay import Audio


CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
record_audio = 5
WAVE_OUTPUT_FILENAME = "voice.wav"

audio = Audio()



WINDOW_SIZE = 512
DISPLAY_HEIGHT = 40
BUTTON_SIZE = 60

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self._initialiseUI()
    
    def _initialiseUI(self):
        self.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)
        self.setWindowTitle("Record and Play")
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self):
        # title_label = QLabel(self)
        # title_label.setText("Record and Play audio")
        # title_label.setFont(QFont("Arial", 20))
        # title_label.move(WINDOW_SIZE//4,30)
        self._createButtons()
        self._createLineEditTime()
        self._setUpLabels()

        # bottom_label = QLabel(self)
        # bottom_label.setText("Like a digital Cassette recorder/player!")
        # bottom_label.move(15,WINDOW_SIZE-20)

    def _setUpLabels(self):
        title_label = QLabel(self)
        title_label.setText("Record and Play audio")
        title_label.setFont(QFont("Arial", 20))
        title_label.move(WINDOW_SIZE//4,30)

        bottom_label = QLabel(self)
        bottom_label.setText("Like a digital Cassette recorder/player!")
        bottom_label.move(15,WINDOW_SIZE-20)

        self.time_label = QLabel(self)
        self.time_label.move(80,230)
        self.time_label.setText(f"The record length is set to {audio.getRecordTime()} seconds")
    
    def _createButtons(self):
        self.buttonR = QPushButton("Record", self)
        self.buttonR.move(80,110)
        self.buttonR.setFixedSize(BUTTON_SIZE,BUTTON_SIZE)
        self.buttonR.clicked.connect(audio.record)

        self.buttonP = QPushButton("Play", self)
        self.buttonP.move(80,310)
        self.buttonP.setFixedSize(BUTTON_SIZE,BUTTON_SIZE)
        self.buttonP.clicked.connect(audio.PlayMusic)


    def _createLineEditTime(self):
        QLabel("Please enter the recording length below (seconds).",self).move(80,190)

        self.time_edit = QLineEdit(self)
        self.time_edit.resize(210,20)
        self.time_edit.move(80,210)
        self.time_edit.textChanged.connect(self._checkIfNotEmpty)

        self.buttonC = QPushButton("Enter",self)
        self.buttonC.move(300,208)
        self.buttonC.clicked.connect(self._acceptTime)
        self.buttonC.setDisabled(True)

        # self.time_label = QLabel(self)
        # self.time_label.move(80,230)
    
    def _acceptTime(self):
            # print(time)
            time = self.time_edit.text()
            try:
                t = audio.setRecordTime(time)
            except:
                print("No inputty")
            if t == 55:
                QMessageBox.critical(self,
                                      "Character Error",
                                      """<p>The characters inputted are invalid</p>
                                      <p>Please only input numbers</p>""",
                                      QMessageBox.StandardButton.Ok)
            if t == 0:
                self.time_label.setText(f"The record length is set to {audio.getRecordTime()} seconds")

    
    def _checkIfNotEmpty(self, text):
        if text:
            self.buttonC.setDisabled(False)
        elif not text:
            self.buttonC.setDisabled(True)
        else:
            print("Error")
            


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()
        