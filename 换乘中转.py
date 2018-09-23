import pandas as pd
from matplotlib import pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']

postage=pd.read_excel('换乘时间分配.xlsx')

fig,ax=plt.subplots(figsize=(10,4))
ax.tick_params(axis = 'x',labelsize =18,
                direction='out', colors='brown',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='brown',
               grid_color='r', grid_alpha=0.5)
ax.step(postage["x"],postage["y"],where='post',color='lightcoral')


#ax.set_title("US Postage Fee") #设置标题
ax.set_xticks([i for i in postage["x"]]) #设置x轴刻度
ax.set_yticks([i for i in postage["y"]]) #去除y轴刻度

plt.xlabel("时间/min",size = 18)
plt.ylabel("中转乘客比率",size = 18)
#添加文字注释
for i,j in zip(postage["x"],postage["y"]):
    ax.text(x=i,y=j+0.003,s=j,size=18)


plt.show()