import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('USGS/NED')
elevation = dataset.select('elevation')
elevationVis = {
  'min': 0.0,
  'max': 4000.0,
  'gamma': 1.6,
}
Map.setCenter(-100.55, 40.71, 5)
Map.addLayer(elevation, elevationVis, 'Elevation')

# Display the map.
Map
