from pathlib import Path
from typing_extensions import Annotated

import netCDF4
import typer

from livas_plots import common, per_orbit, utils

app = typer.Typer()


@app.command()
def plot_per_orbit(
    file_path: Path,
    output_directory: Path,
    min_altitude_km: Annotated[float, typer.Option()] = 0.0,
    max_altitude_km: Annotated[float, typer.Option()] = 10,
    fig_size_x: Annotated[float, typer.Option()] = 10,
    fig_size_y: Annotated[float, typer.Option()] = 6,
    trim_lat_start: Annotated[float, typer.Option()] = None,
    trim_lat_end: Annotated[str, typer.Option()] = None,
):
    output_directory.mkdir(exist_ok=True, parents=True)
    print(trim_lat_start, trim_lat_end)
    with netCDF4.Dataset(file_path) as nc:
        # Find start/end indices
        latitude = nc.variables["Latitude"][:]
        start_idx = 0
        end_idx = latitude.shape[0] - 1
        if trim_lat_start is not None:
            start_idx = utils.find_nearest_location(float(trim_lat_start), latitude)[1]
            print("Plotting from index", start_idx)
        if trim_lat_end is not None:
            end_idx = utils.find_nearest_location(float(trim_lat_end), latitude)[1]
            print("Plotting to index", end_idx)

        # Create plots, first trajectory, then profiles
        common.plot_trajectory(
            output_directory,
            nc,
            fig_kwargs={"figsize": (fig_size_x, fig_size_y)},
            trim=(start_idx, end_idx),
        )
        for plot in per_orbit.PER_ORBIT_PLOTS:
            common.plot_profile(
                output_directory,
                plot,
                nc,
                altitude_range=(min_altitude_km, max_altitude_km),
                fig_kwargs={"figsize": (fig_size_x, fig_size_y)},
                trim=(start_idx, end_idx),
            )


def main():
    app()
