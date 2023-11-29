import sys
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QStatusBar,
    QPushButton,
    QHBoxLayout,
)
from PyQt6.QtGui import(
    QAction,
    QIcon,
    QFont,

)

from PyQt6.QtCore import (
    Qt,
    QSize,
)

class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.initialiseUI()

    def initialiseUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("The test GUI3 - GUI3 test")
        self.setWindowIcon(QIcon("appLogo.png"))

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.createStatusBar()
        self.show()
    
    def setUpMainWindow(self):
        hBox = QHBoxLayout()

        mainHeader = QLabel(self)
        mainHeader.setText("The Rhythm Checker")
        mainHeader.setFont(QFont("Arial", 25))

        startButton = QPushButton()
        startButton.setText("Start the rhythm checker")
        startButton.setFont(QFont("Arial", 40))

        # self.setCentralWidget(startButton)
        hBox.addWidget(mainHeader)
        hBox.addWidget(startButton)

    def createActions(self):
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

        help_menu = self.menuBar().addMenu("&Help")
    
    def createStatusBar(self):
        statusBar = QStatusBar()
        statusBar.showMessage("The rhythm checker       2023 Lenny S")
        self.setStatusBar(statusBar)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()