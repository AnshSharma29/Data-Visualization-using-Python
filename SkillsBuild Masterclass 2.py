# Masterclass 2 codes

#import libraries 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline

#import dataset
titanic=pd.read_csv(r'Path of titanic dataset')

#importing sweetviz #pip install sweetviz
import sweetviz as sv

#analyzing the dataset 
titanic_report = sv.analyze(titanic)

#display the report
titanic_report.show_html(titanic.html)

#using dtale library
d=dtale.show(titanic)
d.open_browser()



#import folium
import folium

# Coordinates for New York City
latitude, longitude = 40.7128, -74.0060

# Create a map centered at New York City
m = folium.Map(location=[latitude, longitude], zoom_start=12)

# Add a marker for New York City
folium.Marker([latitude, longitude], popup='New York City').add_to(m)

#save the map to an HTML file
m.save('map.html')


