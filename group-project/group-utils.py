
from pdgstaging import TileStager
import matplotlib.pyplot as plt
import geopandas as gpd
import random

def initialize_stager(dir_input, dir_staged):
    iwp_config = {
        # The directory and file type of the input vector data the we want to stage
        'dir_input': dir_input,
        'ext_input': '.gpkg',
        # The path to the directory where we want the output tiles to be saved
        # (this will be created if it doesn't exist)
        'dir_staged': dir_staged,
        # Set simplify_tolerance to None to disable polygon simplification (not needed)
        'simplify_tolerance': None
    }

    # Create an instance of the TileStager class, which we can use to 
    iwp_stager = TileStager(iwp_config)
    return(iwp_stager)


def random_hex_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)

def plot_tiles(stager):

    # set up plotting
    plt.style.use('seaborn-notebook')
    font_size = 4
    plt.rcParams['font.size'] = font_size
    plt.rcParams['axes.labelsize'] = font_size
    plt.rcParams['axes.titlesize'] = font_size
    plt.rcParams['xtick.labelsize'] = font_size
    plt.rcParams['ytick.labelsize'] = font_size
    plt.rcParams['legend.fontsize'] = font_size
    plt.rcParams['figure.titlesize'] = font_size
    plt.rcParams['figure.dpi'] = 200

    staged_files = stager.tiles.get_filenames_from_dir('staged')

    if length(staged_files) > 91:
        staged_files = staged_files[0:92]
        print(f'{len(staged_files)} are present. Only plotting the first 91 files.')


    ax = None
    for tile in staged_files:
        gdf = gpd.read_file(tile)
        if ax is None:
            ax = gdf.plot(color=random_hex_color())
        else:
            gdf.plot(ax=ax, color=random_hex_color())

    plt.show()