import matplotlib.pyplot as plt
import seaborn as sns 

import matplotlib as mpl

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [16, 27, 8, 3, 51, 118, 42, 38]



mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']

plt.bar(x, y,width = 0.5, color=['lightcoral','indianred','brown','firebrick','maroon','darkred','tomato','coral']  )
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=17)


plt.xticks(x, ('I + D', 'D + D', 'I + I', 'D + I','I + D', 'D + D', 'I + I', 'D + I'), size = 10)
plt.ylabel('数量', size = 18)
plt.xlabel('到达和出发航班类型', size = 18)

#plt.title('航班ID类型数量分布图',size = 20, color = 'orangered')
plt.ylim(0,125)

plt.text(2, 80, "19号", size=30,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
plt.text(7.5, 80, "20号", size=30,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
plt.axvline(4.5 , c= 'r')
plt.show()