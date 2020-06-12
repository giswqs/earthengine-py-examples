
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# This function gets NDVI from Landsat 5 imagery.


def getNDWI(image):
    return image.normalizedDifference(['B3', 'B5'])


image1 = ee.Image('LANDSAT/LT05/C01/T1_TOA/LT05_044034_19900604')

# Compute NDVI from the scene.
ndvi1 = getNDWI(image1)

ndwiParams = {'palette': ['#ece7f2', '#d0d1e6', '#a6bddb', '#74a9cf', '#3690c0', '#0570b0', '#045a8d', '#023858']}

Map.centerObject(image1, 10)
Map.addLayer(ndvi1, ndwiParams, 'NDWI')

# Display the map.
Map
