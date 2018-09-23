import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#设置字体样式
mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['font.sans-serif']=[u'SimHei']



fig, ax = plt.subplots(figsize=(15, 9), subplot_kw=dict(aspect="equal"))

recipe = ["296  Narrow",
          "72  Wide"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.2f}%\n(航班数:{:d})".format(pct, absolute)

wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=20, weight="bold")


plt.show()