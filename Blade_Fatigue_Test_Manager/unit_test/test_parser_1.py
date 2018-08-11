#coding=utf-8

import bftm

path='D:\\BaiduNetdiskDownload\\各家疲劳试验数据\\20180426-1.txt'
flag=bftm.core.parser.ParseStrainFile_1(path)
print(flag)