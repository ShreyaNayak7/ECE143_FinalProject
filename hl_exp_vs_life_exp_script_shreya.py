import pandas as pd
from utilities import Utilities as ut
from plot_func import ScatterPlot as sc
from gather_data import DataHandler as dh
#%matplotlib notebook

#load file on health expenditure
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
file_1="D:\ECE 143\Data files for Project\SHA_30052019014114312.csv"

hl_raw=dh.gather_data_from_csv(file_1)
hl_raw=ut.remove_spaces(hl_raw)
hl_c=hl_raw[(hl_raw.Financing_scheme == "All financing schemes") &      # filter rows based on desired column values
       (hl_raw.Function == "Current expenditure on health (all functions)") &
       (hl_raw.Provider == "All providers") &
       (hl_raw.Measure == "Share of gross domestic product")]
hl_piv=ut.pivot(hl_c,index_new='LOCATION',columns_new='Year',values_new='Value')

#load file on life_expectancy 
#https://stats.oecd.org/Index.aspx?DataSetCode=SHA
file_2="D:\ECE 143\Data files for Project\HEALTH_STAT_30052019043359352.csv"

lf_raw=dh.gather_data_from_csv(file_2)
lf_raw=ut.remove_spaces(lf_raw)
lf_c=lf_raw[(lf_raw.Variable=="Total population at birth")]
lf_piv=pd.pivot_table(lf_c,index='COU',columns='Year',values='Value')

#load data that maps country to continent
cont_raw=dh.cont_cou_map("D:\ECE 143\Data files for Project\country-and-continent-codes-list.csv")

#plot
year=2015
lf,hl,cont=ut.trim(lf_piv,hl_piv,cont_raw)
sc_plot=sc(hl[year],lf[year],cont,title="Life Expectancy Versus Health Expenditure",xlabel="Percentage of Gross Domestic Product",ylabel="Years")
sc_plot.show()


