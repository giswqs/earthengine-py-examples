import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('WWF/HydroSHEDS/03CONDEM')
elevation = dataset.select('b1')
elevationVis = {
  'min': -50.0,
  'max': 3000.0,
  'gamma': 2.0,
}
Map.setCenter(-121.652, 38.022, 8)
Map.addLayer(elevation, elevationVis, 'Elevation')


dataset = ee.Image('WWF/HydroSHEDS/03VFDEM')
elevation = dataset.select('b1')
elevationVis = {
  'min': -50.0,
  'max': 3000.0,
  'gamma': 2.0,
}
Map.setCenter(-121.652, 38.022, 8)
Map.addLayer(elevation, elevationVis, 'Elevation Void Filled')

# Display the map.
Map
