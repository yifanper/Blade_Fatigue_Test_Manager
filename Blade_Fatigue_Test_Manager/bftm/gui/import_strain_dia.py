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
from .. import core

class ImportStrainDataDialog(QDialog):
    def __init__(self,parent):
        super(ImportStrainDataDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        text=('Import Strain Data','导入应变数据')
        self.setWindowTitle(core.common.trans(text))
        self.IniUIElements()
        self.DrawLayout()

    def IniUIElements(self):
        text=('Browse File','选择文件')
        self.browse_button=QPushButton(core.common.trans(text))
        self.browse_button.setFixedWidth(200)
        self.browse_button.clicked.connect(self.BrowseButtonClicked)

    def DrawLayout(self):
        dia_layout=QHBoxLayout()
        dia_layout.addStretch()
        dia_layout.addWidget(self.browse_button)
        self.setLayout(dia_layout)

    def BrowseButtonClicked(self):
        path=QFileDialog.getOpenFileNames(self,"Choose a Project to Open.",\
        mdb.current_path,"文本文档(*.txt)")
        print(path)