#coding=utf-8

'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

from .. import mdb

def trans(text_list):
    if mdb.language=='ch':
        return text_list[1]
    else:
        return text_list[0]

def ProgramVersionStr():
    version_str='%d.%d.%d' %(mdb.version[0],mdb.version[1],mdb.version[2])
    return version_str

def WindowTitle():
    text=('Blade Fatigue Test Data Manager','叶片疲劳测试数据处理系统')
    title=trans(text)
    title=title+'-V%s' %ProgramVersionStr()
    return title