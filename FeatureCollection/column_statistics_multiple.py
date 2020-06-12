
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fromFT = ee.FeatureCollection("users/wqs/Pipestem/Pipestem_HUC10")
geom = fromFT.geometry()
Map.centerObject(fromFT)
Map.addLayer(ee.Image().paint(geom, 0, 2), {}, 'Watersheds')

stats = fromFT.reduceColumns(**{
  'reducer': ee.Reducer.sum().repeat(2),
  'selectors': ['AreaSqKm', 'AreaAcres']
  # weightSelectors: ['weight']
}).getInfo()

print(stats)

# Display the map.
Map
