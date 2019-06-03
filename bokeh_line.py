# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:01:41 2019

@author: shrey
"""
import gather_data as gd
from bokeh.plotting import Figure,show,output_file
from bokeh.models import Select,CustomJS,ColumnDataSource,HoverTool
from bokeh.layouts import row,widgetbox

output_file('line.html')

#format and clean data
df = gd.gather_data_from_Excel('Govt exp imf 2.xls', sh_name='exp')
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

#prepare dictionary with data, one entry for each country
data=df1.to_dict(orient='list')
data['x']=df1.index.tolist()

source_available = ColumnDataSource(data=data)
source_visible=ColumnDataSource(data={'x' : df1.index.tolist(),
                                      'y' : df1.loc[:,country].tolist()
                                      })
p = Figure(x_axis_label='year', y_axis_label='Government Expenditure (% of GDP)')
p.line(y='y',x='x',source=source_visible)
p.circle(y='y',x='x',source=source_visible,size=4,hover_fill_color='firebrick',
         hover_line_color='white')

#hovertool parameters
hover = HoverTool(
                  tooltips=[
                            ('Year',"$x{0f}"),
                            ('Value',"$y%")],
                  mode='vline'
                  )
p.add_tools(hover)

#select widget callback
select = Select(title="Country", options=df1.columns.tolist(), value=country)
        
select.callback = CustomJS(args=dict(source_visible=source_visible,
                                     source_available=source_available), code="""
    var data_visible = source_visible.data;
    var data_available = source_available.data;
    var f = cb_obj.value;
    data_visible.y = data_available[f];
    source_visible.change.emit();
        """)

show(row(p,widgetbox(select)))
