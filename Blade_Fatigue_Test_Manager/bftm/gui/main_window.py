#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .. import mdb
from . import data_tree

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('叶片疲劳测试数据处理系统')
        self.IniLayoutElements()
        self.IniLayout()

    def IniLayoutElements(self):
        self.tree=data_tree.DataTree()
        self.statusBar()

    def IniLayout(self):
        self.setMinimumSize(1200, 600)
        self.main_layout=QSplitter()
        self.main_layout.addWidget(self.tree)
        self.main_layout.setOrientation(Qt.Horizontal)

        self.setCentralWidget(self.main_layout)