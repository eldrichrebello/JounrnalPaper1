# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 14:06:15 2019

@author: Eldrich
"""

import os
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

os.chdir('E:\\University\\data\\Class Work\\Thesis - KTH\\Extra Work\\Papers\\Journal Paper\\V2')
df=pd.read_csv('Delay_Table.csv')

sns.set(style='whitegrid')
#sns.set(rc={'figure.figsize':(11.7,8.27)})
#g=sns.barplot(x=df['Run number'], y=df.Delay, hue=df.Pulse, data=df, color='gray')
#g.despine(left=True)
g=sns.catplot('Run number', 'Delay', 'Pulse', data=df, kind='bar', color='gray', legend=False, aspect=2, size=3)
g.set_ylabels('Delay (s)')
g.set_xlabels(label='')
g.set(ylim=(0,0.5),xlim=g.ax.axes.get_xbound())
sns.despine()
plt.plot([-0.54, 2.5400000000000005], [0.3435263157894737,0.3435263157894737], linewidth=1, linestyle='--', color='k')
#sns.set_context("paper")
plt.annotate('Average',xy=(1,0), xytext=(2,0.35))

plt.tight_layout()