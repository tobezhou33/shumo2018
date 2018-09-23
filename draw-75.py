import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdate
import matplotlib.ticker as ticker

pdf = pd.read_excel('temp1.xlsx')


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

fig, ax = plt.subplots()

ax.tick_params(axis = 'x',labelsize =18,
                direction='out', colors='brown',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='lightcoral',
               grid_color='r', grid_alpha=0.5)

plt.xticks(rotation=40)

ax.xaxis.set_major_formatter(mdate.DateFormatter('%d %H:%M'))
ax.xaxis.set_major_locator(mdate.HourLocator(byhour=range(24), interval=5))

plt.yticks(np.arange(1,180,10))
plt.ylim(1, 180)

xs1 = pdf['到达时间']
xs2 = pdf['出发时间']
ys = pdf['y']

plt.plot_date(x = xs1, y = ys , c='b', marker=r'$\vdash$')
plt.plot_date(x = xs2, y = ys,  c= 'g' ,marker=r'$\diamondsuit$')

x = []
y = []
for i in range(177):
    x.append([pdf['到达时间'][i], pdf['出发时间'][i]])
    y.append([pdf['y'][i], pdf['y'][i]])
for i in range(177):
    plt.plot(x[i], y[i])

font = {
        'color':  'darkred',
        'weight': 'normal',
        'size': 32,
        }
#plt.title('原始航班分布图', fontdict=font )


plt.axvline('2018-01-20 00:00:00' , c= 'r')
plt.axvline('2018-01-21 00:00:00',  c = 'r')

plt.show()
