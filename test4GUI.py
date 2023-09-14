import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QFormLayout,
    QLineEdit,
    QLabel, 
    QWidget,
    QGridLayout,
    QFormLayout,
    QPushButton,
    QVBoxLayout
    )
from functools import partial

def greet(name: str):
    if msglabel.text():
        msglabel.setText("")
    else:
        msglabel.setText(f"Hello there {name}")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Sigmals and slots")
layout = QVBoxLayout()

button = QPushButton("Grreet")
button.clicked.connect(partial(greet,"Nicholas Demitiu"))

layout.addWidget(button)
msglabel = QLabel()
layout.addWidget(msglabel)
window.setLayout(layout)


# layout = QGridLayout()
# layout.addWidget(QPushButton("(0,0)"), 0, 0)
# layout.addWidget(QPushButton("Center 01"), 0, 1)
# layout.addWidget(QPushButton("Bottom10"), 1, 0)
# layout.addWidget(QPushButton("1,1"), 1, 1)
# layout.addWidget(QPushButton("5,5"),5 ,5)
# window.setLayout(layout)

# layout = QFormLayout()
# layout.addRow("Name:", QLineEdit())
# layout.addRow("Age:", QLineEdit())
# layout.addRow("Job:", QLineEdit())
# layout.addRow("Hobbies:", QLineEdit())
# window.setLayout(layout)

# window.setGeometry(200, 300, 350, 100)
# helloMsg = QLabel("<h1>Hello, Worlgd!</h1>", parent=window)
# helloMsg.move(60, 15)
# towMsg = QLabel("<p>this is a final thing it works on windows</p><p>but not on linux i hate it</p>", parent=window)
# towMsg.move(30, 70)

window.show()

sys.exit(app.exec())