# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:49:23 2019

@author: shrey
Editor: Akhil Jain
"""
import gather_data as gd
def cont_cou_map(beginning_of_path=""):
    '''
    gives dataframe that has continent name against country label
    '''
    assert isinstance(beginning_of_path,str)
    #colour file, remove duplicate turkey
    #https://datahub.io/JohnSnowLabs/country-and-continent-codes-list
    cont_raw=gd.gather_data_from_csv(beginning_of_path+"country-and-continent-codes-list.csv",
                                 index='Three_Letter_Country_Code')
    cont_raw = cont_raw.loc[~cont_raw.index.duplicated(keep='last')]
    return cont_raw
