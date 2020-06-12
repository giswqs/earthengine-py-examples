
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fc = ee.FeatureCollection('TIGER/2018/States') 

print(fc.first().getInfo())

# Use this empty image for paint().
empty = ee.Image().byte()
palette = ['green', 'yellow', 'orange', 'red']

states = empty.paint(**{
  'featureCollection': fc,
  'color': 'ALAND',
})

Map.addLayer(states, {'palette': palette}, 'US States')
# Display the map.
Map
