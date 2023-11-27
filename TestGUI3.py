import sys
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QMessageBox,
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
        infoLabel = QLabel("Test test test test")
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(infoLabel)

        container = QWidget()
        container.setLayout(main_v_box)
        self.setCentralWidget(container)

    def createActions(self):
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.triggered.connect(self.close)

        self.about = QAction("&About")
        self.about.setShortcut("Ctrl+A")
        self.about.triggered.connect(self.aboutt)


    def createMenu(self):
        self.menuBar().setNativeMenuBar(False)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

    def aboutt(self):
        QMessageBox.about(self, "About Rhythm Checker",
                          """<p>The rhythm checker program attempt</p>
                          <p>Caption</p>
                          """)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()