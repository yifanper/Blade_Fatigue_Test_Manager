#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .. import media
from .. import mdb

class ImportStrainDataDialog(QDialog):
    def __init__(self,parent):
        super(ImportStrainDataDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle('Rename Load Set')

    def IniUIElements(self):
        pass