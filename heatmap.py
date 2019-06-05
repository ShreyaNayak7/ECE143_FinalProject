#!/usr/bin/env python
# coding: utf-8

# In[1]:


def draw_heatmap_linear(acc, acc_desc, depth_list):
    '''this function will draw a linear heatmap, acc : list, acc_desc: string, depth_list:list of rows
    Here is the sample input.
    #acc = grid.cv_results_['mean_train_score'].reshape(5,1)
    #draw_heatmap_linear(acc, 'accuracy', D_list)
    '''
    assert isinstance(acc_desc,str)
   
    assert isinstance(acc,list)
    assert isinstance(depth_list,list)
    import scipy.io as sio
    import matplotlib.pyplot as plt
    import numpy as np
    import seaborn as sns
    from sklearn import tree
    from sklearn.model_selection import GridSearchCV
    import math
    import scipy
    plt.figure(figsize = (2,4))
    ax = sns.heatmap(acc, annot=True, fmt='.3f', yticklabels=depth_list, xticklabels=[])
    ax.collections[0].colorbar.set_label("accuracy")
    ax.set(ylabel='depth')
    plt.title(acc_desc + ' w.r.t depth')
    sns.set_style("whitegrid", {'axes.grid' : False})
    plt.show()
#train_acc = grid.cv_results_['mean_train_score'].reshape(5,1)
#draw_heatmap_linear(train_acc, 'train accuracy', D_list)


# In[ ]:


def draw_heatmap_RBF(acc, acc_desc, gamma_list, C_list):
    '''this function will draw a 2D heatmap, acc : list, acc_desc: string, depth_list:list of rows
    here is the sample input.
    #acc = grid.cv_results_['meanscore'].reshape(4,4)
    #draw_heatmap_RBF(acc, ' accuracy', gamma_list, C_list)
    '''
    assert isinstance(acc_desc,str)
    assert isinstance(C_list,list)
    assert isinstance(acc,list)
    assert isinstance(gamma_list,list)
    import seaborn as sns
    from sklearn import svm
    from sklearn.model_selection import GridSearchCV
    from mpl_toolkits.mplot3d import Axes3D

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from mpl_toolkits.mplot3d import Axes3D
    import math
    get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
    get_ipython().run_line_magic('matplotlib', 'inline')
    from sklearn.utils import shuffle
    import scipy.io as sio
    plt.rcParams['figure.figsize'] = 8,8
    plt.figure(figsize = (5,4))
    ax = sns.heatmap(acc, annot=True, fmt='.3f', 
                     xticklabels=gamma_list, yticklabels=C_list)
    ax.collections[0].colorbar.set_label("accuracy")
    ax.set(xlabel = '$\gamma$', ylabel='$C$')
    plt.title(acc_desc + ' w.r.t $C$ and $\gamma$')
    sns.set_style("whitegrid", {'axes.grid' : False})
    plt.show()
    


# In[ ]:




