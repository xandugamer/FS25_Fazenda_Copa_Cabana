
import processing

############################################################
####### ADD THE DIRECTORY FOR THE FILES TO SAVE HERE #######
############################################################
############### IT MUST END WITH A SLASH (/) ###############
############################################################

SAVE_DIR = "C:/Users/iwatk/OneDrive/Desktop/"

############################################################

layers = [
    ("Background_FULL", -6059916.2561937375, -6053533.676512374, -1748429.7928881792, -1742047.2129215195),
    ("Background_FULL_margin", -6060416, -6053033, -1748929, -1741547)
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
