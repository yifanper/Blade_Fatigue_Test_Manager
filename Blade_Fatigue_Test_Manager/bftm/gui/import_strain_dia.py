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
        text=('Import Strain Data Wizard','导入应变数据向导')
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

        text=('Back','上一步')
        self.back_button=QPushButton(core.common.trans(text))
        self.back_button.setFixedWidth(100)
        self.back_button.setDisabled(True)

        text=('Next','下一步')
        self.next_button=QPushButton(core.common.trans(text))
        self.next_button.setFixedWidth(100)

        text=('Cancel','取消')
        self.cancel_button=QPushButton(core.common.trans(text))
        self.cancel_button.setFixedWidth(100)

    def DrawLayout(self):
        tree_layout=QVBoxLayout()
        self.tree=WizardTree()
        for n in self.tree.items:
            tree_layout.addWidget(n)
        tree_layout.addStretch()

        self.stack=QStackedWidget()

        top_layout=QHBoxLayout()
        top_layout.addLayout(tree_layout)
        v_separator=QFrame()
        v_separator.setFrameShape(QFrame.VLine)
        v_separator.setFrameShadow(QFrame.Sunken)
        top_layout.addWidget(v_separator)
        top_layout.addWidget(self.stack)

        nav_layout=QHBoxLayout()
        nav_layout.addStretch()
        nav_layout.addWidget(self.back_button)
        nav_layout.addWidget(self.next_button)
        nav_layout.addWidget(self.cancel_button)

        dia_layout=QVBoxLayout()
        h_separator=QFrame()
        h_separator.setFrameShape(QFrame.HLine)
        h_separator.setFrameShadow(QFrame.Sunken)
        dia_layout.addLayout(top_layout)
        dia_layout.addWidget(h_separator)
        dia_layout.addLayout(nav_layout)

        self.setLayout(dia_layout)

    def BrowseFileStackWidget(self):
        pass

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

class WizardTree():
    def __init__(self):
        self.items=[]
        text=('Browse Files','选择文件')
        self.items.append(QLabel(core.common.trans(text)))
        self.items.append(QLabel('step 2'))
        self.SetCurrentStep(0)

    def SetCurrentStep(self,current_step):
        if current_step<0 or current_step>=len(self.items):
            return
        done_font=QFont("Times", 8, QFont.Normal)
        current_font=QFont("Times", 8, QFont.Bold)
        todo_font=QFont("Times", 8, QFont.Normal)
        for n in range(0,len(self.items)):
            if n<current_step:
                self.items[n].setFont(done_font)
            elif n==current_step:
                self.items[n].setFont(current_font)
            else:
                self.items[n].setFont(todo_font)

class TypeComboGenerator(QComboBox):
    def __init__(self):
        super(TypeComboGenerator,self).__init__()
        text=('Please select format type','请选择数据格式')
        self.addItem(core.common.trans(text))
        self.addItem('a')