
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fc = ee.FeatureCollection('TIGER/2018/States')

print(fc.first().getInfo())

new_fc = fc.select(['STUSPS', 'NAME', 'ALAND'], ['abbr', 'name', 'area'])
print(new_fc.first().getInfo())

propertyNames = new_fc.first().propertyNames()
print(propertyNames.getInfo())
# Display the map.
Map
