#Copyright ZHANG Yifan

from PyQt5.QtWidgets import *
import sys

import bftm

app=QApplication(sys.argv)
window=bftm.gui.main_window.MainWindow()
window.show()
app.exec_()