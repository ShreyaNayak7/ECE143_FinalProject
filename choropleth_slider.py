# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:50:57 2019

@author: shrey
"""

import plotly as py
py.tools.set_credentials_file(username='shre', api_key='AQsz9RywWpoxsfsQV1xb')
import pandas as pd
import plotly.graph_objs as go
def choropleth_map_slider(df):
    '''
    With data given in df, plot a choropleth heat map on the world map
    '''
#    df=df.fillna(0)
    start_index=57
   
    data = [dict(type='choropleth',
    locations = df['Country Code'],
    z = df[col],
    text = df['Country Name'],
    visible=False,
#    colorscale = [
#        [0, "rgb(5, 10, 172)"],
#        [0.35, "rgb(40, 60, 190)"],
#        [0.5, "rgb(70, 100, 245)"],
#        [0.6, "rgb(90, 120, 245)"],
#        [0.7, "rgb(106, 137, 247)"],
#        [1, "rgb(220, 220, 220)"]
#    ],
    colorscale='Greens',
    autocolorscale = False,
    reversescale = True,
    marker = dict(
        line = go.choropleth.marker.Line(
            color = 'rgb(180,180,180)',
            width = 0.5
        )),
    colorbar = dict(
        tickprefix = '$',
        title = 'GDP<br>per Capita US$'),) for col in df.columns[4::]]
    data[start_index]['visible']=True
    
    steps = []
    for i in range(len(data)):
        step = dict(
            method = 'restyle',  
#            args = ['visible', [False] * len(data)],
            args = [
                # Make the ith trace visible
                {'visible': [t == i for t in range(len(data))]},
                
                # Set the title for the ith trace
                {'title.text': 'Standard of Living: %s' % df.columns[i+4]}],
            label = str(df.columns[4+i]),
        )
       # step['args'][1][i] = True # Toggle i'th trace to "visible"
        steps.append(step)
    
    sliders = [dict(
        active = start_index,
        currentvalue = {"prefix": "Year: "},
        pad = {"t": 25},
        steps = steps,
    )]

    layout = dict(
        title = dict(text = 'Standard of Living: %s'% df.columns[start_index]),
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = go.layout.geo.Projection(
                type = 'equirectangular'
            )
        ),
        annotations = [dict(
            x = 0.55,
            y = 0.1,
            xref = 'paper',
            yref = 'paper',
            text = 'Source: <a href="https://data.worldbank.org/indicator/ny.gdp.pcap.cd">\
                The World Bank</a>',
            showarrow = False)],
          sliders=sliders
    )
    
    
    fig = dict(data = data, layout = layout)
    py.plotly.iplot(fig, filename = 'd3-world-map-slider')
        