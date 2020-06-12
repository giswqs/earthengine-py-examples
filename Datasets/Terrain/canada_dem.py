import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.ImageCollection('NRCan/CDEM')
elevation = dataset.select('elevation').mosaic()
elevationVis = {
  'min': -50.0,
  'max': 1500.0,
  'palette': ['0905ff', 'ffefc4', 'ffffff'],
}
Map.setCenter(-139.3643, 63.3213, 9)
Map.addLayer(elevation, elevationVis, 'Elevation')

# Display the map.
Map
