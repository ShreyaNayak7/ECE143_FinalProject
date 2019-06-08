import pandas as pd
from utilities import Utilities as ut
from plot_func import ScatterPlot as sc
from gather_data import DataHandler as dh

file_1="D:\ECE 143\Data files for Project\Education Expenditure.xls"
file_2="D:\ECE 143\Data files for Project\EDULIT_DS_31052019025144633.csv"
ed_raw=dh.gather_data_from_Excel(file_1,sh_name='Data',
                                 header=3,index='Country Code')
ed_piv=ed_raw

lit_raw=dh.gather_data_from_csv(file_2)
lit_raw = ut.remove_spaces(lit_raw)

cont_raw=dh.cont_cou_map("D:\ECE 143\Data files for Project\country-and-continent-codes-list.csv")

#Youth literacy rate
lit_c=lit_raw[(lit_raw.Indicator == "Youth literacy rate, population 15-24 years, both sexes (%)")]
lit_piv=ut.pivot(lit_c,index_new='LOCATION',columns_new='TIME',values_new='Value')

#plot
year=2014
lit=lit_piv[year].dropna()
ed=ed_piv[str(year)].dropna()
ed,lit,cont=ut.trim(ed,lit,cont_raw)

sc_plot=sc(ed,lit,cont,"Youth Literacy Rate Versus Education Expenditure","Education Expenditure (Percentage of GDP)", "Literacy Rate (Percentage)")
sc_plot.show()

#Adult literacy rate
lit_c=lit_raw[(lit_raw.Indicator == "Adult literacy rate, population 15+ years, both sexes (%)")]
lit_piv=ut.pivot(lit_c,index_new='LOCATION',columns_new='TIME',values_new='Value')

#plot
lit=lit_piv[year].dropna()
ed=ed_piv[str(year)].dropna()
ed,lit,cont=ut.trim(ed,lit,cont_raw)

sc_plot=sc(ed,lit,cont,"Adult Literacy Rate Versus Education Expenditure","Education Expenditure (Percentage of GDP)", "Literacy Rate (Percentage)")
sc_plot.show()