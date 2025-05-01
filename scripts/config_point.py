
layers = [
    ("Overview_bbox", -6058852.492913511, -6054597.439792601, -1747365.911082492, -1743110.8578770505),
    ("Overview_bbox_with_margin", -6059352, -6054097, -1747865, -1742610)
]
for layer in layers:
    name = "Points_" + layer[0]
    north, south, east, west = layer[1:]

    top_left = QgsPointXY(north, west)
    top_right = QgsPointXY(north, east)
    bottom_right = QgsPointXY(south, east)
    bottom_left = QgsPointXY(south, west)

    points = [top_left, top_right, bottom_right, bottom_left, top_left]

    # Create a new layer
    layer = QgsVectorLayer('Point?crs=EPSG:3857', name, 'memory')
    provider = layer.dataProvider()

    # Add fields
    provider.addAttributes([QgsField("id", QVariant.Int)])
    layer.updateFields()

    # Create and add features for each point
    for i, point in enumerate(points):
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(point))
        feature.setAttributes([i + 1])
        provider.addFeature(feature)

    layer.updateExtents()

    # Add the layer to the project
    QgsProject.instance().addMapLayer(layer)
