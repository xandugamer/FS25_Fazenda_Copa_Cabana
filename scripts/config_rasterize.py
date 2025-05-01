
import processing

############################################################
####### ADD THE DIRECTORY FOR THE FILES TO SAVE HERE #######
############################################################
############### IT MUST END WITH A SLASH (/) ###############
############################################################

SAVE_DIR = "C:/Users/iwatk/OneDrive/Desktop/"

############################################################

layers = [
    ("Overview_bbox", -6058852.492913511, -6054597.439792601, -1747365.911082492, -1743110.8578770505),
    ("Overview_bbox_with_margin", -6059352, -6054097, -1747865, -1742610)
]

for layer in layers:
    name = layer[0]
    north, south, east, west = layer[1:]

    epsg3857_string = str(north) + "," + str(south) + "," + str(east) + "," + str(west) + " [EPSG:3857]"
    file_path = SAVE_DIR + name + ".tif"

    processing.run(
        "native:rasterize",
        {
            "EXTENT": epsg3857_string,
            "EXTENT_BUFFER": 0,
            "TILE_SIZE": 64,
            "MAP_UNITS_PER_PIXEL": 1,
            "MAKE_BACKGROUND_TRANSPARENT": False,
            "MAP_THEME": None,
            "LAYERS": None,
            "OUTPUT": file_path,
        },
)
