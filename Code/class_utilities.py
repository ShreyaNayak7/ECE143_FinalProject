import pandas as pd


class Utilities:
    
    @staticmethod
    def remove_spaces(df):
        '''
        replaces whitespace in column names with underscore
        Inputs: df
                (pd.DataFrame)
                Pandas dataframe that has column names with white spaces 
                and need to be replaced by underscore
        '''
        assert isinstance(df,pd.DataFrame)
        df.columns = [c.replace(' ', '_') for c in df.columns]
        return df
    
    @staticmethod
    def pivot(df,index_new,columns_new,values_new):
        '''
        Pivot a table based on index and values
        Inputs: df
                Pandas dataframe that needs to be pivoted
        '''
        assert isinstance(df,pd.DataFrame)
        assert isinstance(index_new, str)
        assert isinstance(columns_new, str)
        assert isinstance(values_new, str)
        df_piv=pd.pivot_table(df,index=index_new,columns=columns_new,values=values_new)
        return df_piv
    
    @staticmethod
    def trim(df1,df2,df3=None):
        '''
        Find intersection of dataframes based on indices and return trimmed dataframes
        Inputs: df1
                (pd.DataFrame or pd.Series)
                One of the DataFrames to concatenate
               
                df2
                (pd.DataFrame or pd.Series)
                One of the DataFrames to concatenate
               
                df3
                (pd.DataFrame or pd.Series)
                One of the DataFrames to concatenate
        '''
        assert (isinstance(df1,pd.DataFrame) or isinstance(df1,pd.Series))
        assert (isinstance(df2,pd.DataFrame) or isinstance(df2,pd.Series))
        if df3 is None:
            inx=df1.index & df2.index
            df1_trim=df1.loc[inx]
            df2_trim=df2.loc[inx]
            return df1_trim,df2_trim
            
        else:
            assert (isinstance(df3,pd.DataFrame) or isinstance(df3,pd.Series))  
            inx=df1.index & df2.index & df3.index
            df1_trim=df1.loc[inx]
            df2_trim=df2.loc[inx]
            df3_trim=df3.loc[inx]
            return df1_trim,df2_trim,df3_trim
    
    @staticmethod
    def pipeline(df,year,name):
        '''
        Does series data formatting and filtering operations for the priority bar graph
        Inputs: df
                (pd.DataFrame)
                The dataframe which contains data for the graph
                
                year
                (integer)
                Year to be used for the graph
                
                name
                (str)
                The new name of the column to be plotted
        '''
        assert isinstance(df,pd.DataFrame)
        assert isinstance(year,int)
        assert isinstance(name,str)        
        df_col=df[year].copy()
        df_col.dropna(inplace=True)
        df_col.sort_values(ascending=True,inplace=True)
        df_col_df=df_col.to_frame()
        df_col_df.rename(columns = {year: name},inplace=True)
        
        return df_col_df
         

    
    @staticmethod
    def return_modified_data_frame(data_frame,list_of_tuples):
        '''
        This function is used to return a Pandas DataFrame that includes just four specified columns.
        :type data_frame: Pandas DataFrame
        :type list_of_tuples: list
        :param list_of_tuples: a list of tuples such that each tuple contains both the name of a column and a string
        '''
        assert isinstance(list_of_tuples,list)
        assert len(list_of_tuples)==4
        for a_tuple in list_of_tuples:
            assert len(a_tuple)==2
            assert isinstance(a_tuple[1],str)
        assert isinstance(data_frame, pd.DataFrame)
        return data_frame[(data_frame[list_of_tuples[0][0]] == list_of_tuples[0][1]) & (data_frame[list_of_tuples[1][0]] == list_of_tuples[1][1]) & (data_frame[list_of_tuples[2][0]] == list_of_tuples[2][1]) & (data_frame[list_of_tuples[3][0]] == list_of_tuples[3][1]) ]

         
         
               
        
        
        
        
        
