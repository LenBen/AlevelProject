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

# from comparison import getDifference

# gd = getDifference()

class Step4Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self._initialiseUI()

    def _initialiseUI(self) -> None:        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker 4")
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
        scoreLabel.setText(f"Your score is: -11111 % !")
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
        # self.showFeedback.clicked.connect(self._showFeedback)

        self.showGraph = QPushButton("Show Graph Comparing", self)
        self.showGraph.setFixedSize(150,75)
        self.showGraph.move(170, 275)
        # self.showGraph.clicked.connect(gd.plotGraph)
    
    def _finishRhythmChecker(self):
        QApplication.closeAllWindows()
   
    # def _showFeedback(self):
    #     for i in range(len(gd.scoreValues)):
    #         QMessageBox.information(self, f"Beat {i + 1}",
    #                                 f"""<p>Your score on this beat is:</p>
    #                                  <p>{gd.scoreValues[i]}</p>
    #                                  <p>Where 1 is the best and on time and 4 is the worst and most off rhythm</p> """)

    # def _runClass(*args):
    #     gd.getModelTimes()
    #     gd.compareTimes()

def main():     # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = Step4Window()
    sys.exit(app.exec())

if __name__ =="__main__":
    main()