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

beginning_of_path="../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/"

hap_raw=gd.gather_data_from_csv(beginning_of_path+"2017.csv",index='Country')

# gdp_cp_raw=gd.gather_data_from_Excel("GDPpercapita.xls",sh_name='Data',index='Country Name')
gdp_cp_raw=gd.gather_data_from_Excel(beginning_of_path+"GDPpercapita.xls",sh_name='Data',index='Country Name')

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
# merged.drop(['NER','AFG','LSO','KEN','GIN','GHA','KEN','MMR','PRY','ZMB','BLR','SEN','ARM','LBR','TJK','CAF','BDI','TZA','RWA','TGO'],inplace=True)
merged.drop(['NER','AFG','LSO','KEN','GIN','GHA','KEN','MMR','PRY','ZMB','BLR','SEN','ARM','LBR','TJK','CAF','BDI','TZA','RWA','TGO', 'ZWE','MLI','BEN','BFA','TCD',
    'BTN','MDG','AUS'],inplace=True)
# for element in merged["Happiness.Rank"]:
    # if element
    # if(element<101 or element%2==0):
        # print(element)
        # print(merged[element])
#        drop element
# elements=list(merged)
# for element in merged:
#     if()
# print(merged.index)

cont_raw=cmap.cont_cou_map(beginning_of_path)
cont=cont_raw.loc[merged.index.tolist()]

color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
# print(merged.head)
# print(merged[1])
pf.scatter_plot(merged['2017'],merged['Happiness.Rank'],cont['Color'],'Happiness Rank Versus GDP Per Capita','current US$',"No units",color_map,size_of_figure=[6.4*4,4.8*4])

