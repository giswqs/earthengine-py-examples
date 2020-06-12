
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.FeatureCollection('projects/google/wrs2_descending')

empty = ee.Image().byte()

Map.setCenter(-78, 36, 8)
Map.addLayer(empty.paint(dataset, 0, 2), {}, 'Landsat WRS-2 grid')
# Display the map.
Map
