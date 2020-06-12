
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fromFT = ee.FeatureCollection("users/wqs/Pipestem/Pipestem_HUC10")
geom = fromFT.geometry()
Map.centerObject(fromFT)
Map.addLayer(ee.Image().paint(geom, 0, 2), {}, 'Watersheds')

print(fromFT.aggregate_stats('AreaSqKm'))

total_area = fromFT.reduceColumns(**{
  'reducer': ee.Reducer.sum(),
  'selectors': ['AreaSqKm']
  # weightSelectors: ['weight']
}).getInfo()

print("Total area: ", total_area)

# Display the map.
Map
