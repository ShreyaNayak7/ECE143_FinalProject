# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:17:25 2019

@author: shrey
"""
import pandas as pd
import gather_data as gd
import matplotlib.pyplot as plt
#%matplotlib notebook
from matplotlib.pyplot import figure
ax = figure(figsize=(10, 6)).gca()

soc_raw=gd.gather_data_from_csv("Social Expenditure.csv")
#clean file: replace space in col names with _, filter, delete unnecessary cols
soc_raw.columns = [c.replace(' ', '_') for c in soc_raw.columns]
soc_c=soc_raw[(soc_raw.Source == "Public") &
              (soc_raw.Branch == "Total") &
              (soc_raw.Type_of_Expenditure == "Total") &
              (soc_raw.Measure == "In percentage of Total General Government Expenditure")]
soc_piv=pd.pivot_table(soc_c,index='Country',columns='Year',values='Value')

soc_col=soc_piv[2010].copy()
soc_col.dropna(inplace=True)
soc_col_ed=soc_col.drop(['Iceland','Slovak Republic','OECD - Total','Latvia','Estonia','Lithuania',
             'Slovenia','Finland','Sweden','Italy','Belgium','Austria','Czech Republic',
             'Portugal','Ireland','Hungary','Switzerland','Netherlands','Norway','Denmark'],inplace=True)

#soc_col=soc_col.iloc[::2]
soc_col.sort_values(ascending=True,inplace=True)
#ax.barh(soc_col,soc_col.index.tolist(),align='center')
ax=soc_col.plot.barh(color='steelblue',alpha=1,zorder=3)
for i, v in enumerate(soc_col):
    ax.text(v+0.5, i - 0.25 , str(round(v))+'%', color='black',fontsize=8)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.xaxis.grid(True,linestyle='--',color='lightgray',zorder=0)
plt.suptitle('Social Expenditure', fontsize=14)
plt.xlabel('% of Government Expenditure', fontsize=11)
plt.savefig('soc_exp.jpg')