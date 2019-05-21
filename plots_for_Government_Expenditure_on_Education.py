def plot_change_in_Government_Expenditure_on_Education():
    import gather_data
    import pandas
    data_frame_1=gather_data.gather_data_from_Excel_file("../../Downloads/Downloaded_Data_for_the_Final_Project_for_ECE_143/API_SE.XPD.TOTL.GD.ZS_DS2_en_excel_v2_10576899.xls","Data")
    data_frame_1.plot.scatter("Unnamed: 46", "Unnamed: 56")
