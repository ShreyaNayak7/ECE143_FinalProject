# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:03:35 2019

@author: shrey
Editor: Akhil Jain; Jiaye Wang
"""
import pandas as pd
import gather_data as gd
import plot_functions as pf
import continent_country_map as cmap

#load file on health expenditure
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
# beginning_of_path=""
beginning_of_path="../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/"

#file_1="SHA_30052019014114312.csv"
file_1="SHA_01062019033826092.csv"
# file_2="HEALTH_STAT_30052019043359352.csv"
file_2="HEALTH_STAT_01062019034825710.csv"
hl_raw=gd.gather_data_from_csv(beginning_of_path+file_1)
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
lf_raw=gd.gather_data_from_csv(beginning_of_path+file_2)
lf_raw.columns = [c.replace(' ', '_') for c in lf_raw.columns]
lf_c=lf_raw[(lf_raw.Variable=="Total population at birth")]
#format into "country in rows and cols in years" format
lf_piv=pd.pivot_table(lf_c,index='COU',columns='Year',values='Value')

cont_raw=cmap.cont_cou_map(beginning_of_path)

#plot
year=2015
inx=lf_piv.index & hl_piv.index & cont_raw.index
lf=lf_piv.loc[inx]
hl=hl_piv.loc[inx]
cont=cont_raw.loc[inx]
color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
pf.scatter_plot(hl[year],lf[year],cont['Color'],"Life Expectancy Versus Health Expenditure", "Percentage of Gross Domestic Product", "Years",color_map)
###################################
#plot2
#i=0
#for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
#    plt.plot(hl[year][i], lf[year][i], marker,
#             label=lf[year].keys()[i])
#    i=i+1
#plt.xlabel('Health Expenditure, Percentage of Gross Domestic Product')
#plt.ylabel('Life Expectancy,Years')
#plt.legend(loc='upper right', fontsize=10)
#plt.title('Life Expectancy Versus Health Expenditure"')
#plt.show()
