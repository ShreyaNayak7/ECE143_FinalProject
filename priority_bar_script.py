# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:23:37 2019

@author: shrey
"""
import pandas as pd
import gather_data as gd
import priority_bar as pb

hl_raw=gd.gather_data_from_csv("UNdata_Export_Health.csv",
                                index='Country or Area')
hl_piv=pd.pivot_table(hl_raw,index='Country or Area',columns='Year(s)',values='Value')
hl_col=hl_piv[2010].copy()
hl_col.dropna(inplace=True)
hl_col.sort_values(ascending=True,inplace=True)

ed_raw=gd.gather_data_from_csv("Education expenditure UNESCO.csv",
                                index='Country')
ed_c=ed_raw[(ed_raw.Indicator == "Expenditure on education as a percentage of total government expenditure (%)")]
ed_piv=pd.pivot_table(ed_c,index='Country',columns='Time',values='Value')

ed_col=ed_piv[2013].copy()
ed_col.dropna(inplace=True)
ed_col.sort_values(ascending=True,inplace=True)


#soc_raw=gd.gather_data_from_csv("Social Expenditure.csv")
##clean file: replace space in col names with _, filter, delete unnecessary cols
#soc_raw.columns = [c.replace(' ', '_') for c in soc_raw.columns]
#soc_c=soc_raw[(soc_raw.Source == "Public") &
#              (soc_raw.Branch == "Total") &
#              (soc_raw.Type_of_Expenditure == "Total") &
#              (soc_raw.Measure == "In percentage of Total General Government Expenditure")]
#soc_piv=pd.pivot_table(soc_c,index='Country',columns='Year',values='Value')
soc_piv=gd.gather_data_from_Excel("001_Main SPEED Dataset 2015.xls",
                                 sh_name='totsp_ppp',index='country')
soc_col=soc_piv[2010].copy()
soc_col.dropna(inplace=True)
soc_col.sort_values(ascending=True,inplace=True)

inx= soc_col.index & hl_col.index & ed_col.index
soc_col_df=soc_col.to_frame()
hl_col_df=hl_col.to_frame()
ed_col_df=ed_col.to_frame()
soc_col_df.rename(columns = {2010: "Social Expenditure"},inplace=True)
hl_col_df.rename(columns = {2010: "Health Expenditure"},inplace=True)
ed_col_df.rename(columns = {2013: "Eucation Expenditure"},inplace=True)
merged2 = ed_col_df.merge(hl_col_df, left_index=True, right_index=True,
                       how='inner') 
merged3=merged2.merge(soc_col_df, left_index=True, right_index=True,
                       how='inner')
merged3.sort_values(ascending=True,inplace=True,by=['Social Expenditure','Health Expenditure'])

choice=['United States of America','Brazil','Germany','Italy','Israel',
        'Thailand','Malaysia','Nepal','Jamaica']
merged3_subset=merged3.loc[choice]
merged3_subset.rename(index={'United States of America':'United States'},inplace=True)
merged3_subset.sort_values(ascending=True,inplace=True,by=['Social Expenditure','Health Expenditure'])
pb.mix_plot(merged3_subset)