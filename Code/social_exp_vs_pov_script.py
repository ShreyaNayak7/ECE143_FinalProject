import pandas as pd
from class_utilities import Utilities as ut
from class_plot_functions import ScatterPlot as sc
from class_gather_data import DataHandler as dh
#%matplotlib notebook

#load file on poverty
#https://data.oecd.org/inequality/poverty-rate.html
file_1="D:\ECE 143\Data files for Project\Poverty.csv"

pv_raw=dh.gather_data_from_csv(file_1)
pv_raw=ut.remove_spaces(pv_raw)
pv_c=pv_raw[(pv_raw.SUBJECT == "TOT")]
pv_piv=ut.pivot(pv_c,index_new='LOCATION',columns_new='TIME',values_new='Value')

#load file on social expenditure
#https://data.oecd.org/inequality/poverty-rate.html
file_2="D:\ECE 143\Data files for Project\Social Expenditure.csv"
soc_raw=dh.gather_data_from_csv(file_2)
soc_raw=ut.remove_spaces(soc_raw)
soc_c=soc_raw[(soc_raw.Source == "Public") &
              (soc_raw.Branch == "Total") &
              (soc_raw.Type_of_Expenditure == "Total") &
              (soc_raw.Measure == "In percentage of Gross Domestic Product")]
soc_piv=ut.pivot(soc_c,index_new='COUNTRY',columns_new='Year',values_new='Value')

cont_raw=dh.cont_cou_map("D:\ECE 143\Data files for Project\country-and-continent-codes-list.csv")

#plot
year=2015
pv=pv_piv[year].dropna()
soc=soc_piv[year].dropna()
inx=soc.index & pv.index
pv=pv.loc[inx]
soc=soc.loc[inx]
soc,pv,cont=ut.trim(soc,pv,cont_raw)
sc_plot=sc(soc,pv,cont,"Poverty Rate Versus Social Expenditure", "Social Expenditure (Percentage of GDP)", "Pverty Rate (ratio)")
sc_plot.show()
