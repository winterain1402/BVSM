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
#plt.rc('font',family='Times New Roman')

#plt.rcParams['font.sans-serif'] = ['Times New Roman'] # 设置字体，不然中文无法显示
plt.rcParams['figure.figsize'] = (10.0, 8.0) # 设置figure_size尺寸
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
#plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rc('font', family='Times New Roman')

# 或者直接修改配色方案
#plt.rcParams['axes.color_cycle'] = colors
font_size = 18
def Data_power2_random_TEST():
    #plt.figure()
    plt.figure(1)  # 创建第一个画板（figure）
    plt.subplot(211)  # 第一个画板的第一个子图
    font = FontProperties(fname=r"/home/daiwen/simhei/simhei.ttf",size=15)
    plt.rc('font', family='Times New Roman')
    # plt.axhline(0.3197557 , color='red', linestyle='--')
    # plt.axvline(232, color='black', linestyle='--')
    # plt.axvline(240, color='green', linestyle='--')

    # plt.axhline(0.3197557 , color='red', linestyle='--')
    # plt.axvline(232, color='black', linestyle='--')
    # plt.axvline(240, color='green', linestyle='--')
    plt.ylabel('Time (us)', fontsize=14)
    

    MM = [0.064,0.133,0.30, 0.713, 1.319]
    MM_U = [0.032,0.104,0.23, 0.685, 1.078]
    plt.tick_params(labelsize=14)
    #plt.grid(linestyle='-.', axis='y')

    x = np.arange(len(MM))
    
    a5 = plt.bar(x-0.1, MM, 0.2, color='#30688D', label='MM', align='center')
    a6 = plt.bar(x+0.1, MM_U, 0.2, color='#35B777', label='MM_U', align='center')
    
    plt.legend(labels=['MM','MM_U'], loc='upper left', fontsize=14)
    
    plt.xticks(x, ['(8,8,8)','(16,16,16)','(24,24,24)','(32,32,32)','(40,40,40)'],size=10,rotation=90)
    plt.ylim(0, 1.4)
    plt.savefig('循环展开对不同维度矩阵乘法的性能影响.pdf',format='pdf')

    #plt.show()

if __name__ == '__main__':
    Data_power2_random_TEST()
