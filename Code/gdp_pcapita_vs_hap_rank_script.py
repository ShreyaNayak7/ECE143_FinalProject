import numpy as np
from class_utilities import Utilities as ut
from class_plot_functions import ScatterPlot as sc
from class_gather_data import DataHandler as dh
#%matplotlib notebook

#download from https://www.kaggle.com/unsdsn/world-happiness#2017.csv
#download from https://data.worldbank.org/indicator/ny.gdp.pcap.cd
file_1="D:\ECE 143\Data files for Project\Happiness Report 2017.csv"
file_2="D:\ECE 143\Data files for Project\GDPpercapita.xls"

hap_raw=dh.gather_data_from_csv(file_1,index='Country')
gdp_cp_raw=dh.gather_data_from_Excel(file_2,sh_name='Data',index='Country Name')

hap=hap_raw['Happiness.Rank'].dropna()
hap=hap.drop('South Sudan')

gdp_cp=gdp_cp_raw[['Country Code','2017']].copy()
gdp_cp.replace("nan", np.nan, inplace = True)
gdp_cp.dropna(inplace=True)

hap1,gdp_cp1=ut.trim(hap,gdp_cp)
hap_df=hap1.to_frame()
merged = gdp_cp1.merge(hap_df, left_index=True, right_index=True, how='inner')
merged.set_index('Country Code',inplace=True)
merged.drop(['XKX','NER','AFG','LSO','KEN','GIN','GHA','KEN','MMR','PRY','ZMB','BLR','SEN','ARM','LBR','TJK','CAF','BDI','TZA','RWA','TGO', 'ZWE','MLI','BEN','BFA','TCD',
    'BTN','MDG','AUS'],inplace=True)

cont_raw=dh.cont_cou_map("D:\ECE 143\Data files for Project\country-and-continent-codes-list.csv")
merged,cont=ut.trim(merged,cont_raw)

sc_plot=sc(merged['2017'],merged['Happiness.Rank'],cont,'Happiness Rank Versus GDP Per Capita','GDP per capita (current US$)',"Happiness Rank (No units)")
sc_plot.show()
