import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('JRC/GSW1_1/Metadata')
detectionsObservations = dataset.select(['detections', 'valid_obs', 'total_obs'])
visParams = {
  'min': 100.0,
  'max': 900.0,
}
Map.setCenter(4.72, -2.48, 2)
Map.addLayer(detectionsObservations, visParams, 'Detections/Observations')

# Display the map.
Map
