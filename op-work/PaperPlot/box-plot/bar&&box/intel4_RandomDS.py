import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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
font_size = 24

data_methods = ['D1', 'D2', 'D3', 'D4', 'D5']
data_results = {
    'D1': [8.7,12.6,13.7,12.9,13.3,13.7,14.5,14.7, 13.4, 13.8],
    'D2': [25.8, 21.4,23.6,23.3,18.2,22.7,25.8,26.4, 17.8, 22.5],
    'D3': [8.5, 4.7, 8.5, 4.9, 4.8, 7.7, 7.3, 8.4, 4.7, 7.0],
    'D4': [23.7, 19.8, 19.6, 14.5, 23.8, 18.8, 14.5, 20.5, 14.4, 13.9],
    'D5': [49.8, 52.7, 31, 48.1, 50.3, 30.7, 30.87, 49.9, 45.5, 30.9]
}

BVSM = {
    'D1': 15.4,
    'D2': 31.6,
    'D3': 5.35,
    'D4': 22.6,
    'D5': 70.0
}


# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图
bar_width = 0.3
index = np.arange(len(data_methods))


for i, method in enumerate(data_methods):
    plt.bar(index[i] - bar_width / 2, BVSM[method], bar_width, color='white', label=method, align='center', edgecolor='k', hatch='/')

# 绘制箱型图
box_data = [data_results[method] for method in data_methods]
ax.boxplot(box_data, positions=index + bar_width / 2, widths=bar_width, manage_ticks=False, showfliers=False)

# 设置轴标签和图例
ax.set_xticks(index,data_methods,size=18)
ax.set_xticklabels(data_methods)
#ax.set_xlabel('Methods',fontsize = 20)
#ax.set_ylabel('Values',fontsize = 20)

#plt.legend(loc='upper left', fontsize=18)

# 显示图形
#plt.tight_layout()
plt.savefig('intel4_RandomDS_mklbatch.pdf',format='pdf', dpi=1000)
#plt.show()
