import sys

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

WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40
ERROR_MSG = "ERROR #9999"

class PyCalcWindow(QMainWindow):
    #This is the main window of the calculator program

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Calc")
        self.setFixedSize(WINDOW_SIZE,WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
         self.display = QLineEdit()
         self.display.setFixedHeight(DISPLAY_HEIGHT)
         self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
         self.display.setReadOnly(True)
         self.generalLayout.addWidget(self.display)
    
    def _createButtons(self):
         self.buttonMap = {}
         buttonsLayout = QGridLayout()
         KeyBoard = [
              ["7","8","9","/","C"],
              ["4","5","6","*","("],
              ["2","2","3","-",")"],
              ["0","00",".","+","="]
         ]

         for row, keys in enumerate(KeyBoard):
              for col, key in enumerate(keys):
                   self.buttonMap[key] = QPushButton(key)
                   self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                   buttonsLayout.addWidget(self.buttonMap[key], row, col)
         self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self,text:str) -> None:
         self.display.setText(text)
         self.display.setFocus()
    
    def displayText(self) -> str:
         return self.display.text()
    
    def clearDisplay(self):
         self.setDisplayText("")

class PyCalc:
     def __init__(self, model, view):
          self._evaluate = model
          self._view = view
          self._connectSignalsAndSlots()
    
     def _calculateResults(self):
          result = self._evaluate(expression=self._view.displayText())
          self._view.setDisplayText(result)

     def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)
    
     def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
             if keySymbol not in {"=","C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResults)
        self._view.display.returnPressed.connect(self._calculateResults)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
                

def evaluateExpression(expression):
     try:
          result = str(eval(expression, {}, {}))
     except Exception:
          result = ERROR_MSG
     return result



def main():
      pycalcApp = QApplication([])
      pycalcWindow = PyCalcWindow()
      pycalcWindow.show()
      PyCalc(model=evaluateExpression, view=pycalcWindow)
      sys.exit(pycalcApp.exec())

if __name__ == "__main__":
      main()