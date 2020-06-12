
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# LSIB: Large Scale International Boundary Polygons, Simplified

# dataset = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017')
# styleParams = {
#   'fillColor': 'b5ffb4',
#   'color': '00909F',
#   'width': 3.0,
# }
# countries = dataset.style(**styleParams)
# Map.addLayer(countries, {}, 'USDOS/LSIB_SIMPLE/2017')


# LSIB: Large Scale International Boundary Polygons, Detailed
dataset = ee.FeatureCollection('USDOS/LSIB/2013')
visParams = {
  'palette': ['f5ff64', 'b5ffb4', 'beeaff', 'ffc0e8', '8e8dff', 'adadad'],
  'min': 0.0,
  'max': 894.0,
  'opacity': 0.8,
}
image = ee.Image().float().paint(dataset, 'iso_num')
Map.addLayer(image, visParams, 'USDOS/LSIB/2013')
# Map.addLayer(dataset, {}, 'for Inspector', False)

# Display the map.
Map
