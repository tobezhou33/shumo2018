import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd 
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdate
import matplotlib.ticker as ticker
import numpy as np 

df = pd.read_excel('窄2.xlsx')
x = df['x']
y = df['y']


mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']

def millions(x, pos):
    if x > 28 and x <=69 :
         return 'S%d' % (x-28)
    else:
        return 'T%d' %(x)

formatter = FuncFormatter(millions)


fig, ax = plt.subplots()
ax.xaxis.set_major_formatter(formatter)

ax.tick_params(axis = 'x',labelsize =18,
                direction='out', colors='brown',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='brown',
               grid_color='r', grid_alpha=0.5)

plt.bar(x, y, width = 0.5, color=['lightcoral','darkred','indianred','firebrick','brown','maroon','tomato','coral'])


for a,b in zip(x,y):
    plt.text(a, b+0.005, '%d' % b, ha='center', va= 'bottom',fontsize=10)

ax.set_xticks([i for i in x])
plt.xticks(rotation=90)

#plt.xticks(x, ('I + D', 'D + D', 'I + I', 'D + I','I + D', 'D + D', 'I + I', 'D + I'), size = 10)
plt.ylabel('航班数', size = 18)
plt.xlabel('登机口', size = 18)

#plt.title('航班ID类型数量分布图',size = 20, color = 'orangered')
plt.ylim(0,15)

#plt.axvline(4.5 , c= 'r')

plt.show()