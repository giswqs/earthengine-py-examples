import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.ImageCollection('JRC/GSW1_1/MonthlyRecurrence').first()
monthlyRecurrence = dataset.select('monthly_recurrence')
monthlyRecurrenceVis = {
  'min': 0.0,
  'max': 100.0,
  'palette': ['ffffff', 'ffbbbb', '0000ff'],
}
Map.setCenter(-51.482, -0.835, 9)
Map.addLayer(monthlyRecurrence, monthlyRecurrenceVis, 'Monthly Recurrence')

# Display the map.
Map
