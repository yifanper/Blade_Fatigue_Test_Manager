'''
Copyright ZHANG Yifan
Email: yifanper@hotmail.com
Wechat: yifaner
'''

import os
import scipy.fftpack
import scipy.optimize
import numpy
import time

#For debug only
def PerformanceAnalysis(func):
    def func_wrapper(*args, **kwargs):
        starting_time=time.time()
        flag=func(*args, **kwargs)
        print('time=%f' %(time.time()-starting_time))
        return flag
    return func_wrapper

def ParseStrainFile(path,format_type,ori_obj):
    #Determine readability
    readability=os.access(path,os.R_OK)
    if not readability:
        return

    #Read file
    with open(path,'r') as f:
        if format_type=='a':
            header=ReadHeaderInfo_1(f)
            strain=ReadStrain_1(f,header['channels'])

    #Data processing
    time_interval=300.0
    points=int(time_interval*header['sampling'])
    freq=[]
    freq.append(Frequency(strain['2-1'],header['sampling']))
    flag=SineFit(strain['2-1'][:1000],header['sampling'],freq[0])
    print(freq)
    ori_obj.StrainParsingFinishedRedirector(flag)

def ReadHeaderInfo_1(f):
    #header['starting_time']
    #      ['sampling']
    #      ['channels']
    header={}
    #f.readline()
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

@PerformanceAnalysis
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

@PerformanceAnalysis
def SineFit(descrete,samp_freq,freq):
    point_no=len(descrete)
    time_interval=1.0/float(samp_freq)
    t=numpy.linspace(0.0,time_interval*float(point_no),point_no,endpoint=False)
    ini_amp=(max(descrete)-min(descrete))/2.0
    ini_mean=numpy.mean(descrete)
    w=2.0*numpy.pi*freq
    ini_phase=0.0

    fit_function=lambda x: x[0]*numpy.sin(w*t+x[1])+x[2]-descrete
    fit_amp,fit_phase,fit_mean=scipy.optimize.leastsq(fit_function,[ini_amp,ini_phase,ini_mean])[0]
    return [fit_amp,fit_phase,fit_mean]

def JumpFilter():
    return