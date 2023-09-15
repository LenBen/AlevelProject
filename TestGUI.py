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

WINDOW_SIZE = 256

class TestGUIWIndow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TestGUI")
        self.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)

def main():
      App = QApplication([])
      Window = TestGUIWIndow()
      Window.show()
      sys.exit(App.exec())

if __name__ == "__main__":
     main()