import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdate
import matplotlib.ticker as ticker


pdf = pd.read_excel('367图.xlsx', sheet_name = [0,1,2,3,4,5,6,7])


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


def millions(y, pos):

    if y > 28 and y <=69 :
         return 'S%d登机口' % (y-28)
    elif y == 70:
        return '临时机位'
    else:
        return 'T%d登机口' %(y)

formatter = FuncFormatter(millions)


fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)

ax.tick_params(axis = 'x',labelsize =18,
                direction='out', colors='g',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='slategrey',
               grid_color='r', grid_alpha=0.5)

plt.xticks(rotation=40)



ax.xaxis.set_major_formatter(mdate.DateFormatter('%d %H:%M'))
ax.xaxis.set_major_locator(mdate.HourLocator(byhour=range(24), interval=5))
plt.yticks(np.arange(1,71,3))



for i in range(8):
    xs1 = pdf[i]['time1']
    xs2 = pdf[i]['time2']
    ys = pdf[i]['y']


    plt.plot_date(x = xs1, y = ys , c='b', marker=r'$\vdash$')
    plt.plot_date(x = xs2, y = ys,  c= 'g' ,marker=r'$\diamondsuit$')


    x = []
    y = []
    for j in range(len(ys)):
        x.append([pdf[i]['time1'][j], pdf[i]['time2'][j]])
        y.append([pdf[i]['y'][j], pdf[i]['y'][j]])
    for j in range(len(ys)):
        plt.plot(x[j], y[j])  




font = {
        'color':  'darkred',
        'weight': 'normal',
        'size': 32,
        }

plt.axvline('2018-01-20 00:00:00' , c= 'r')
plt.axvline('2018-01-21 00:00:00',  c = 'r')

plt.show()