# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:52:25 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import plot_functions as pf

##load file on poverty
##https://data.oecd.org/inequality/poverty-rate.html
pv_raw=gd.gather_data_from_csv("Poverty.csv")
##clean file: replace space in col names with _, filter, delete unnecessary cols
pv_raw.columns = [c.replace(' ', '_') for c in pv_raw.columns]
pv_c=pv_raw[(pv_raw.SUBJECT == "TOT")]
#pv_piv=pv_c
pv_piv=pd.pivot_table(pv_c,index='LOCATION',columns='TIME',values='Value')

#load file on social expenditure
#https://data.oecd.org/inequality/poverty-rate.html
soc_raw=gd.gather_data_from_csv("Social Expenditure.csv")
#clean file: replace space in col names with _, filter, delete unnecessary cols
soc_raw.columns = [c.replace(' ', '_') for c in soc_raw.columns]
soc_c=soc_raw[(soc_raw.Source == "Public") &
              (soc_raw.Branch == "Total") &
              (soc_raw.Type_of_Expenditure == "Total") &
              (soc_raw.Measure == "In percentage of Gross Domestic Product")]
#format into "country in rows and cols in years" format
soc_piv=pd.pivot_table(soc_c,index='COUNTRY',columns='Year',values='Value')

#plot
year=2015
pv=pv_piv[year].dropna()
soc=soc_piv[year].dropna()
inx=soc.index & pv.index
pv=pv.loc[inx]
soc=soc.loc[inx]
pf.scatter_plot(soc,pv,"social expenditure vs poverty")