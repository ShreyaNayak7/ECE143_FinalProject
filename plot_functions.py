'''
Team 7
Making Plots by Using the "matplotlib.pyplot" Module
'''


import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches
from matplotlib.pyplot import figure

# import matplotlib

def scatter_plot(x,y,color,title, units_for_x="", units_for_y="",legend={}):
    '''
    
    :param x: data along x axis
    :param y: data along y axis
    :type x: <class 'pandas.Series'>
    :type y: <class 'pandas.Series'>
    :type s: <class 'pandas.Series'>
    '''
    assert isinstance(x,pd.Series)
    assert isinstance(y,pd.Series)
    assert isinstance(color, pd.Series)
    assert isinstance(title, str)
    assert isinstance(legend,dict)
    fig1 = plt.figure(figsize=(8,6))
    ax = plt.subplot(111)
    plt.scatter(x, y,c=color,alpha=0.8,zorder=3)
    list_of_labels=title.split(" Versus ")
    provide_labels(list_of_labels[1]+", "+units_for_x, list_of_labels[0]+", "+units_for_y, title)
    for i, txt in enumerate(x.index):
        plt.annotate(txt, (x[i], y[i]))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.grid(True,which='both',color='0.9',zorder=0)
    patches=[]
    for counter_1 in range(len(legend)):
        patches.append(mpatches.Patch(color=list(legend.values())[counter_1],label=list(legend.keys())[counter_1]))
    
  
    
    #ax.legend(handles=list(patches),bbox_to_anchor=(1.1, 1.02))
    ax.legend(handles=list(patches),loc='bottom right')
    fig1.show()
def provide_labels(label_for_x_axis,label_for_y_axis,title):
    '''
    
    :param x: data along x axis
    :param y: data along y axis
    :type x: pandas.Series
    :type y: pandas.Series
    '''
    assert isinstance(label_for_x_axis, str)
    assert isinstance(label_for_y_axis,str)
    assert isinstance(title, str)
    plt.xlabel(label_for_x_axis)
    plt.ylabel(label_for_y_axis)
    plt.title(title)

