import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Display an image given its ID.

image = ee.Image('CGIAR/SRTM90_V4')
# Center the Map.
Map.setCenter(-110, 40, 5)
# Display the image.
Map.addLayer(image, {'min': 0, 'max': 3000}, 'SRTM')

# Display the map.
Map
