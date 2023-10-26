import sys
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
)
from PyQt6.QtGui import(
    QAction,
    QIcon
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
        self.setWindowIcon(QIcon("O_Input/music.png"))

        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()
    
    def setUpMainWindow(self):
        pass

    def createActions(self):
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()