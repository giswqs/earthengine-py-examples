import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# get a single feature
countries = ee.FeatureCollection("USDOS/LSIB_SIMPLE/2017")
country = countries.filter(ee.Filter.eq('country_na', 'Ukraine'))

# TEST: add feature to the Map
Map.addLayer(country, { 'color': 'orange' }, 'feature')

# set Map center using coordinates and zoom
Map.setCenter(31.472, 49.044, 6)

# Display the map.
Map
