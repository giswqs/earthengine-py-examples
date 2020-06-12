import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/Global/ALOS_topoDiversity')
alosTopographicDiversity = dataset.select('constant')
alosTopographicDiversityVis = {
  'min': 0.0,
  'max': 1.0,
}
Map.setCenter(-111.313, 39.724, 6)
Map.addLayer(
    alosTopographicDiversity, alosTopographicDiversityVis,
    'ALOS Topographic Diversity')

# Display the map.
Map
