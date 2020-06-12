import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# get a single feature
countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
country = countries.filter(ee.Filter.eq('country_na', 'Ukraine'))
Map.addLayer(country, { 'color': 'orange' }, 'feature collection layer')

# TEST: center feature on a map
Map.centerObject(country, 6)

# Display the map.
Map
