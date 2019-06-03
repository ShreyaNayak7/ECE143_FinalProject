'''
Team 7
Making Plots by Using the "matplotlib.pyplot" Module
'''


import matplotlib.pyplot as plt
import pandas as pd
# import matplotlib

def scatter_plot(x,y,color,title, units_for_x="", units_for_y="",legend):
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
    plt.scatter(x, y,c=color,alpha=0.8)
    list_of_labels=title.split(" Versus ")
    provide_labels(list_of_labels[1]+", "+units_for_x, list_of_labels[0]+", "+units_for_y, title)
    for i, txt in enumerate(x.index):
        plt.annotate(txt, (x[i], y[i]))
    plt.box(False)
    plt.grid(True,which='both',color='0.9')
    plt.show()
    plt.legend(legend.keys(),legend.values())
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

