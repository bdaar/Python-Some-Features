#Import Library
import folium

#Create base map
map = folium.Map(location=[X,Y], zoom_start = 12)

#Multiple Markers
folium.Marker(location= [X, Y], popup= "Place Name",tooltip= "None" , icon=folium.Icon(color = 'red')).add_to(map)
#Save the map
map.save("Map.html")