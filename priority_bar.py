# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:20:42 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib notebook
from matplotlib.pyplot import figure
def mix_plot(merged_df):
    '''
    plot multi-bar graph for each country
    '''

    cmap1 = matplotlib.cm.get_cmap('PuRd')
    ax=merged_df.plot.barh(color=[cmap1(0.3),cmap1(0.6),cmap1(0.9)],alpha=1,zorder=3,figsize=(10,6))

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.grid(True,linestyle='--',color='lightgray',zorder=0)
    plt.suptitle('Expenditure by sector', fontsize=14)
    plt.xlabel('% of Government Expenditure', fontsize=11)
    plt.savefig('pririty_exp.jpg')