
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

HUC10 = ee.FeatureCollection("USGS/WBD/2017/HUC10")
HUC08 = ee.FeatureCollection('USGS/WBD/2017/HUC08')
roi = HUC08.filter(ee.Filter.eq('name', 'Pipestem'))

Map.centerObject(roi, 10)
Map.addLayer(ee.Image().paint(roi, 0, 3), {}, 'HUC08')

# select polygons intersecting the roi
roi2 = HUC10.filter(ee.Filter.contains(**{'leftValue': roi.geometry(), 'rightField': '.geo'}))
Map.addLayer(ee.Image().paint(roi2, 0, 2), {'palette': 'blue'}, 'HUC10')

# roi3 = HUC10.filter(ee.Filter.stringContains(**{'leftField': 'huc10', 'rightValue': '10160002'}))
# # print(roi3)
# Map.addLayer(roi3)

# Display the map.
Map
