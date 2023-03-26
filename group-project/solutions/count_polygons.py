import geopandas as gpd
from grouputils import initialize_stager

iwp_stager = initialize_stager("/home/shares/example-pdg-data/SCC-2023")

staged_files = iwp_stager.tiles.get_filenames_from_dir('staged')

num_rows_all = []
for file in staged_files:
    gdf = gpd.read_file(file)
    num_rows = len(file)
    num_rows_all.append(num_rows)

num_polygons = sum(num_rows_all)

print(f"The total number of polygons is {num_polygons}.")
