
#!/usr/bin/env python
"""Select by attributes

"""

import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)

# Select North Dakota and South Dakota
fc = ee.FeatureCollection('TIGER/2018/States') \
    .filter(ee.Filter.Or(
        ee.Filter.eq('STUSPS', 'ND'),
        ee.Filter.eq('STUSPS', 'SD'),
    ))

image = ee.Image().paint(fc, 0, 2)
# Map.setCenter(-99.844, 37.649, 5)
Map.centerObject(fc, 6)
Map.addLayer(image, {'palette': 'FF0000'}, 'TIGER/2018/States')



# Display the map.
Map
