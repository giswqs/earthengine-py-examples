import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.ImageCollection('JRC/GSW1_1/YearlyHistory') \
                  .filter(ee.Filter.date('2015-01-01', '2015-12-31'))
waterClass = dataset.select('waterClass')
waterClassVis = {
  'min': 0.0,
  'max': 3.0,
  'palette': ['cccccc', 'ffffff', '99d9ea', '0000ff'],
}
Map.setCenter(59.414, 45.182, 7)
Map.addLayer(waterClass, waterClassVis, 'Water Class')

# Display the map.
Map
