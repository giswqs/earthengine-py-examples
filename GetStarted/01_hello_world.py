import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# traditional python string
print('Hello world!')

# Earth Eninge object
print(ee.String('Hello World from Earth Engine!').getInfo())
print(ee.Image('LANDSAT/LC08/C01/T1/LC08_044034_20140318').getInfo())

# Display the map.
Map
