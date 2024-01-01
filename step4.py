import sys
import typing
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
from CreateRhythm import CreateRhythm

cr = CreateRhythm()

from comparison import getDifference

gd = getDifference()


class step4Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.checkedBPM = False
        self._initialiseUI()
    
    def _initialiseUI(self):
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("Images\\appLogo.png"))
        self._setUpMainWindow()
        self.show()

    def _setUpMainWindow(self):
        self._createLabels()
        self._createButtons()
        
    def _createLabels(self):
        titleLabel = QLabel(self)
        titleLabel.setText("Step 4")
        titleLabel.setFont(QFont("Arial", 35))
        titleLabel.move(self.windowSize//3, 30)

        scoreLabel = QLabel(self)
        scoreLabel.setText(f"Your score is: {gd.score}%")
        scoreLabel.setFont(QFont("Arial", 28))
        scoreLabel.move(self.windowSize//5, 80)

    def _createButtons(self):
        self.nextButton = QPushButton("Finish", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._finishRhythmChecker)

        self.showFeedback = QPushButton("Show feedback", self)
        self.showFeedback.setFixedSize(150,75)
        self.showFeedback.move(170,200)
        self.showFeedback.clicked.connect(self._showFeedback)

        self.showGraph = QPushButton("Show Graph Comparing", self)
        self.showGraph.setFixedSize(150,75)
        self.showGraph.move(170, 275)
        self.showGraph.clicked.connect(gd.plotGraph)
    
    def _finishRhythmChecker(self):
        QApplication.closeAllWindows()
    
    def _showFeedback(self):
        numBeats = len(cr.rhythmList)



def main():

    app = QApplication(sys.argv)
    window = step4Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

