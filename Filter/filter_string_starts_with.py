
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)


states = ee.FeatureCollection('TIGER/2018/States')

# Select states its name starting with 'Al'
selected = states.filter(ee.Filter.stringStartsWith('NAME', 'Al'))


Map.centerObject(selected, 6)
Map.addLayer(ee.Image().paint(selected, 0, 2), {'palette': 'yellow'}, 'Selected')

# Display the map.
Map
