
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

roi = ee.Geometry.Point([-99.2182, 46.7824])

collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') \
    .filterBounds(roi) \
    .filter(ee.Filter.calendarRange(6, 6, 'month')) \
    .sort('DATE_ACQUIRED')

print(collection.size().getInfo())

first = ee.Image(collection.first())
print(first.bandNames().getInfo())
print(first.bandTypes().getInfo())

# Display the map.
Map
