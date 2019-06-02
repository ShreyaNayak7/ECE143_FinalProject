'''
Team 7
Making Plots by Using the "matplotlib.pyplot" Module
'''


import matplotlib.pyplot as plt

def scatter_plot(x,y,color,title):
    '''
    
    :param x: data along x axis
    :param y: data along y axis
    :type x: <class 'pandas.Series'>
    :type y: <class 'pandas.Series'>
    :type s: <class 'pandas.Series'>
    '''

    plt.scatter(x, y,c=color,alpha=0.8)
    provide_labels(x.name, y.name, title)
    for i, txt in enumerate(x.index):
        plt.annotate(txt, (x[i], y[i]))
    plt.show()

def provide_labels(label_for_x_axis,label_for_y_axis,title):
    '''
    
    :param x: data along x axis
    :param y: data along y axis
    :type x: pandas.Series
    :type y: pandas.Series
    '''
    plt.xlabel(label_for_x_axis)
    plt.ylabel(label_for_y_axis)
    plt.title(title)

