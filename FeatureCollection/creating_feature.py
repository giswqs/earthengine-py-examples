import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Create an ee.Geometry.
polygon = ee.Geometry.Polygon([
  [[-35, -10], [35, -10], [35, 10], [-35, 10], [-35, -10]]
])

# Create a Feature from the Geometry.
polyFeature = ee.Feature(polygon, {'foo': 42, 'bar': 'tart'})


print(polyFeature.getInfo())
Map.addLayer(polyFeature, {}, 'feature')


# Display the map.
Map
