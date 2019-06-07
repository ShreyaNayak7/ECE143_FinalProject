import pandas as pd
class DataHandler:

    @staticmethod
    def gather_data_from_csv(path_of_file,index='default',header=0,fillnan='no_fill'):
        '''
        This function is used to gather data from a file that has an extension of "csv".
        
        :path_of_file: string; is the path of the csv file that needs to be loaded into a dataframe
        :index: string; gives the name of column that needs to be set as the index; 
        'default' implies no specific column to be set as the index
        :fillnan: integer,string; specifies the value that will replace nan in the dataframe
        '''
        assert isinstance(path_of_file,str)
        df=pd.read_csv(path_of_file,header=header)
        if index!='default':
            df=df.set_index(index)
        if fillnan!='no_fill':
            df=df.fillna(fillnan)
        return df

    @staticmethod
    def gather_data_from_Excel(path_of_file, sh_name,index='default',header=0,fillnan='no_fill'):
        ''''
        This function is used to gather data from an excel file into a dataframe
    
        :path_of_file: string; is the path of the excel file that contains data
        :sh_name: string; name of the sheet that has the data
        'default' implies no specific column to be set as the index
        :fillnan: integer,string; specifies the value that will replace nan in the dataframe
        '''
        assert isinstance(path_of_file,str)
        assert isinstance(sh_name,str)
        df=pd.read_excel(path_of_file, sheet_name=sh_name,header=header)
        if index!='default':
            df=df.set_index(index)
        if fillnan!='no_fill':
            df=df.fillna(fillnan)
        return df
    @staticmethod
    def cont_cou_map(file_path):
        '''
        gives dataframe that has continent name against country label
        Inputs: file path
                (str)
                Gives path where file is located
        '''
        assert isinstance(file_path,str)
        #colour file, remove duplicate turkey
        #https://datahub.io/JohnSnowLabs/country-and-continent-codes-list
        cont_raw=pd.read_csv(file_path)
        cont_raw.set_index('Three_Letter_Country_Code',inplace=True)                              
        cont_raw = cont_raw.loc[~cont_raw.index.duplicated(keep='last')]
        return cont_raw

