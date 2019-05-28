
'''
script for piechart-speed dataset
'''
import plotly as py
py.tools.set_credentials_file(username='shre', api_key='AQsz9RywWpoxsfsQV1xb')
import pandas as pd
from gather_data import gather_data_from_Excel
ag=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpag_ppp",index='country',fillnan=0)
ed=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpeducation_ppp",index='country',fillnan=0)
hl=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdphealth_ppp",index='country',fillnan=0)
df=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpdefense_ppp",index='country',fillnan=0)
com=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpcom_ppp",index='country',fillnan=0)
tran=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdptransp_ppp",index='country',fillnan=0)
tc=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdptc_ppp",index='country',fillnan=0)
sp=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpsp_ppp",index='country',fillnan=0)
mine=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpmining_ppp",index='country',fillnan=0)
fuel=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpfuel_ppp",index='country',fillnan=0)
oth=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdpother_ppp",index='country',fillnan=0)
tot_of_gdp=gather_data_from_Excel("001_Main SPEED Dataset 2015.xls","gdptotal_ppp",index='country',fillnan=0)
year=2011
#sum_df=pd.DataFrame(index=df.index)
#sum_df['sum']=ag[year]+ed[year]+hl[year]+df[year]+com[year]+tran[year]+tc[year]+sp[year]+mine[year]+fuel[year]+oth[year]

def pie_chart():
    '''
    used to make pie chart using plotly
    '''
    country='India'
    year=2011
    
    data = [dict(type='pie',
    values=[ ag.loc[country,year],ed.loc[country,year],hl.loc[country,year],
            df.loc[country,year],com.loc[country,year],tran.loc[country,year],
            tc.loc[country,year],sp.loc[country,year],mine.loc[country,year],
            fuel.loc[country,year],oth.loc[country,year]],
    labels=["Agriculture","Education","Health","Defense","Communication",
            "Transport", "Transport and Communication","Social Expenditure",
            "Mining", "Fuel", "Other"],
    #textinfo='label+value',
    hole=0.4)]
    
    layout = dict(
        title = dict(text = 'Expenditure by Sector, Year 2011'),
        annotations = [dict(
            x = 0.55,
            y = 0.1,
            xref = 'paper',
            yref = 'paper',
            text = 'Source: <a href="https://data.worldbank.org/indicator/ny.gdp.pcap.cd">\
                The World Bank</a>',
            showarrow = False)])
    fig = dict(data = data, layout = layout)
    py.plotly.iplot(fig, filename = 'piechart')

pie_chart()