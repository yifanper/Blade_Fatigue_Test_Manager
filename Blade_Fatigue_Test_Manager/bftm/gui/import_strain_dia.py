#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

from .. import media
from .. import mdb
from .. import core

#Python version dependent packages
if mdb.python_version==3:
    import _thread as thread
else:
    import thread

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

        self.file_table=QTableWidget(2,2)
        header=(('File Names','文件名'),('Format Type','文件格式'))
        self.file_table.setHorizontalHeaderLabels(core.common.trans(header))
        self.file_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.file_table.setColumnWidth(0,300)
        self.file_table.setColumnWidth(1,200)

    def DrawLayout(self):
        dia_layout=QHBoxLayout()
        dia_layout.addStretch()
        dia_layout.addWidget(self.file_table)
        dia_layout.addWidget(self.browse_button)
        self.setLayout(dia_layout)

    def BrowseButtonClicked(self):
        text1=('Select a Strain Data File','请选择应变数据文件')
        text2=('Plain Text(*.txt)','文本文档(*.txt)')
        path=QFileDialog.getOpenFileNames(self,core.common.trans(text1),\
        mdb.current_path,core.common.trans(text2))
        if not len(path[0])==0:
            self.StrainFileBrowsed(path)
            #thread.start_new_thread(core.parser.ParseStrainFile,(path[0][0],'a',self,))

    def StrainFileBrowsed(self,path):
        file_no=len(path[0])
        self.file_table.setRowCount(file_no)
        for n in range(0,file_no):
            file_name=os.path.splitext(path[0][n])
            file_name=file_name[0]+file_name[1]
            cell_item=QTableWidgetItem('%s' %file_name)
            self.file_table.setItem(n,0,cell_item)
            cell_item=TypeComboGenerator()
            self.file_table.setCellWidget(n,1,cell_item)

    def StrainParsingFinishedRedirector(self,result):
        pass

class TypeComboGenerator(QComboBox):
    def __init__(self):
        super(TypeComboGenerator,self).__init__()
        text=('Please select format type','请选择数据格式')
        self.addItem(core.common.trans(text))
        self.addItem('a')