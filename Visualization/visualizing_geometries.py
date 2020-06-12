import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Create a geodesic polygon.
polygon = ee.Geometry.Polygon([
  [[-5, 40], [65, 40], [65, 60], [-5, 60], [-5, 60]]
])

# Create a planar polygon.
planarPolygon = ee.Geometry(polygon, {}, False)

polygon = ee.FeatureCollection(polygon)
planarPolygon = ee.FeatureCollection(planarPolygon)

# Display the polygons by adding them to the map.
Map.centerObject(polygon)
Map.addLayer(polygon, {'color': 'FF0000'}, 'geodesic polygon')
Map.addLayer(planarPolygon, {'color': '000000'}, 'planar polygon')


# Display the map.
Map
