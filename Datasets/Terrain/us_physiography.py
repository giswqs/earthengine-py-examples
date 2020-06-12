import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/US/physiography')
physiography = dataset.select('constant')
physiographyVis = {
  'min': 1100.0,
  'max': 4220.0,
}
Map.setCenter(-105.4248, 40.5242, 8)
Map.addLayer(physiography, physiographyVis, 'Physiography')

# Display the map.
Map
