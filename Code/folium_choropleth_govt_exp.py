import os
from class_gather_data import DataHandler as dh
from class_plot_functions import Choropleth as choro

#load json file that contains the map
world_geo = os.path.join(r'C:\Users\shrey\A_Repository_for_the_Final_Project_for_ECE_143', 'countries.geo.json')
#load data
file_1="D:/ECE 143/Data files for Project/001_Main SPEED Dataset 2015.xls"
df = dh.gather_data_from_Excel(file_1,
                               sh_name='poptotal_ppp',index='country')
# make Choropleth object
m = choro(location=[30,15],zoom_start=2.4,
          geo_data=world_geo,data=df,
          columns=['ISO', 2009],
          key_on='feature.id',
          legend_name='Government Expenditure per capita(US$), 2009',
          fill_color="YlGn")   

mapp=m.make_map()
m.add_marker(mapp,[([49.463803,6.18632],"Luxembourg $30.2k"),
              ([41.850033,-87.6500523],"USA $10.45k"),
              ([35,104],"China $1.6k")])                          
m.save(mapp,"my_plot.html")
