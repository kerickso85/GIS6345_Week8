import geopandas
import matplotlib.pyplot as plt

filename="StreetCenterlines.shp"
centerlines=geopandas.read_file(filename)
#print('StreetCenterlines.shp imported as type: ',type(centerlines)) #validation
#print(centerlines.shape) #debug statement
print(centerlines.head()) #a glimpse of what we're looking at


#create 20x20 plot with the shape lengths colorized by percentile
#increased line width and a different color map
centerlines.plot(figsize=(20,20), column='LENGTH', scheme='percentiles', 
                 linewidth=2.5, legend=True, cmap='cividis_r')


plt.show() #display the shapefile contents





