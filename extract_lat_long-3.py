# Program extracting first column 
import xlrd 
#Import important libraries




loc = ("mental.xls") 
key="AIzaSyAfyuaeIDdIqkNVPtLC_198Jk6hK2JG7DI"
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
longitude=[]
latitude=[]
for i in range(sheet.nrows):

	if str(type(sheet.cell_value(i, 9)))=="<class 'float'>" and str(type(sheet.cell_value(i, 8)))=="<class 'float'>":
	    longitude.append(sheet.cell_value(i, 9)) 
	    latitude.append(sheet.cell_value(i, 8))


#Your Google_API_Key

y_12=latitude
x_12=longitude
#Import important libraries
from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(y_12[0], x_12[0], 13)

# Polygon

# gmap.plot(latitude, longitude, 'cornflowerblue', edge_width=10)

# Scatter points
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

gmap.scatter(latitude,longitude, '#3B0B39', size=10, marker=False)

# Marker
hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
for index,value in enumerate(latitude):
	gmap.marker(latitude[index], longitude[index], 'cornflowerblue')
gmap.apikey=key
# Draw
gmap.draw("my_map.html")