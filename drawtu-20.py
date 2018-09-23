import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.dates as mdate
import matplotlib.ticker as ticker


pdf = pd.read_excel('20号图.xlsx', sheet_name = [0,1,2,3,4,5,6,7])


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

#tick_spacing = 5
#ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

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
plt.title('20号到达航班分布图', fontdict=font)

plt.axvline('2018-01-20 00:00:00' , c= 'r')
plt.axvline('2018-01-21 00:00:00',  c = 'r')

plt.show()
  

'''

xs1 = pdf['time1']
xs2 = pdf['time2']
ys = pdf['y']


txt1 = []
for i in range(len(pdf['到达航班'])):
    txt1.append(pdf['到达航班'][i])

txt2 = []
for i in range(len(pdf['出发航班'])):
    txt2.append(pdf['出发航班'][i])



ax.tick_params(axis = 'x',labelsize =10,
                direction='out', colors='g',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='slategrey',
               grid_color='r', grid_alpha=0.5)

for i in range(len(pdf['到达航班'])):
    plt.annotate(txt1[i], xy = (xs1[i], ys[i]),  xytext = (+3, +0),textcoords="offset points")

for i in range(len(pdf['出发航班'])):
    plt.annotate(txt2[i], xy = (xs2[i], ys[i]),  xytext = (-30, +0),textcoords="offset points")

plt.xticks(rotation=70)

ax.xaxis.set_major_formatter(mdate.DateFormatter('%m-%d %H:%M'))
ax.xaxis.set_major_locator(mdate.HourLocator(byhour=range(24), interval=1))


plt.yticks(np.arange(1,71,3))

plt.plot_date(x = xs1, y = ys , c='b',marker=r'$\vdash$')
plt.plot_date(x = xs2, y = ys, c = 'g' ,marker=r'$\diamondsuit$')


x = []
y = []
for i in range(66):
    x.append([pdf['time1'][i], pdf['time2'][i]])
    y.append([pdf['y'][i], pdf['y'][i]])
for i in range(66):
    plt.plot(x[i], y[i])


'''


'''
    txt1 = []
    for j in range(len(pdf[i]['到达航班'])):
        txt1.append(pdf[i]['到达航班'][j])

    txt2 = []
    for j in range(len(pdf[i]['出发航班'])):
        txt2.append(pdf[i]['出发航班'][j])


    for j in range(len(pdf[i]['到达航班'])):
        plt.annotate(txt1[j], xy = (xs1[j], ys[j]),  xytext = (+3, +0),textcoords="offset points")

    for j in range(len(pdf[i]['出发航班'])):
        plt.annotate(txt2[j], xy = (xs2[j], ys[j]),  xytext = (-30, +0),textcoords="offset points")
'''
