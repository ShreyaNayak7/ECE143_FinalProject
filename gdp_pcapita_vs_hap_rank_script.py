# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:01:41 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import plot_functions as pf
import numpy as np

hap_raw=gd.gather_data_from_csv("2017.csv",index='Country')

gdp_cp_raw=gd.gather_data_from_Excel("GDPpercapita.xls",sh_name='Data',index='Country Name')


hap=hap_raw['Happiness.Rank'].dropna()

gdp_cp=gdp_cp_raw['2017']
gdp_cp.replace("nan", np.nan, inplace = True)
gdp_cp.dropna(inplace=True)
#gdp_cp.drop('South Sudan')
hap=hap.drop('South Sudan')

inx=hap.index & gdp_cp_raw.index
hap1=hap.loc[inx]
gdp_cp1=gdp_cp[inx]
pf.scatter_plot(hap1,gdp_cp1,'GDP per cap vs Happiness')
