import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

pdf = pd.read_excel('19号图.xlsx')


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

#pdf.set_index(["time3"], inplace=True)
xs = pdf['x']
ys = pdf['y']

txt = []
for i in range(len(pdf['hangban'])):
    txt.append(pdf['hangban'][i])




ax.tick_params(axis = 'x',labelsize =10,
                direction='out', colors='g',
               grid_color='r', grid_alpha=0.5)

ax.tick_params(axis = 'y',which= 'major',labelsize =18,
                direction='out', colors='slategrey',
               grid_color='r', grid_alpha=0.5)

#plt.xticks(np.arange(0,108,1), rotation=40)


#plt.ylabel('不同登机口')


plt.scatter(x = xs, y = ys, c="blue")

for i in range(108):
    plt.annotate(txt[i], xy = (xs[i], ys[i]),  xytext = (xs[i], ys[i]))

x = []
y = []
for i in range(54):
    x.append([pdf['time1'][i], pdf['time2'][i]])
    y.append([pdf['y'][i], pdf['y'][i]])
for i in range(54):
    plt.plot(x[i], y[i])

plt.xticks( rotation=90)
plt.yticks(np.arange(1,71,3))
#plt.ylabel('不同登机口')

'''
for i in range(54):
    plt.plot()
'''
tick_spacing = 5
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
font = {
        'color':  'darkred',
        'weight': 'normal',
        'size': 32,
        }
plt.title('19号到达航班分布图', fontdict=font, backgroundcolor='lavender' )

plt.show()
