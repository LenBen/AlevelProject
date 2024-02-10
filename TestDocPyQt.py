import sys                      #Importing all of the libraries and classes used in the program
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
)
from PyQt6.QtGui import(
    QIcon,
    QFont,
)


class Step2Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.displaySize = 40
        self._initialiseUI()

    def _initialiseUI(self):        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("Images\\appLogo.png"))
        self.show()

    

def main():     # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = Step2Window()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()