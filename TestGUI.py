import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt 
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
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



WINDOW_SIZE = 256
DISPLAY_HEIGHT = 40
BUTTON_SIZE = 40

class TestGUIWIndow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Record Program")
        self.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButton()
    
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButton(self):
         buttonsLayout = QVBoxLayout()
         self.button1 = QPushButton(text="Record")
         self.button1.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
         buttonsLayout.addWidget(self.button1)
         self.button1.clicked.connect(audio.record)

         self.button2 = QPushButton(text="Play")
         self.button2.setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
         buttonsLayout.addWidget(self.button2)

         widget = QWidget()
         widget.setLayout(buttonsLayout)
         self.setCentralWidget(widget)
         self.generalLayout.addLayout(buttonsLayout)
         self.button2.clicked.connect(audio.PlayMusic)


def main():
      App = QApplication([])
      Window = TestGUIWIndow()
      Window.show()
      sys.exit(App.exec())


if __name__ == "__main__":
     main()