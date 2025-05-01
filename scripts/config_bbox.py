
layers = [
    ("Overview_bbox", -6058852.492913511, -6054597.439792601, -1747365.911082492, -1743110.8578770505),
    ("Overview_bbox_with_margin", -6059352, -6054097, -1747865, -1742610)
]
for layer in layers:
    name = "Bounding_Box_" + layer[0]
    north, south, east, west = layer[1:]

    # Create a rectangle geometry from the bounding box.
    rect = QgsRectangle(north, east, south, west)

    # Create a new memory layer to hold the bounding box.
    layer = QgsVectorLayer("Polygon?crs=EPSG:3857", name, "memory")
    provider = layer.dataProvider()

    # Add the rectangle as a feature to the layer.
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromRect(rect))
    provider.addFeatures([feature])

    # Add the layer to the map.
    QgsProject.instance().addMapLayer(layer)

    # Set the fill opacity.
    symbol = layer.renderer().symbol()
    symbol_layer = symbol.symbolLayer(0)

    # Set the stroke color and width.
    symbol_layer.setStrokeColor(QColor(0, 255, 0))
    symbol_layer.setStrokeWidth(0.2)
    symbol_layer.setFillColor(QColor(0, 0, 255, 0))
    layer.triggerRepaint()
