# -*- coding: utf-8 -*-
"""
Created on Sat May 18 09:20:23 2019

@author: shrey
"""
import plotly as py
py.tools.set_credentials_file(username='shre', api_key='AQsz9RywWpoxsfsQV1xb')
import pandas as pd
import plotly.graph_objs as go
def choropleth_map(df):
    '''
    With data given in df, plot a choropleth heat map on the world map
    '''
    data = [go.Choropleth(
    locations = df['Country Code'],
    z = df['2017'],
    text = df['Country Name'],
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
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(180,180,180)',
            width = 0.5
        )),
    colorbar = go.choropleth.ColorBar(
        tickprefix = '$',
        title = 'GDP<br>per Capita US$'),)]

    layout = go.Layout(
        title = go.layout.Title(
            text = '2017 Standard of Living'
        ),
        geo = go.layout.Geo(
            showframe = False,
            showcoastlines = False,
            projection = go.layout.geo.Projection(
                type = 'equirectangular'
            )
        ),
        annotations = [go.layout.Annotation(
            x = 0.55,
            y = 0.1,
            xref = 'paper',
            yref = 'paper',
            text = 'Source: <a href="https://data.worldbank.org/indicator/ny.gdp.pcap.cd">\
                The World Bank</a>',
            showarrow = False
        )]
    )
    
    fig = go.Figure(data = data, layout = layout)
    py.plotly.iplot(fig, filename = 'd3-world-map')
        