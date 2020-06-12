

import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image('srtm90_v4')

smoothed = image.reduceNeighborhood(**{
    'reducer': ee.Reducer.mean(),
    'kernel': ee.Kernel.square(3),
})

# vis_params = {'min': 0, 'max': 3000}
# Map.addLayer(image, vis_params, 'SRTM original')
# Map.addLayer(smooth, vis_params, 'SRTM smoothed')
Map.setCenter(-112.40, 42.53, 12)
Map.addLayer(ee.Terrain.hillshade(image), {}, 'Original hillshade')
Map.addLayer(ee.Terrain.hillshade(smoothed), {}, 'Smoothed hillshade')

# Display the map.
Map
