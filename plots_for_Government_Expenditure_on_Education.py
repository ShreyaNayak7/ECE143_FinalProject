def plot_some_data__Government_Expenditure_on_Education():
    import gather_data
    import pandas
    import plot_functions
    data_frame_1=gather_data.gather_data_from_Excel("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/API_SE.XPD.TOTL.GD.ZS_DS2_en_excel_v2_10576899.xls","Data")
    title=data_frame_1.loc[5][2]
    xdata=data_frame_1.loc[21][4:]
    ydata=data_frame_1.loc[51][4:]
    plot_functions.scatter_plot(xdata,ydata,1000000,title)
    # data_frame_1.plot.scatter("Unnamed: 46", "Unnamed: 56")
def gather_data__Government_Expenditure_on_Education():
    import gather_data
    data_frame_1=gather_data.gather_data_from_Excel("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/API_SE.XPD.TOTL.GD.ZS_DS2_en_excel_v2_10576899.xls","Data")
    return data_frame_1
