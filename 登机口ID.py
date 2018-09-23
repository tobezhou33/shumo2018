import matplotlib.pyplot as plt


import matplotlib as mpl

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 5, 21, 37, 2, 2, 1]



mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']

plt.bar(x, y,width = 0.5, color=['indianred','brown','firebrick','maroon','darkred','tomato']  )
for a,b in zip(x,y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=17)
plt.xticks(x, ('I + DI', 'DI + DI', 'I + I', 'D + D', 'DI + D', 'D + DI', 'DI + I'), size = 10)
plt.ylabel('数量', size = 18)
plt.xlabel('到达和出发航班类型', size = 18)
#plt.title('登机口ID类型数量分布图',size = 20, color = 'orangered')
plt.ylim(0,42)
plt.show()



