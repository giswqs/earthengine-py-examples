
#!/usr/bin/env python
"""Download example."""

import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Get a download URL for an image.
image1 = ee.Image('srtm90_v4')
path = image1.getDownloadUrl({
    'scale': 30,
    'crs': 'EPSG:4326',
    'region': '[[-120, 35], [-119, 35], [-119, 34], [-120, 34]]'
})

print(path)
vis_params = {'min': 0, 'max': 3000}
Map.addLayer(image1, vis_params)

# Display the map.
Map
