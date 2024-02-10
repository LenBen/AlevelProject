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

from step1 import step1Window

class MenuScreen(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.displaySize = 40
        self._initialiseUI()

    def _initialiseUI(self):        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("Images\\appLogo.png"))
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self):     # Calls methods to set up the components of the window
        self._createLabels()
        self._createButton()
    
    def _createLabels(self):        # Creates all the text labels in the program
        title_label = QLabel(self)
        title_label.setText("The Rhythm Checker")
        title_label.setFont(QFont("Arial", 35))
        title_label.move(self.windowSize//12,30)

        desc_label = QLabel(self)
        desc_label.setText("Input sheet music and compare with your playing!")
        desc_label.setFont(QFont("Arial",10))
        desc_label.move(self.windowSize//4, 95)

        dec2_label = QLabel(self)
        dec2_label.setText("Check you are playing the correct rhythm!")
        dec2_label.setFont(QFont("Arial",8))
        dec2_label.move(self.windowSize//4,115)

    def _createButton(self):        # Creates the button of the window
        self.startButton = QPushButton("Start the rhythm checker!",self)
        self.startButton.setFixedSize(400, 200)
        self.startButton.setFont(QFont("Arial", 20))
        self.startButton.move(self.windowSize//8,self.windowSize//3)
        self.startButton.clicked.connect(self._callOtherPage)

    def _callOtherPage(self):       # Calls the next page of the program
        self.window = step1Window() 
        self.window.show()

def main():     # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = MenuScreen()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()