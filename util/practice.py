import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("hello PyQt")
label.show()
app.exec_()