
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('USGS/NLCD/NLCD2016')
landcover = ee.Image(dataset.select('landcover'))

Map.setCenter(-95, 38, 5)
Map.addLayer(landcover.randomVisualizer(), {}, 'Landcover')

# Display the map.
Map
