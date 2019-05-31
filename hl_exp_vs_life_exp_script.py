# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:03:35 2019

@author: shrey
Editor: Akhil Jain
"""
import pandas as pd
import gather_data as gd
import plot_functions as pf
#beginning_of_file=""
beginning_of_path="../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/"
#file_1="SHA_30052019014114312.csv"
file_2="HEALTH_STAT_30052019043359352.csv"
#
#load file on health expenditure
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
hl_raw=gd.gather_data_from_csv(str(beginning_of_path+file_1))
#clean file: replace space in col names with _, filter, delete unnecessary cols
hl_raw.columns = [c.replace(' ', '_') for c in hl_raw.columns]
hl_c=hl_raw[(hl_raw.Financing_scheme == "All financing schemes") & 
       (hl_raw.Function == "Current expenditure on health (all functions)") &
       (hl_raw.Provider == "All providers") &
       (hl_raw.Measure == "Share of gross domestic product")]
#format into "country in rows and cols in years" format
hl_piv=pd.pivot_table(hl_c,index='Country',columns='Year',values='Value')

#load file on life_expectancy 
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
lf_raw=gd.gather_data_from_csv(str(beginning_of_path+file_2))
lf_raw.columns = [c.replace(' ', '_') for c in lf_raw.columns]
lf_c=lf_raw[(lf_raw.Variable=="Total population at birth")]
#format into "country in rows and cols in years" format
lf_piv=pd.pivot_table(lf_c,index='Country',columns='Year',values='Value')

#plot
while(True):
    input_year=pf.get_year()
    if(input_year=='done'):
        exit()
    try:
        inx=lf_piv.index & hl_piv.index
        lf=lf_piv.loc[inx]
        hl=hl_piv.loc[inx]
        pf.scatter_plot(hl[year],lf[year],"health expenditure vs life expectancy")
    except:
        assert False
