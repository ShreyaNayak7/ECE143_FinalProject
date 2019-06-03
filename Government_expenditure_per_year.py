def Government_expenditure_per_year(countries_list):
    '''this function plot the Government_expenditure_per_year
    its input will be a list of strings which is countries name
    '''  
    assert isinstance(countries_list, list)
    import pandas as pd
    import gather_data as gd
    from bokeh.plotting import figure,show,output_file,ColumnDataSource
    from bokeh.models import HoverTool

    import gather_data as gd
    import matplotlib.pyplot as plt
    import pandas as pd
    import gather_data as gd
    import matplotlib.pyplot as plt
    import pandas as pd


    # In[2]:



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

    df2=df1.replace('no data',0)


    %matplotlib inline
    import matplotlib.pyplot as plt
    df2[countries_list].plot()
    #.legend(['A simple line'])

    plt.show()

