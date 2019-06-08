from gather_data import DataHandler as dh
from plot_functions import BokehLine as bl

#load_data
file_1="D:\ECE 143\Data files for Project\Govt exp imf 2.xls"
df = dh.gather_data_from_Excel(file_1, sh_name='exp')
df.rename(columns={'Government expenditure, percent of GDP (% of GDP)':'Country_name'},
                   inplace=True)
df.drop([0],inplace=True)
df=df.T
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
df.index.names=['Year']
df.columns.names=['Countries']
df.drop(list(range(1800,1880)),inplace=True)
df.drop(df.iloc[:, -2::], inplace = True, axis = 1)
df1=df[['Argentina','Australia','Germany','India','Italy','Japan','United States',
        'United Kingdom']].copy()
#pick initial country
country='United States'
col=df1.columns.get_loc(country)
file_name="line.html"
bok_line=bl(df1,
             country,
             title='Government Expenditure',
             xlabel='Year',
             ylabel='Government Expenditure (% of GDP)')
fig=bok_line.make_line()
fig=bok_line.add_hover(fig,tooltips=[
                            ('Year',"$x{0f}"),
                            ('Value',"$y%")])
drop_down=bok_line.add_dropdown(df)
bok_line.show(file_name,fig,drop_down)
