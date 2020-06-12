import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/Global/ALOS_CHILI')
alosChili = dataset.select('constant')
alosChiliVis = {
  'min': 0.0,
  'max': 255.0,
}
Map.setCenter(-105.8636, 40.3439, 11)
Map.addLayer(alosChili, alosChiliVis, 'ALOS CHILI')

# Display the map.
Map
