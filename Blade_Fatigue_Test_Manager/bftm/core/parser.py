'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

import os
import scipy.fftpack
import numpy
import time

def ParseStrainFile_1(path):
    readability=os.access(path,os.R_OK)
    if not readability:
        return
    with open(path,'r') as f:
        header=ReadHeaderInfo_1(f)
        strain=ReadStrain_1(f,header['channels'])
        freq=[]
        for n in header['channels']:
            freq.append(Frequency(strain[n],header['sampling']))
    return freq

def ReadHeaderInfo_1(f):
    #header['starting_time']
    #      ['sampling']
    #      ['channels']
    header={}
    f.readline()
    line_content=f.readline()
    sampling_str=''
    for n in line_content:
        if n.isdigit():
            sampling_str=sampling_str+n
    header['sampling']=int(sampling_str)
    line_content=f.readline()
    line_elements=line_content.split()
    header['channels']=line_elements[1:]
    return header

def ReadStrain_1(f,channels):
    #strain['channel name']
    #      ['time']
    strain={}
    strain['time']=[]
    for key in channels:
        strain[key]=[]
    while 1:
        line_content=f.readline()
        line_elements=line_content.split()
        if len(line_elements)==0:
            break
        strain['time'].append(float(line_elements[0]))
        for n in range(0,len(channels)):
            strain[channels[n]].append(float(line_elements[n+1]))
    return strain

def Frequency(descrete,samp_freq):
    #descrete is a tuple of strains
    #samp_freq is a float indicating sampling frequency [Hz]
    value_no=len(descrete)
    value_no_f=float(value_no)
    x=(float(n)/samp_freq for n in range(0,value_no))
    yf=scipy.fftpack.fft(descrete)
    xf=[]
    sample_time=1.0/samp_freq
    for n in range(0,int(value_no/2)):
        xf.append(1.0/(2.0*sample_time)/(value_no_f/2.0)*float(n))
    xf=xf[1:]
    yf2=[]
    for n in range(1,int(value_no/2)):
        yf2.append(2.0/value_no_f*numpy.abs(yf[n]))
    freq=xf[yf2.index(max(yf2))]
    return freq