import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Make a list of Features.
features = [
  ee.Feature(ee.Geometry.Rectangle(30.01, 59.80, 30.59, 60.15), {'name': 'Voronoi'}),
  ee.Feature(ee.Geometry.Point(-73.96, 40.781), {'name': 'Thiessen'}),
  ee.Feature(ee.Geometry.Point(6.4806, 50.8012), {'name': 'Dirichlet'})
]

# Create a FeatureCollection from the list and print it.
fromList = ee.FeatureCollection(features)
print(fromList.getInfo())

# Create a FeatureCollection from a single geometry and print it.
fromGeom = ee.FeatureCollection(ee.Geometry.Point(16.37, 48.225))
print(fromGeom.getInfo())

# Display the map.
Map
