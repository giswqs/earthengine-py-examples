import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)
img = ee.Image("COPERNICUS/S2_SR/20191115T074201_20191115T075706_T37MBM") 
ndvi = img.normalizedDifference(['B8','B4'])
pal = ["red","yellow","green"]
Map.setCenter(36.9,-7.7, 12)
Map.addLayer(ndvi,{'min':0,'max':0.8,'palette':pal},'NDVI')
# Display the map.
Map
