from class_gather_data import DataHandler as dh
from class_utilities import Utilities as ut 
from class_plot_functions import MultiBar as mb

#load health expenditure data
hl_raw=dh.gather_data_from_csv(r"D:\ECE 143\Data files for Project\UN data health exp.csv",index='Country or Area')
hl_piv=ut.pivot(hl_raw,index_new='Country or Area',columns_new='Year(s)',values_new='Value')
year_hl=2010
hl_col_df=ut.pipeline(hl_piv,year_hl,"Health Expenditure")


#load education expenditure data
ed_raw=dh.gather_data_from_csv("D:\ECE 143\Data files for Project\Education expenditure UNESCO.csv",
                                index='Country')
ed_c=ed_raw[(ed_raw.Indicator == "Expenditure on education as a percentage of total government expenditure (%)")]
ed_piv=ut.pivot(ed_c,index_new='Country',columns_new='Time',values_new='Value')
year_ed=2013
ed_col_df=ut.pipeline(ed_piv,year_ed,"Education Expenditure")

#load social expenditure data
soc_piv=dh.gather_data_from_Excel("D:/ECE 143/A_Repository_for_the_Final_Project_for_ECE_143/001_Main SPEED Dataset 2015.xls",
                                 sh_name='totsp_ppp',index='country')
year_soc=2010
soc_col_df=ut.pipeline(soc_piv,year_soc,"Social Expenditure")

#merge to one dataframe
merged2 = ed_col_df.merge(hl_col_df, left_index=True, right_index=True,
                       how='inner') 
merged3=merged2.merge(soc_col_df, left_index=True, right_index=True,
                       how='inner')
merged3.sort_values(ascending=True,inplace=True,by=['Social Expenditure','Health Expenditure'])

#pick countries to plot
choice=['United States of America','Brazil','Germany','Italy','Israel',
        'Thailand','Malaysia','Nepal','Jamaica']
merged3_subset=merged3.loc[choice]
merged3_subset.rename(index={'United States of America':'United States'},inplace=True)
merged3_subset.sort_values(ascending=True,inplace=True,by=['Social Expenditure','Health Expenditure'])
fig=mb(merged3_subset,"Expenditure by sector","% of Government Expenditure")
fig.show()
