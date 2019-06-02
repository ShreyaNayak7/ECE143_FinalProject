# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:03:35 2019

@author: shrey
"""
import pandas as pd
import gather_data as gd
import plot_functions as pf

#load file on health expenditure
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
hl_raw=gd.gather_data_from_csv("SHA_30052019014114312.csv")
#clean file: replace space in col names with _, filter, delete unnecessary cols
hl_raw.columns = [c.replace(' ', '_') for c in hl_raw.columns]
hl_c=hl_raw[(hl_raw.Financing_scheme == "All financing schemes") & 
       (hl_raw.Function == "Current expenditure on health (all functions)") &
       (hl_raw.Provider == "All providers") &
       (hl_raw.Measure == "Share of gross domestic product")]
#format into "country in rows and cols in years" format
hl_piv=pd.pivot_table(hl_c,index='LOCATION',columns='Year',values='Value')

#load file on life_expectancy 
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
lf_raw=gd.gather_data_from_csv("HEALTH_STAT_30052019043359352.csv")
lf_raw.columns = [c.replace(' ', '_') for c in lf_raw.columns]
lf_c=lf_raw[(lf_raw.Variable=="Total population at birth")]
#format into "country in rows and cols in years" format
lf_piv=pd.pivot_table(lf_c,index='COU',columns='Year',values='Value')

#colour file, remove duplicate turkey
#https://datahub.io/JohnSnowLabs/country-and-continent-codes-list
cont_raw=gd.gather_data_from_csv("country-and-continent-codes-list.csv",
                             index='Three_Letter_Country_Code')
cont_raw = cont_raw.loc[~cont_raw.index.duplicated(keep='last')]


#plot
year=2015
inx=lf_piv.index & hl_piv.index & cont_raw.index
lf=lf_piv.loc[inx]
hl=hl_piv.loc[inx]
cont=cont_raw.loc[inx]
color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet'}
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
pf.scatter_plot(hl[year],lf[year],cont['Color'],"health expenditure vs life expectancy")


