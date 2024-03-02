import sys                  # Import all the libraries and classes for the program
import typing
from PyQt6 import QtCore

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QMessageBox,
    QFileDialog,
)
from PyQt6.QtGui import(
    QIcon,
    QFont,

)

from PyQt6.QtCore import (
    QSize,
    QUrl,
)

from PIL import Image

from step2 import Step2Window

class step1Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.windowSize = 512
        self.uploadedImage = False
        self._initialiseUI()
    
    def _initialiseUI(self):        # Initialise the size, title and icon of the window.
        self.setFixedSize(self.windowSize, self.windowSize)
        self.setWindowTitle("The Rhythm Checker")
        self.setWindowIcon(QIcon("Images\\appLogo.png"))
        self._setUpMainWindow()
        self.show()
    
    def _setUpMainWindow(self):     # Calls methods to set up the components of the window
        self._createLabels()
        self._createButtons()
    
    def _createLabels(self):        # Creates all the text labels in the program
        title_label = QLabel(self)
        title_label.setText("Step 1")
        title_label.setFont(QFont("Arial", 35))
        title_label.move(self.windowSize//3,30)
    
    def _createButtons(self):       # Creates the button of the window
        self.nextButton = QPushButton("Next", self)
        self.nextButton.setFixedSize(100,50)
        self.nextButton.move(400,450)
        self.nextButton.clicked.connect(self._callNextPage)

        self.uploadButton = QPushButton("",self)
        self.uploadButton.setIcon(QIcon("Images\\upload.png"))
        self.uploadButton.setIconSize(QSize(400,250))
        self.uploadButton.setFixedSize(400,250)
        self.uploadButton.move(self.windowSize//8, self.windowSize//4)
        self.uploadButton.clicked.connect(self._uploadFile)
    
    def _callNextPage(self):        # Calls the next class if an image has been uploaded
        if self.uploadedImage:
            self.window = Step2Window()
            self.window.show()
        else:
            QMessageBox.critical(self, "File needed",
                                 """<p>To go to the next step, a file must be uploaded</p>
                                 <p>Please upload a file</p>""",
                                 QMessageBox.StandardButton.Ok)
    
    def _uploadFile(self):      # Uploads the file
        rhythmFile = QFileDialog.getOpenFileUrl(self, "Open Rhythm File",       # Opens the file via the path of the file
                                                QUrl("C://"), "Image Files(*.jpg *.jpeg *.png)")
        
        try:
            image = Image.open(QUrl.toLocalFile(rhythmFile[0]))
            image = image.save("O_Input\\music.png")        # Saves the file 
        except Exception as e:
            print(e)

        self.uploadedImage = True
    

        
def main():         # Function if the file is run by itself
    app = QApplication(sys.argv)
    window = step1Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()