import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/US/physioDiversity')
physiographicDiversity = dataset.select('b1')
physiographicDiversityVis = {
  'min': 0.0,
  'max': 1.0,
}
Map.setCenter(-94.625, 39.825, 7)
Map.addLayer(
    physiographicDiversity, physiographicDiversityVis,
    'Physiographic Diversity')

# Display the map.
Map
