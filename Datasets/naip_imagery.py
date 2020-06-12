import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)
image = ee.Image('USDA/NAIP/DOQQ/m_4609915_sw_14_1_20100629')
Map.addLayer(image, {'bands': ['N', 'R', 'G']}, 'NAIP')
# Display the map.
Map
