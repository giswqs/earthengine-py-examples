import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)
dataset = ee.Image('JRC/GSW1_1/GlobalSurfaceWater')
occurrence = dataset.select('occurrence');
occurrenceVis = {'min': 0.0, 'max': 100.0, 'palette': ['ffffff', 'ffbbbb', '0000ff']}
Map.setCenter(59.414, 45.182, 6)
Map.addLayer(occurrence, occurrenceVis, 'Occurrence')
# Display the map.
Map
