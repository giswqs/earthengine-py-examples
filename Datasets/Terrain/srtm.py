import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)
image = ee.Image('srtm90_v4')
# path = image.getDownloadUrl({
#     'scale': 30,
#     'crs': 'EPSG:4326',
#     'region': '[[-120, 35], [-119, 35], [-119, 34], [-120, 34]]'
# })
vis_params = {'min': 0, 'max': 3000}
Map.addLayer(image, vis_params, 'SRTM')
# Display the map.
Map
