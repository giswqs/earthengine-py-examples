#!/usr/bin/env python
"""Display an image given its ID."""

import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

image = ee.Image('srtm90_v4')
vis_params = {'min': 0, 'max': 3000}
Map.addLayer(image, vis_params,"SRTM")
Map.setCenter(0,0, 2)

# Display the map.
Map
