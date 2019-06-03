# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 21:01:41 2019

@author: shrey
"""
import gather_data as gd
from bokeh.plotting import Figure,show,output_file
from bokeh.models import Select,CustomJS,ColumnDataSource,HoverTool
from bokeh.layouts import row,widgetbox

output_file('line.html')

#format and clean data
df = gd.gather_data_from_Excel('Govt exp imf 2.xls', sh_name='exp')
df.rename(columns={'Government expenditure, percent of GDP (% of GDP)':'Country_name'},
                   inplace=True)
df.drop([0],inplace=True)
df=df.T
new_header = df.iloc[0]
df = df[1:]
df.columns = new_header
df.index.names=['Year']
df.columns.names=['Countries']
df.drop(list(range(1800,1880)),inplace=True)
df.drop(df.iloc[:, -2::], inplace = True, axis = 1)
df1=df[['Argentina','Australia','Germany','India','Italy','Japan','United States',
        'United Kingdom']].copy()
#######################
#########dropdown menu###########
#from bokeh.io import output_file, show
#from bokeh.models.widgets import Dropdown
#from bokeh.io import output_file, show
#from bokeh.layouts import widgetbox
#from bokeh.models.widgets import Dropdown
#from bokeh.plotting import curdoc
#countries=df1.keys()
#countries2=list(zip(countries, countries))
#countries2=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Angola', 'Angola'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ("China, People's Republic of", "China, People's Republic of"), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo, Dem. Rep. of the', 'Congo, Dem. Rep. of the'), ('Congo, Republic of ', 'Congo, Republic of '), ('Costa Rica', 'Costa Rica'), ('Croatia', 'Croatia'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ("Côte d'Ivoire", "Côte d'Ivoire"), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominican Republic', 'Dominican Republic'), ('Egypt', 'Egypt'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('Gambia, The', 'Gambia, The'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong Kong SAR', 'Hong Kong SAR'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea, Republic of', 'Korea, Republic of'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyz Republic', 'Kyrgyz Republic'), ('Lao P.D.R.', 'Lao P.D.R.'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Lithuania', 'Lithuania'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Moldova', 'Moldova'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Macedonia ', 'North Macedonia '), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russian Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovak Republic', 'Slovak Republic'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('South Africa', 'South Africa'), ('South Sudan, Republic of', 'South Sudan, Republic of'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('São Tomé and Príncipe', 'São Tomé and Príncipe'), ('Taiwan Province of China', 'Taiwan Province of China'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')]
#output_file("dropdown.html")
#menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
#dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=countries2)
#def function_to_call(attr, old, new):
#    print (dropdown.value)

#dropdown.on_change('value', function_to_call)

#curdoc().add_root(dropdown)
#show(dropdown)
##########################################
#pick initial country
country='United States'
col=df1.columns.get_loc(country)

#prepare dictionary with data, one entry for each country
data=df1.to_dict(orient='list')
data['x']=df1.index.tolist()

source_available = ColumnDataSource(data=data)
source_visible=ColumnDataSource(data={'x' : df1.index.tolist(),
                                      'y' : df1.loc[:,country].tolist()
                                      })
p = Figure(x_axis_label='year', y_axis_label='Government Expenditure (% of GDP)')
p.line(y='y',x='x',source=source_visible)
p.circle(y='y',x='x',source=source_visible,size=4,hover_fill_color='firebrick',
         hover_line_color='white')

#hovertool parameters
hover = HoverTool(
                  tooltips=[
                            ('Year',"$x{0f}"),
                            ('Value',"$y%")],
                  mode='vline'
                  )
p.add_tools(hover)

#select widget callback
select = Select(title="Country", options=df1.columns.tolist(), value=country)
        
select.callback = CustomJS(args=dict(source_visible=source_visible,
                                     source_available=source_available), code="""
    var data_visible = source_visible.data;
    var data_available = source_available.data;
    var f = cb_obj.value;
    data_visible.y = data_available[f];
    source_visible.change.emit();
        """)

show(row(p,widgetbox(select)))
