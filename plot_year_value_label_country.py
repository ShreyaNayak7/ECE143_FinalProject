#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[6]:


def plot_year_value_label_country(path_of_file):
    '''
    this funtion will plot the value of corresponsing years for each country
    path_of_file: string; is the path of the csv file that needs to be loaded into a dataframe
    '''
    assert isinstance(path_of_file,str)
    import gather_data as gd
    import matplotlib.pyplot as plt
    import pandas as pd
    import gather_data as gd
    import matplotlib.pyplot as plt
    import pandas as pd
    df=gd.gather_data_from_csv(path_of_file)
    get_ipython().run_line_magic('matplotlib', 'inline')

    for name, data in df.groupby('Country'):
        plt.plot(data["Year"],data['Value'], label=name)


    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


# In[2]:





# In[ ]:




