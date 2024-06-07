# -*- coding:utf8 -*
# !/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
#import brewer2mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rc('font',family='Times New Roman')

plt.rcParams['font.sans-serif'] = ['SimHei'] # 设置字体，不然中文无法显示
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.figsize'] = (12.0, 6.0) # 设置figure_size尺寸
#plt.rcParams['figure.figsize'] = (4.0, 4.0) # 设置figure_size尺寸


#figsize(12.5, 4) # 设置 figsize
plt.rcParams['savefig.dpi'] = 500 #保存图片分辨率
plt.rcParams['figure.dpi'] = 500  #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
print(plt.style.available)
plt.style.use('fast')
#plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
#plt.rcParams['image.cmap'] = 'gray' # 设置 颜色 style
# 参照下方配色方案，第三参数为颜色数量，这个例子的范围是3-12，每种配色方案参数范围不相同
#bmap = brewer2mpl.get_map('Set3', 'qualitative', 10)
#colors = bmap.mpl_colors
plt.figure()
plt.rcParams['font.sans-serif'] = ['Times New Roman']
#plt.rc('font', family='Times New Roman')
plt.rc('font', family='Times New Roman')
# 或者直接修改配色方案
#plt.rcParams['axes.color_cycle'] = colors
font_size = 18
def geomean(ls):
    n = len(ls)
    r = 1
    for i in range(n):
       r *= ls[i]
    return pow(r,1/n)

def al_mean(ls):
    return np.average(ls)

def Optimization_time_nor():
    from matplotlib import ticker
    '''
    openblas = [0.303,0.644,0.345,0.591]
    MKL = [2.136,0.545,0.871,0.937]
    MKL_batch = [0.112,0.104,0.129,0.159] 
    '''  
    
    #numpy_openblas = [1.739,0.474,0.543,0.999]
    AnsorTVM = [1,1,1,1]
    MKL = [1.81,1.84,1.82,2.16]
    BVSM = [1.45,1.56,1.09,1.71]
    #AnsorTVM = [0.125,0.078,0.117,0.207]

    fig, ax = plt.subplots()
    plt.ylabel('Speedup (times)', fontsize=18)
    
    font = FontProperties(fname=r"/home/daiwen/simhei/simhei.ttf",size=15)
    #plt.xlabel('i7-9700F上四种随机数据集在BSMM不同优化方法下的时间开销', fontsize=18,fontproperties=font)
    #ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
    plt.tick_params(labelsize=18)
    plt.grid(linestyle=':', axis='y')
    x = np.arange(len(BVSM))
    print(x)
    base = [1,1,1,1,1,1,1]
    '''
    a1 = plt.bar(x-0.3, openblas, 0.1, color='orange', label='openblas', align='center')
    a2 = plt.bar(x-0.2, MKL, 0.1, color='darkcyan', label='MKL', align='center')
    a3 = plt.bar(x-0.1, MKL_batch, 0.1, color='green', label='MKL_batch', align='center')
    '''
    #a4 = plt.bar(x-0.3, numpy_openblas, 0.2, color='blue', label='numpy+openblas', align='center')
    a5 = plt.bar(x-0.2, AnsorTVM, 0.2, color='black', label='AnsorTVM', align='center')
    a6 = plt.bar(x, MKL, 0.2, color='white', label='Intel-MKL-vbatch', align='center', edgecolor='k', hatch='/')
    a7 = plt.bar(x+0.2, BVSM, 0.2, color='white', label='BVSM', align='center', edgecolor='k', hatch='')
    
    
        
    #plt.axhline(1.0, color='red',lw=1,linestyle='--')
    plt.xticks(x, ['AIDS', 'BZR','COX2','DHFR'],size=18,rotation=0)
    plt.ylim(0.0, 4.0)
    plt.legend(loc='upper left', fontsize=18)
    plt.savefig('intel4_CPU_BaseLine_TUDataset.pdf',format='pdf', dpi=1000)
    plt.show()

if __name__ == '__main__':
    Optimization_time_nor()
