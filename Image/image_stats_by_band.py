
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image('USDA/NAIP/DOQQ/m_3712213_sw_10_1_20140613')
Map.setCenter(-122.466123, 37.769833, 17)
Map.addLayer(image, {'bands': ['N', 'R','G']}, 'NAIP')

geometry = image.geometry()

means = image.reduceRegions(geometry, ee.Reducer.mean().forEachBand(image), 10)

print(means.getInfo())

# Display the map.
Map
