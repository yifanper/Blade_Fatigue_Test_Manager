#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from .. import core

class MenuBar():
    def __init__(self,bar_obj):
        self.RootLevel(bar_obj)

    def RootLevel(self,bar_obj):
        text=('File','文件')
        self.file=bar_obj.addMenu(core.common.trans(text))
        text=('Import','导入')
        self.import_data=bar_obj.addMenu(core.common.trans(text))
        text=('Help','帮助')
        self.help=bar_obj.addMenu(core.common.trans(text))