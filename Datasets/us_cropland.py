
# Metadata: https://developers.google.com/earth-engine/datasets/catalog/USDA_NASS_CDL

import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

dataset = ee.ImageCollection('USDA/NASS/CDL') \
                  .filter(ee.Filter.date('2017-01-01', '2018-12-31')) \
                  .first()
cropLandcover = dataset.select('cropland')
Map.setCenter(-100.55, 40.71, 4)
Map.addLayer(cropLandcover, {}, 'Crop Landcover')

# Display the map.
Map
