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
        title_label = QLabel(self)
        title_label.setText("Record and Play audio")
        title_label.setFont(QFont("Arial", 20))
        title_label.move(WINDOW_SIZE//4,30)
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()
        