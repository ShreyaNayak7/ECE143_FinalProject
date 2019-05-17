import pandas as pd
def gather_data_from_csv(path_of_file):
    '''
    This function is used to gather data from a file that has an extension of "csv".
    
    :path_of_file: string; is the path of the csv file that needs to be loaded into a dataframe
    '''
    assert isinstance(path_of_file,str)
    df=pd.read_csv(path_of_file)
    return df

def gather_data_from_Excel_file(path_of_file, sh_name):
    ''''
    This function is used to gather data from an excel file into a dataframe
    
    :path_of_file: string; is the path of the excel file that contains data
    :sh_name: string; name of the sheet that has the data
    '''
    assert isinstance(path_of_file,str)
    assert isinstance(sh_name,str)
    df=pd.read_excel(path_of_file, sheet_name=sh_name)
    return df