import matplotlib 
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
import folium
from bokeh.plotting import Figure,show,output_file
from bokeh.models import Select,CustomJS,ColumnDataSource,HoverTool
from bokeh.layouts import row,widgetbox

class ScatterPlot:
    
    color_map={'Asia':'blue','Europe':'crimson','North America':'darkgreen',
               'South America':'yellow','Oceania':'blueviolet','Africa':'lawngreen'}
        
    def __init__(self,x,y,cont_df,title="Scatter Plot",xlabel="x",ylabel="y"):
        '''
        Initializes an instance with the data to plot and the color of the bubbles representing the data in the scatter plot
        Inputs: x
                (pd.Series)
                Gives the x-axis values for the plot
                y
                (pd.Series)
                Gives the y-axis values for the plot
                color
                (pd.Series)
                Gives the colors for the datapoints
        '''
        assert isinstance(x,pd.Series)
        assert isinstance(y,pd.Series)
        assert isinstance(cont_df, pd.DataFrame)
        assert (isinstance(title,str))
        assert (isinstance(xlabel,str))
        assert (isinstance(ylabel,str))
        self.x=x
        self.y=y
        self.cont_df=cont_df
        self.title=title
        self.xlabel=xlabel
        self.ylabel=ylabel
        
    def make_legend(self):
        '''
        makes a legend for the scatter plot, using the predefined mapping of color with continent
        '''
        patches=[]
        
        for counter_1 in range(len(self.color_map)):
            patches.append(mpatches.Patch(color=list(self.color_map.values())[counter_1],
                                      label=list(self.color_map.keys())[counter_1]))
        return patches
    
    def give_color(self,cont_df):
        '''
        assigns a color to each continet based on the color_map defined as class variable
        '''
        assert isinstance(cont_df,pd.DataFrame)
        cont_df["Color"] = cont_df["Continent_Name"].apply(lambda x: self.color_map.get(x))
        return cont_df["Color"]
    
    def show(self):
        '''
        Gives scatter plot
        '''
        plt.figure()
        color=self.give_color(self.cont_df)
        plt.scatter(self.x, self.y,c=color,alpha=0.8)
        for i, txt in enumerate(self.x.index):
            plt.annotate(txt, (self.x[i], self.y[i]))
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.grid(True,which='both',color='0.9')
        patches=self.make_legend()
        plt.legend(handles=list(patches),loc='best')
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.show()
        


class Choropleth:
    def __init__(self,geo_data,data,columns,key_on,legend_name,location=[0,0],zoom_start=0,fill_color="YlGn"):
        '''
        Gives choropleth graph
        Inputs: geo_data
                (json file)
                Contains geographical coordinates 
                
                data
                (pd.Dataframe)
                Contains data for the map
                
                columns
                (list)
                contains names of columns that contain data to be plotted
                
                key_on
                (str)
                Gives position of Country index in json file
                
                legend_name
                (str)
                Gives name to the legend
                
                location
                (list with two elements)
                gives the x,y coordinates at which map needs to be centred
                
                zoom_start
                (int)
                gives the initial zoom value for the graph
                
                fill_color
                (str)
                Gives colormap for the plot
        '''
        assert isinstance(data,pd.DataFrame)
        assert isinstance(columns,list)
        assert isinstance(key_on,str)
        assert isinstance(legend_name,str)
        assert isinstance(location,list)
        assert isinstance(zoom_start,float)
        assert isinstance(fill_color,str)                
        self.geo_data=geo_data
        self.location=location
        self.zoom_start=zoom_start
        self.data=data
        self.columns=columns
        self.key_on=key_on
        self.legend_name=legend_name
        self.fill_color=fill_color
        
    def add_marker(self,m,loc_label):
        '''
        Adds markers to choropleth map
        Inputs: loc_label
                (list of tuples)
                Each tuple corresponds to a marker. 
                First item in each tuple is a list of 2 items- latitude and longitude 
                of the marker. Second item is the label for the marke.r
                
                m
                (folium.Map object)
                The map on which markers need to be placed.
        '''
        assert isinstance(m,folium.Map)
        assert isinstance(loc_label,list)
        assert all(isinstance(item,tuple) for item in loc_label)
        folium.LayerControl().add_to(m)
        for marker in loc_label:
            folium.map.Marker(location=marker[0],tooltip=marker[1]).add_to(m)
        return m
    
    def make_map(self):
        '''
        Makes and returns folium map object
        '''
        m = folium.Map(location=[30,15],zoom_start=2.4)
        m.choropleth(
        geo_data=self.geo_data,
        name='choropleth',
        data=self.data,
        columns=self.columns,
        key_on=self.key_on,
        fill_color=self.fill_color,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=self.legend_name
        )
        return m
    
    def save(self,m,file_name):
        '''
        saves the map with given file name
        '''
        assert isinstance(file_name,str)
        m.save(file_name)
        
        
