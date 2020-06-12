
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

roi = ee.Geometry.Point([-99.2182, 46.7824])

# find images acquired during June and July
collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') \
    .filterBounds(roi) \
    .filter(ee.Filter.calendarRange(6, 7, 'month')) \
    .sort('DATE_ACQUIRED')

print(collection.size().getInfo())

first = collection.first()
propertyNames = first.propertyNames()
print(propertyNames.getInfo())

time_start = ee.Date(first.get('system:time_start')).format("YYYY-MM-dd")
print(time_start.getInfo())
# Display the map.
Map
