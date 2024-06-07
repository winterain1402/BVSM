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
plt.rcParams['figure.figsize'] = (12.0, 7.0) # 设置figure_size尺寸
#plt.rcParams['figure.figsize'] = (4.0, 4.0) # 设置figure_size尺寸


#figsize(12.5, 4) # 设置 figsize
plt.rcParams['savefig.dpi'] = 500 #保存图片分辨率
plt.rcParams['figure.dpi'] = 500  #分辨率
# 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
# 指定dpi=200，图片尺寸为 1200*800
# 指定dpi=300，图片尺寸为 1800*1200
print(plt.style.available)
plt.style.use('fast')
plt.figure()
plt.rcParams['font.sans-serif'] = ['Times New Roman']
#plt.rc('font', family='Times New Roman')
plt.rc('font', family='Times New Roman')

# 或者直接修改配色方案
#plt.rcParams['axes.color_cycle'] = colors
font_size = 18
def Data_power2_random_TEST():
    #plt.figure()
    font = FontProperties(fname=r"/home/daiwen/simhei/simhei.ttf",size=15)
    plt.rc('font', family='Times New Roman')
    plt.figure(1)  # 创建第一个画板（figure）
    plt.subplot(211)  # 第一个画板的第一个子图
    font = FontProperties(fname=r"/home/daiwen/simhei/simhei.ttf",size=15)
    plt.rc('font', family='Times New Roman')
    plt.ylabel('Speedup(x)', fontsize=18)
    #plt.xlabel('Auto_unroll_max_step', fontsize=14)
    #plt.axhline(0.244, color='black', linestyle='--',linewidth=2)

    #CPU intel3
    y_1 = [2.76,3.9,3.05,5.69,3.59]
    #CPU intel4
    y_2 = [1.54,1.91,4.045,1.54,1.84]

    plt.tick_params(labelsize=14)
    plt.grid(linestyle='-.', axis='y')

    x = np.arange(len(y_1))

    #l1 = plt.scatter(x, y_1, color='deepskyblue', linewidth='4',marker='+')
    #l2 = plt.scatter(x, y_1, color='green', linewidth='3',marker='*')
    #l3 = plt.scatter(x, y_3, color='black', linewidth='4',marker='o')

    plt.plot(x, y_1, color="black", linewidth=3, linestyle='-', label='JJ income')
    plt.plot(x, y_2, color="black", linewidth=3, linestyle='--', label='JJ income')

    
    plt.legend(labels=['M1','M2'], loc='upper right', fontsize=14)
    #plt.axhline(1.0, color='black',lw=3,linestyle='--')
    plt.xticks(x, ['D1', 'D2', 'D3', 'D3', 'D5'],size=18,rotation=0)
    plt.ylim(0, 6.0)

    plt.savefig("CPU_intel3_test.pdf",format='pdf')

    #plt.show()

if __name__ == '__main__':
    Data_power2_random_TEST()
