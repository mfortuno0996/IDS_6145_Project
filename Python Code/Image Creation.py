import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(20,20))
def draw_Map(c1, c2, c3, c4):
    """initialize a basemap. For purposes of the project, the Hellenic Trench is used"""

    return Basemap(projection='lcc', resolution='i',
                   llcrnrlon=c1, urcrnrlon=c2,
                   llcrnrlat=c3, urcrnrlat=c4,
                   lat_1=36.4, lon_0=22.4,
                   area_thresh=100)

He_Tr = draw_Map(20, 26.3, 34, 38.5) #Hellenic Trench

He_Tr.drawcoastlines() #draws the coastlines, default color is black
He_Tr.fillcontinents(color='red') #fills in land color


df1 = pd.read_csv("C:/Users/mfort/IDS_6145_Project/58968/all_ais.csv") #CSV file obtained from https://www.seanoe.org/data/00459/57040/
df1_reduced = df1.drop(df1.index[1000000:], axis = 0) #shortens the excel file to be the first 1 million rows of data for time reduction
He_Tr.scatter(df1_reduced.iloc[:,6], df1_reduced.iloc[:,7], latlon = True, color='navy', s=1) #plots ship position on map

plt.savefig(fname = "C:/Users/mfort/IDS_6145_Project/Hellenic Trench Ships.png", bbox_inches = 'tight')
#saves figure as "Hellenic Trench Ships"; bbox_inches is called to prevent undesirable white space
plt.show()