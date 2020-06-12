
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)


SD = ee.FeatureCollection('TIGER/2018/States') \
    .filter(ee.Filter.eq('STUSPS', 'SD'))

ND = ee.FeatureCollection('TIGER/2018/States') \
    .filter(ee.Filter.eq('STUSPS', 'ND'))

states = SD.merge(ND)
Map.centerObject(states, 6)
Map.addLayer(ee.Image().paint(states, 0, 2), {}, 'Dakotas')
# print(states.size().getInfo())

# Display the map.
Map
