#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MenuBar():
    def __init__(self,bar_obj):
        self.RootLevel(bar_obj)

    def RootLevel(self,bar_obj):
        self.file=bar_obj.addMenu('文件')