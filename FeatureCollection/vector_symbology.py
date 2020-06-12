
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fc = ee.FeatureCollection('TIGER/2018/States')
# .filter(ee.Filter.eq('STUSPS', 'MN'))

image = ee.Image().paint(**{
    'featureCollection': fc,
    'color': 1,
    'width': 3
})

Map.setCenter(-99.844, 37.649, 5)
Map.addLayer(image, {'palette': 'FF0000'}, 'TIGER/2018/States')
# Map.addLayer(fc, {}, 'US States')

# Display the map.
Map
