
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image('LANDSAT/LC8_L1T/LC80260412017023LGN00')
b5 = image.select('B5')

Map.centerObject(image, 10)
Map.addLayer(image, {}, 'Band 5')

selected = image.select(["B5", 'B4', 'B3'], ['Nir', 'Red', 'Green'])
Map.addLayer(selected, {}, "Renamed bands")
print(selected.bandNames().getInfo())


# Display the map.
Map
