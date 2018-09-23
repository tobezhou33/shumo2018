import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#设置字体样式
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']
title = '成功分配航班数量分析'

fig = plt.figure(title, figsize=(8, 7))
fig.tight_layout()
ax = fig.add_subplot(111)
data = [300,100]
labels = ['Wide-body', 'Narrow-body']
explodes =[0 for x in data]
explodes[0] =0.015

def func(pct, data):
    absolute = int(pct/100.*np.sum(data))
    return "{:.1f}%\n(航班数:{:d} )".format(pct, absolute)

ax.pie(data, labels= labels, radius=0.8, #data 是数据，labels 是标签，radius 是饼图半径
       explode=explodes, #explodes 为0 代表不偏离圆心， 不为零则代表偏离圆心的距离
       autopct=lambda pct: func(pct, data), #显示所占比例，百分数
       pctdistance = 0.5,
       labeldistance=1.1,  # a,b,c,d 到圆心的距离
       textprops={'fontsize': 20, 'color': 'black'}) # 标签和比例的格式
plt.axis('equal') # 正圆
plt.legend( loc = 'upper right',bbox_to_anchor=(1.1, 1.05), fontsize=14, borderaxespad=0.3)
# loc =  'upper right' 位于右上角
# bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边
# ncol=2 分两列
# borderaxespad = 0.3图例的内边距
ax.set_title("成功分配航班数量分析",  size = 32, color = 'm')
plt.show()