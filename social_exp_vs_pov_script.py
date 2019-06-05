# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:52:25 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import plot_functions as pf
import continent_country_map as cmap

##load file on poverty
##https://data.oecd.org/inequality/poverty-rate.html
# pv_raw=gd.gather_data_from_csv("Poverty.csv")
pv_raw=gd.gather_data_from_csv("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/DP_LIVE_04062019115820354.csv")
##clean file: replace space in col names with _, filter, delete unnecessary cols
pv_raw.columns = [c.replace(' ', '_') for c in pv_raw.columns]
pv_c=pv_raw[(pv_raw.SUBJECT == "TOT")]
#pv_piv=pv_c
pv_piv=pd.pivot_table(pv_c,index='LOCATION',columns='TIME',values='Value')

#load file on social expenditure
#https://data.oecd.org/inequality/poverty-rate.html
# soc_raw=gd.gather_data_from_csv("Social Expenditure.csv")
soc_raw=gd.gather_data_from_csv("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/SOCX_AGG_04062019103440530.csv")
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
color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
cont_raw=cmap.cont_cou_map("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/")
inx=soc_piv.index & pv_piv.index & cont_raw.index
cont=cont_raw.loc[inx]
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
pf.scatter_plot(soc,pv,cont['Color'],"Poverty Rate (0-year-olds to 17-year-olds) Versus Social Expenditure", "Percentage of GDP", "no units",color_map)
