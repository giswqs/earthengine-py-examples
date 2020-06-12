import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.ImageCollection('JRC/GSW1_1/MonthlyHistory') \
                  .filter(ee.Filter.date('2015-01-01', '2015-12-31'))
water = dataset.select('water').mosaic()
waterVis = {
  'min': 0.0,
  'max': 2.0,
  'palette': ['ffffff', 'fffcb8', '0905ff'],
}
Map.setCenter(-58.999, -3.373, 7)
Map.addLayer(water, waterVis, 'Water')

# Display the map.
Map
