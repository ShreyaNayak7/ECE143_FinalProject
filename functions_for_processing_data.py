import pandas as pd

class process_data:
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