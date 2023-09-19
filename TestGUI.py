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
    QVBoxLayout
    )
from functools import partial

import pyaudio
import wave

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
record_audio = 5
WAVE_OUTPUT_FILENAME = "voice.wav"



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
         self.generalLayout.addLayout(buttonsLayout)
         self.button1.clicked.connect(record)

def record():
     
     p = pyaudio.PyAudio()
     stream = p.open(rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=True,
                frames_per_buffer=CHUNK)
     frames = []

     print("recording start **")

     for i in range(0, int(RATE / CHUNK * record_audio)):
        data = stream.read(CHUNK)
        frames.append(data)

     print("** recording ended")

     stream.stop_stream()
     stream.close()
     p.terminate()

     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
     wf.setnchannels(CHANNELS)
     wf.setsampwidth(p.get_sample_size(FORMAT))
     wf.setframerate(RATE)
     wf.writeframes(b''.join(frames))
     wf.close()

def PlayMusic():
     f = wave.open("voice.wav", "rb")
     p = pyaudio.PyAudio()
     stream = p.open(rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=True,
                frames_per_buffer=CHUNK)
     data = f.readframes(CHUNK)
     while data:
          stream.write(data)
          data = f.readframes(CHUNK)
     stream.stop_stream()
     stream.close()
     p.terminate()

def main():
      App = QApplication([])
      Window = TestGUIWIndow()
      Window.show()
      sys.exit(App.exec())


if __name__ == "__main__":
     main()