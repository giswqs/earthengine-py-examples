
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image('LANDSAT/LC08/C01/T1/LC08_044034_20140318')
print("Number of bands:", image.bandNames().size().getInfo())
imageCollection = ee.ImageCollection(image.bandNames().map(lambda b: image.select([b])))

print("ImageCollection size: ", imageCollection.size().getInfo())

# Display the map.
Map
