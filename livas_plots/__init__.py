from pathlib import Path
from typing_extensions import Annotated

import netCDF4
import typer

from livas_plots import common, per_orbit

app = typer.Typer()


@app.command()
def plot_per_orbit(
    file_path: Path,
    output_directory: Path,
    start_location: Annotated[str, typer.Option()] = None,
    end_location: Annotated[str, typer.Option()] = None,
    min_altitude_km: Annotated[float, typer.Option()] = 0.0,
    max_altitude_km: Annotated[float, typer.Option()] = 10,
    fig_size_x: Annotated[float, typer.Option()] = 10,
    fig_size_y: Annotated[float, typer.Option()] = 6,
):
    output_directory.mkdir(exist_ok=True, parents=True)
    with netCDF4.Dataset(file_path) as nc:
        common.plot_trajectory(
            output_directory, nc, fig_kwargs={"figsize": (fig_size_x, fig_size_y)}
        )
        for plot in per_orbit.PER_ORBIT_PLOTS:
            common.plot_profile(
                output_directory,
                plot,
                nc,
                altitude_range=(min_altitude_km, max_altitude_km),
                fig_kwargs={"figsize": (fig_size_x, fig_size_y)},
            )


def main():
    app()
