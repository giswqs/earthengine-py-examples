
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

HUC10 = ee.FeatureCollection("USGS/WBD/2017/HUC10")
HUC08 = ee.FeatureCollection('USGS/WBD/2017/HUC08')
roi = HUC08.filter(ee.Filter.eq('name', 'Pipestem'))

Map.centerObject(roi, 10)
Map.addLayer(ee.Image().paint(roi, 0, 1), {}, 'HUC8')

bound = ee.Geometry(roi.geometry()).bounds()
Map.addLayer(ee.Image().paint(bound, 0, 1), {'palette': 'red'}, "Minimum bounding geometry")

# Display the map.
Map
