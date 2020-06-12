import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/US/topoDiversity')
usTopographicDiversity = dataset.select('constant')
usTopographicDiversityVis = {
  'min': 0.0,
  'max': 1.0,
}
Map.setCenter(-111.313, 39.724, 6)
Map.addLayer(
    usTopographicDiversity, usTopographicDiversityVis,
    'US Topographic Diversity')

# Display the map.
Map
