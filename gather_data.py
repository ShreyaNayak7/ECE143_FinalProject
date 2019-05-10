import pandas as pd
def gather_data_from_csv(path_of_file):
    '''
    This function is used to gather data from a file that has an extension of "csv".

    :path_of_file: string
    '''

    assert isinstance(path_of_file,str)
    file_1=open(path_of_file)
    rows=file_1.readlines()
    for counter_1 in range(len(rows)):
        columns[counter_1]=rows[counter_1].split(",")
    done=False
    while( not done):
        for counter_2 in range(len(len(rows))):
            for counter_3 in range(len(len(colums(counter_2)))):
                all_elements[number_of_elements]=columns[counter_2][counter_3]
                number_of_elements=number_of_elements+1
        done=True

    return all_elements, columns, rows

def gather_data_from_Excel_file(path_of_file, sh_name):
    ''''
    This function is used to gather data from an excel file into a dataframe
    path_of_file: is the path of the excel file that conytains data
    sh_name: name of the sheet that has the data
    '''
    assert isinstance(path_of_file,str)
    assert isinstance(sh_name,str)
    df=pd.read_excel(path_of_file, sheet_name=sh_name)
    return df