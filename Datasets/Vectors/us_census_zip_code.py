
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.FeatureCollection('TIGER/2010/ZCTA5')
visParams = {
  'palette': ['black', 'purple', 'blue', 'green', 'yellow', 'orange', 'red'],
  'min': 500000,
  'max': 1000000000,
}

zctaOutlines = ee.Image().float().paint(**{
  'featureCollection': dataset,
  'color': 'black',
  'width': 1
})

image = ee.Image().float().paint(dataset, 'ALAND10')
# Map.setCenter(-93.8008, 40.7177, 6)
Map.addLayer(image, visParams, 'TIGER/2010/ZCTA5')
Map.addLayer(zctaOutlines, {}, 'borders')
# Display the map.
Map
