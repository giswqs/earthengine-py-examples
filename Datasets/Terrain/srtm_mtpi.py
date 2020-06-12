import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.Image('CSP/ERGo/1_0/Global/SRTM_mTPI')
srtmMtpi = dataset.select('elevation')
srtmMtpiVis = {
  'min': -200.0,
  'max': 200.0,
  'palette': ['0b1eff', '4be450', 'fffca4', 'ffa011', 'ff0000'],
}
Map.setCenter(-105.8636, 40.3439, 11)
Map.addLayer(srtmMtpi, srtmMtpiVis, 'SRTM mTPI')

# Display the map.
Map
