
import ee 
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

fromFT = ee.FeatureCollection("users/wqs/Pipestem/Pipestem_HUC10")
# This function computes the feature's geometry area and adds it as a property.
def addArea(feature):
  return feature.set({'areaHa': feature.geometry().area().divide(100 * 100)})


# Map the area getting function over the FeatureCollection.
areaAdded = fromFT.map(addArea)
# Print the first feature from the collection with the added property.

first = areaAdded.first()
print('First feature: ', first.getInfo())
print("areaHa: ", first.get("areaHa").getInfo())

# Display the map.
Map
