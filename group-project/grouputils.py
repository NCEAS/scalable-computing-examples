
from pdgstaging import TileStager
from pdgraster import RasterTiler
import matplotlib.pyplot as plt
import geopandas as gpd
import random


def initialize_stager(dir_input):
    iwp_config = {
        # The directory and file type of the input vector data
        # that we want to stage
        'dir_input': dir_input,
        'ext_input': '.gpkg',
        # The path to the directory where we want the output tiles to be saved
        # (this will be created if it doesn't exist)
        'dir_staged': "staged",
        'simplify_tolerance': None
    }

    # Create an instance of the TileStager class, which we can use to
    iwp_stager = TileStager(iwp_config)
    return iwp_stager


def initialize_rasterizer(dir_input):

    # Here are the extra options we will use for rasterization
    iwp_config_raster = {
        'dir_input': dir_input,
        'ext_input': '.gpkg',
        # The path to the directory where we want the output tiles to be saved
        # (this will be created if it doesn't exist)
        'dir_staged': 'staged',
        'simplify_tolerance': None,
        # Where to store the output raster tiles (.tif)
        'dir_geotiff': 'geotiff',
        # Where to store the output web tiles (.png)
        'dir_web_tiles': 'web_tiles',
        # We will calculate TWO statistics.
        #  Each statistic will result in a separate
        # band in the output GeoTIFF.
        'statistics': [
            {
                # The first statistic will count the number of IWP
                # that are located in each pixel in the output GeoTIFF.
                'name': 'number_IWP_per_pixel',
                'weight_by': 'count',
                'property': 'centroids_per_pixel',
                'aggregation_method': 'sum',
                'resampling_method': 'sum',
                'palette': ['rgb(102 51 153 / 0.0)',
                            '#d93fce',
                            'lch(85% 100 85)'],
                # Across ALL the data, the minimum number of polygons per pixel
                # will always be zero, but the maximum will depend on the
                # number of polygons in the input vector data, and the size of
                #  the pixel. It will be calculated dynamically.
                'val_range': [0, None]
            },
            {
                # The second statistic will calculate the proportion
                # of that each pixel in the GeoTIFF is covered by IWP.
                'name': 'prop_pixel_covered_by_IWP',
                'weight_by': 'area',
                'property': 'area_per_pixel_area',
                'aggregation_method': 'sum',
                'resampling_method': 'average',
                'palette': ['rgb(102 51 153 / 0.0)', 'lch(85% 100 85)'],
                # Since we are calculating a proportion, the min and max
                # proportion of a pixel that can be covered by IWP will be
                # 0 and 1, respectively.
                'val_range': [0, 1]
            }
        ],
    }

    # Create an instance of the TileStager class, which we can use to
    iwp_stager = RasterTiler(iwp_config_raster)
    return (iwp_stager)


def random_hex_color():
    return '#%06x' % random.randint(0, 0xFFFFFF)


def plot_tiles(stager):

    # set up plotting
    # plt.style.use('seaborn-white')
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

    if len(staged_files) > 45:
        print(f'{len(staged_files)} are present.\
             Only plotting the first 45 files.')
        staged_files = staged_files[0:46]

    ax = None
    for tile in staged_files:
        gdf = gpd.read_file(tile)
        if ax is None:
            ax = gdf.plot(color=random_hex_color(), figsize=(11, 11))
        else:
            gdf.plot(ax=ax, color=random_hex_color(), figsize=(11, 11))

    plt.show()
