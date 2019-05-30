# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:03:35 2019

@author: shrey
"""
import pandas as pd
import gather_data as gd

#load file on health expenditure
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
hl_raw=gd.gather_data_from_csv("SHA_30052019014114312.csv")
#clean file: replace space in col names with _, filter, delete unnecessary cols
hl_raw.columns = [c.replace(' ', '_') for c in hl_raw.columns]
hl=hl_raw[(hl_raw.Financing_scheme == "All financing schemes") & 
       (hl_raw.Function == "Current expenditure on health (all functions)") &
       (hl_raw.Provider == "All providers") &
       (hl_raw.Measure == "Share of gross domestic product")]
del hl['HF']
del hl['HC']
del hl['HP']
del hl['MEASURE']
del hl['TIME']
del hl['Unit_Code']
del hl['PowerCode_Code']
del hl['Reference_Period']
del hl['Reference_Period_Code']
del hl['Flag_Codes']
del hl['Flags']
#format into "country in rows and cols in years" format
hl_piv=pd.pivot_table(hl,index='Country',columns='Year',values='Value')

#load file on life_expectancy 
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
lf_raw=gd.gather_data_from_csv("HEALTH_STAT_30052019043359352.csv")
lf_raw.columns = [c.replace(' ', '_') for c in lf_raw.columns]
lf=lf_raw[(lf_raw.Variable=="Total population at birth")]
del lf['VAR']
del lf['UNIT']
del lf['YEA']
del lf['Flag_Codes']
del lf['Flags']
#format into "country in rows and cols in years" format
lf_piv=pd.pivot_table(lf,index='Country',columns='Year',values='Value')
