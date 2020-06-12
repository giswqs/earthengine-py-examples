import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Create a FeatureCollection from an Earth Engine Table.

# Load census roads.
roads = ee.FeatureCollection('TIGER/2016/Roads')

# Get only interstates.
interstates = roads.filter(ee.Filter.eq('rttyp', 'I'))

# Get only surface roads.
surfaceRoads = roads.filter(ee.Filter.eq('rttyp', 'M'))

# Display the roads in different colors.
Map.addLayer(surfaceRoads, {'color': 'black'}, 'surface roads')
Map.addLayer(interstates, {'color': 'red'}, 'interstates')


# Display the map.
Map
