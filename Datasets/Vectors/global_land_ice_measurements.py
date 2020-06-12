
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.FeatureCollection('GLIMS/current')
visParams = {
  'palette': ['gray', 'cyan', 'blue'],
  'min': 0.0,
  'max': 10.0,
  'opacity': 0.8,
}

image = ee.Image().float().paint(dataset, 'area')
Map.setCenter(-35.618, 66.743, 7)
Map.addLayer(image, visParams, 'GLIMS/current')
# Map.addLayer(dataset, {}, 'for Inspector', False)

# Display the map.
Map
