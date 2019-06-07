# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 19:45:20 2019

@author: shrey
"""

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure

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
        #assert (isinstance(title,None) or isinstance(title,str))
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
        
        
        
        
        
        
       