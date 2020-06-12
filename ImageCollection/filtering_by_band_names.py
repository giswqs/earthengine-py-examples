
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

roi = ee.Geometry.Point([-99.2182, 46.7824])


collection = ee.ImageCollection('USDA/NAIP/DOQQ') \
    .filterBounds(roi) \
    .filter(ee.Filter.listContains("system:band_names", "N"))
print(collection.size().getInfo())

first = collection.first()
Map.centerObject(first, 13)
Map.addLayer(first, {'bands': ['N', 'R', 'G']}, 'NAIP')
# Display the map.
Map
