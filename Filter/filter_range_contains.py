
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

states = ee.FeatureCollection('TIGER/2018/States')
# print(states.first().getInfo())

# Select states with land area between 200,000 km2 and 300,000 km2
selected = states.filter(ee.Filter.rangeContains("ALAND", 200000000000, 300000000000))
Map.centerObject(selected, 6)
Map.addLayer(ee.Image().paint(selected, 0, 2), {'palette': 'yellow'}, 'Selected')
# Display the map.
Map
