#coding=utf-8

import bftm

path='D:\\BaiduNetdiskDownload\\各家疲劳试验数据\\D161103H0200.txt'
sd=bftm.core.parser.ParseStrainFile(path,'a','unit_test')

'''
Interface:
dic['starting_time']=float
   ['sampling']=int
   ['md5']=tuple
   ['intervals']=tuple
   ['channels']=tuple
   ['channel']['channel_name']['freqency']['interval_no']=float
                              ['amplitude']['interval_no']=float
                              ['mean']['interval_no']=float
                              ['phase']['interval_no']=float
'''

f=open('sd.csv','w')
point_no=len(sd['channel'][sd['channels'][0]]['amplitude'])
f.write('Starting [s],Ending [s],\n')
for n in range(0,point_no):
    for m in sd['channels']:
        pass