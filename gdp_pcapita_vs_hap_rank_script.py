# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:01:41 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import plot_functions as pf
import numpy as np
import continent_country_map as cmap

hap_raw=gd.gather_data_from_csv("2017.csv",index='Country')

gdp_cp_raw=gd.gather_data_from_Excel("GDPpercapita.xls",sh_name='Data',index='Country Name')


hap=hap_raw['Happiness.Rank'].dropna()

gdp_cp=gdp_cp_raw[['Country Code','2017']].copy()
gdp_cp.replace("nan", np.nan, inplace = True)
gdp_cp.dropna(inplace=True)
#gdp_cp.drop('South Sudan')
hap=hap.drop('South Sudan')

inx=hap.index & gdp_cp.index
hap1=hap.loc[inx]
gdp_cp1=gdp_cp.loc[inx.tolist()]
hap_df=hap1.to_frame()
merged = gdp_cp1.merge(hap_df, left_index=True, right_index=True, how='inner')
merged.set_index('Country Code',inplace=True)
merged=merged.drop('XKX')
#merged=merged.iloc[::2]
merged.drop(['NER','AFG','LSO','KEN','GIN','GHA','KEN','MMR','PRY',
             'ZMB','BLR','SEN','ARM','LBR','TJK'],inplace=True)

cont_raw=cmap.cont_cou_map()
cont=cont_raw.loc[merged.index.tolist()]

color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
pf.scatter_plot(merged['2017'],merged['Happiness.Rank'],cont['Color'],'GDP per cap vs Happiness')

