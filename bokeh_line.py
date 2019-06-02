# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:01:41 2019

@author: shrey
"""
import pandas as pd
import gather_data as gd
from bokeh.plotting import figure,show,output_file,ColumnDataSource
from bokeh.models import HoverTool

df = gd.gather_data_from_Excel('Govt exp imf 2.xls', sh_name='exp')
df.rename(columns={'Government expenditure, percent of GDP (% of GDP)':'Country_name'},
                   inplace=True)
df.drop([0],inplace=True)
df1=df.T
new_header = df1.iloc[0]
df1 = df1[1:]
df1.columns = new_header
df1.index.names=['Year']
df1.columns.names=['Countries']

year1=1880
year2=2011
country='India'
y1=df1.index.get_loc(year1)
y2=df1.index.get_loc(year2)
col=df1.columns.get_loc(country)

hover = HoverTool(
                  tooltips=[('Year',"$x{0f}"),
                            ('Value',"$y%")],
                  mode='vline'
                  )
p = figure(x_axis_label='year', y_axis_label='Government Expenditure (% of GDP)')
p.line(y=df1.iloc[y1:y2,col],x=df1.index[y1:y2])
p.circle(y=df1.iloc[y1:y2,col],x=df1.index[y1:y2], size=4,hover_fill_color='firebrick',
         hover_line_color='white')
p.add_tools(hover)
#
output_file('auto-df3.html')
show(p)