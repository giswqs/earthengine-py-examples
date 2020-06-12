import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Add some data to the Map
dem = ee.Image("JAXA/ALOS/AW3D30_V1_1").select('MED')
Map.addLayer(dem, {'min': 0, 'max': 5000, 'palette': ['000000', 'ffffff'] }, 'DEM', True)

# TEST Map.setCenter
Map.setCenter(0, 28, 2.5)

# Display the map.
Map