class BokehLine:
    
    def __init__(self,df,country,title="bokeh line",xlabel="x",ylabel="y"):
        '''
        makes an object of type BokehLine
        Inputs: df
                (pd.DataFrame)
                Dataframe containing data for all traces
                
                country
                (str)
                The country to plot in the initial trace
                
                title
                (str)
                Title of the plot
                
                xlabel
                (string)
                Label for x-axis
                
                ylabel
                (string)
                Label for y-axis
        '''
        assert isinstance(df,pd.DataFrame)
        assert isinstance(xlabel,str)
        assert isinstance(ylabel,str)
        assert isinstance(title,str)
        assert isinstance(country,str)        
        
        self.df=df
        self.country=country
        self.title=title
        self.xlabel=xlabel
        self.ylabel=ylabel
        self.source_visible=ColumnDataSource(data={'x' : self.df.index.tolist(),
                                      'y' : self.df.loc[:,self.country].tolist()
                                      })
                
    def make_line(self):
        '''
        makes a bokeh line chart with markers
        '''
        p = Figure(x_axis_label=self.xlabel, y_axis_label=self.ylabel,title=self.title)
        p.line(y='y',x='x',source=self.source_visible)
        p.circle(y='y',x='x',source=self.source_visible,size=4,hover_fill_color='firebrick',
                 hover_line_color='white')
        return p
    
    def add_hover(self,p,tooltips):
        '''
        Adds hover tool to the chart
        Inputs: p
                (bokeh.plotting.Figure())
                The bokeh figure object to which hover needs to be added
                
                tooltips
                (list of tuples) 
                Each tuple gives (label,value) to be displayed in the hoverlabel
        '''
        assert isinstance(p,Figure)
        assert isinstance(tooltips,list)
        hover = HoverTool(
                  tooltips=tooltips,
                  mode='vline'
                  )
        p.add_tools(hover)
        return p
    
    def add_dropdown(self,df):
        '''
        Adds a dropdown to bokeh line chart
        Inputs: df
                (pd.DataFrame)
                DataFrame that contains data for all the traces of the graph
        '''
        assert isinstance(df,pd.DataFrame)
        data=df.to_dict(orient='list')
        data['x']=df.index.tolist()
        source_available = ColumnDataSource(data=data)
        select = Select(title="Country", options=self.df.columns.tolist(), value=self.country)
        select.callback = CustomJS(args=dict(source_visible=self.source_visible,
                                         source_available=source_available), code="""
        var data_visible = source_visible.data;
        var data_available = source_available.data;
        var f = cb_obj.value;
        data_visible.y = data_available[f];
        source_visible.change.emit();
            """)
        
        return select
    
    def show(self,file_name,p,select=None):
        '''
        Shows the bokeh plot
        Inputs: file_name
                (str)
                Name/path of the file where the plot is to be stored
                
                p
                (bokeh.plotting.Figure())
                The bokeh figure object to which hover needs to be added
                
                select
                (Bokeh.models.Select object)
                Object that allows to select between traces
        '''
        assert isinstance(file_name,str)
        assert isinstance(p,Figure)
        assert (isinstance(select,Select) or isinstance(select,None))
        output_file(file_name)
        if select is None:
            show(p)
        else:
            show(row(p,widgetbox(select)))



class MultiBar:
    
    
    def __init__(self,df,title="Bar",xlabel="x"):
        '''
        Initializes instance of MultiBar; used for plotting 
        Inputs: df
                (pd.DataFrame)
                Contains data for the plot. Each column gives x values
                Index gives y values
                
                title
                (str)
                Gives title of the plot
                
                xlabel
                (str)
                Gives label for x-axis
                
        '''
        assert isinstance(df,pd.DataFrame)
        assert isinstance(title,str)
        assert isinstance(xlabel,str)
        self.df=df
        self.title=title
        self.xlabel=xlabel
        
        
    def show(self):
        '''
        plot multi-bar graph for each row in dataframe
        '''

        cmap1 = matplotlib.cm.get_cmap('PuRd')
        ax=self.df.plot.barh(color=[cmap1(0.3),cmap1(0.6),cmap1(0.9)],alpha=1,zorder=3,figsize=(10,6))
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.xaxis.grid(True,linestyle='--',color='lightgray',zorder=0)
        plt.suptitle(self.title, fontsize=14)
        plt.xlabel(self.xlabel, fontsize=11)
        plt.show()
            

               
                
                
                
                
               
