#coding=utf-8

import bftm

path='D:\\BaiduNetdiskDownload\\各家疲劳试验数据\\D161103H0200.txt'
flag=bftm.core.parser.ParseStrainFile(path,'a',None)
print(flag)