
import ee
import geemap

# Create a map centered at (lat, lon).
Map = geemap.Map(center=[40, -100], zoom=4)


def set_color(f):
    c = ee.String(f.get('COLOR')).slice(1)
    return f \
        .set('R', ee.Number.parse(c.slice(0, 2), 16)) \
        .set('G', ee.Number.parse(c.slice(2, 4), 16)) \
        .set('B', ee.Number.parse(c.slice(4, 6), 16))


fc = ee.FeatureCollection('RESOLVE/ECOREGIONS/2017') \
    .map(lambda f: set_color(f))

base = ee.Image(0).mask(0).toInt8()
Map.addLayer(base.paint(fc, 'R')
             .addBands(base.paint(fc, 'G')
                       .addBands(base.paint(fc, 'B'))), {'gamma': 0.3})



# # Load a FeatureCollection from a table dataset: 'RESOLVE' ecoregions.
# ecoregions = ee.FeatureCollection('RESOLVE/ECOREGIONS/2017')

# # Display as default and with a custom color.
# Map.addLayer(ecoregions, {}, 'default display', False)
# Map.addLayer(ecoregions, {'color': 'FF0000'}, 'colored', False)


# Map.addLayer(ecoregions.draw(**{'color': '006600', 'strokeWidth': 5}), {}, 'drawn', False)


# # Create an empty image into which to paint the features, cast to byte.
# empty = ee.Image().byte()

# # Paint all the polygon edges with the same number and 'width', display.
# outline = empty.paint(**{
#   'featureCollection': ecoregions,
#   'color': 1,
#   'width': 3
# })
# Map.addLayer(outline, {'palette': 'FF0000'}, 'edges')
# Display the map.
Map
