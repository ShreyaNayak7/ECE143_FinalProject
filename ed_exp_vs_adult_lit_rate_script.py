# -*- coding: utf-8 -*-
"""
Created on Thu May 30 23:43:26 2019

@author: shrey
"""

import pandas as pd
import gather_data as gd
import plot_functions as pf
import continent_country_map as cmap

file_for_adult_literacy_rate="../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/EDULIT_DS_04062019033100321.csv"

# ed_raw=gd.gather_data_from_Excel("Education expenditure.xls",sh_name='Data',
#                                 header=3,index='Country Code')
ed_raw=gd.gather_data_from_Excel("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/API_SE.XPD.TOTL.GD.ZS_DS2_en_excel_v2_10576899.xls",sh_name="Data",header=3,index="Country Code")
ed_piv=ed_raw
lit_raw=gd.gather_data_from_csv(file_for_adult_literacy_rate)
# lit_raw=gd.gather_data_from_csv("EDULIT_DS_31052019025144633.csv")
lit_raw.columns = [c.replace(' ', '_') for c in lit_raw.columns]
lit_c=lit_raw[(lit_raw.Indicator == "Adult literacy rate, population 15+ years, both sexes (%)")]
lit_piv=pd.pivot_table(lit_c,index='LOCATION',columns='TIME',values='Value')

# cont_raw=cmap.cont_cou_map()
cont_raw=cmap.cont_cou_map("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/")
#plot
year=2006
lit=lit_piv[year].dropna()
ed=ed_piv[str(year)].dropna()
inx=ed.index & lit.index & cont_raw.index
lit=lit.loc[inx]
ed=ed.loc[inx]
cont=cont_raw.loc[inx]
color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
   'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
cont["Color"] = cont["Continent_Name"].apply(lambda x: color_map.get(x))
color=cont['Color']
pf.scatter_plot(ed,lit,color,"Adult Literacy Rate of "+str(year)+ " Versus Education Expenditure of "+str(year),"Percentage of GDP","Percentage",color_map)
