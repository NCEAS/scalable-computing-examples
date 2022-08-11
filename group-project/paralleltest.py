import os
from datetime import datetime

# For parallel processing
import parsl
import parsl
from parsl import python_app
from parsl.config import Config
from parsl.channels import LocalChannel
from parsl.executors import HighThroughputExecutor
from parsl.executors import ThreadPoolExecutor
from parsl.providers import LocalProvider

# helpers
from grouputils import initialize_rasterizer
from grouputils import initialize_stager
from grouputils import plot_tiles

iwp_rasterizer = initialize_rasterizer("/home/jclark/example-data")
staged_paths = iwp_rasterizer.tiles.get_filenames_from_dir('staged')

# Set up Parsl:
activate_env = 'workon scomp'
htex_local = Config(
    executors=[
        HighThroughputExecutor(
            label="htex_local",
            worker_debug=False,
            cores_per_worker=1,
            max_workers=88,
            provider=LocalProvider(
                channel=LocalChannel(),
                init_blocks=1,
                max_blocks=1,
                worker_init=activate_env
            )
        )
    ],
)
parsl.clear()
parsl.load(htex_local)

# Because rasterization is relatively quick, we want each parsl "task" to process a batch of tiles.
def make_batch(items, batch_size):
    # Create batches of a given size from a list of items.
    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

batch_size = 10
batches = make_batch(staged_paths, batch_size)

# Make a Parsl app that uses the rasterize_vectors method
@python_app
def rasterize(staged_paths, rasterizer):
    # Rasterize a batch of vector files
    return rasterizer.rasterize_vectors(staged_paths, make_parents=False)

# Rasterize the batches in parallel
app_futures = []
for batch in batches:
    app_future = rasterize(batch, iwp_rasterizer)
    app_futures.append(app_future)

# Don't continue to print message until all tiles have been rasterized
done = [app_future.result() for app_future in app_futures]