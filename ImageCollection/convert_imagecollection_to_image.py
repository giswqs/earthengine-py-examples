
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

images = ee.ImageCollection('MODIS/MCD43A4') \
    .filterDate('2017-01-01', '2017-01-31') \
    .select(['Nadir_Reflectance_Band1'])

# unmask to ensure we have the same number of values everywhere
images = images.map(lambda i: i.unmask(-1))

# convert to array
array = images.toArray()

# convert to an image
bandNames = images.aggregate_array('system:index')
image = array.arrayProject([0]).arrayFlatten([bandNames])

print(image.getInfo())

bandNames = image.bandNames()
print(bandNames.getInfo())

# Display the map.
Map
