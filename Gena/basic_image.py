import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image.pixelLonLat() \
    .add([180, 90]).divide([360, 180])

# image = image.multiply(50).sin()

Map.setCenter(0, 28, 2.5)
Map.addLayer(image, {}, 'coords', True)

# Display the map.
Map
