from typing import NamedTuple, Callable, Union
from pathlib import Path

import numpy as np
from netCDF4 import Dataset, Variable as NCVariable
from matplotlib.colors import Colormap, Normalize
from matplotlib.ticker import MultipleLocator, FuncFormatter, LinearLocator
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import (
    LongitudeFormatter,
    LatitudeFormatter,
    LatitudeLocator,
    LongitudeLocator,
)


class Plot(NamedTuple):
    title: str
    variable: Union[str, Callable]
    colorbar: Colormap
    norm: Normalize
    fig_kwargs: dict = {}
    colorbar_kwargs: dict = {}


def lat_lon_formatter(x, pos, latitude, longitude):
    index = np.fix(x).astype(int)
    cx, cy = latitude[index, 1], longitude[index, 1]
    return f"{cx:.2f}°\n{cy:.2f}°"


def plot_profile(
    output_directory: Path,
    info: Plot,
    nc: Dataset,
    altitude_range=(0, 10),
    fig_kwargs={},
    trim=None,
):
    fig, ax = plt.subplots(1, 1, **fig_kwargs)
    fig.suptitle(f"CALIPSO-LIVAS {info.title}")

    if isinstance(info.variable, str):
        var = nc[info.variable]
    else:
        var = info.variable(nc)

    # Time info in title
    time = nc["Profile_Time_Parsed"][:]
    first_day, first_time = time[0][0:10], time[0][11:16]
    last_day, last_time = time[-1][0:10], time[-1][11:16]
    ax.set_title(f"{first_day} {first_time} → {last_time} UTC")

    altitude, latitude, longitude = (
        nc["Altitude"][:],
        nc["Latitude"][:],
        nc["Longitude"][:],
    )

    xx, yy = np.meshgrid(range(longitude.shape[0]), altitude.data)
    v = var[:].T
    v.mask = False

    p = ax.pcolormesh(xx, yy, v, cmap=info.colorbar, norm=info.norm)

    # Colorbar
    units = None
    if isinstance(var, NCVariable):
        if "units" in var.ncattrs():
            units = var.units
    cbar = fig.colorbar(
        p,
        ax=ax,
        label=units,
        **info.colorbar_kwargs,
    )

    # Y Axis
    ax.set_ylim(*altitude_range)
    ax.set_ylabel("Altitude [km]")
    ax.yaxis.set_minor_locator(MultipleLocator(1))

    # x Axis
    ax.set_xlabel("Latitude, Longitude")
    if trim != None:
        ax.set_xlim(trim[0], trim[1])
    ax.xaxis.set_major_locator(LinearLocator(6))
    ax.xaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: lat_lon_formatter(x, pos, latitude, longitude))
    )

    sanitized_title = info.title.replace(" ", "_").replace(",", "")
    filename = output_directory / f"{sanitized_title}.png"
    fig.savefig(filename, dpi=300)


def plot_trajectory(
    output_directory: Path, nc: Dataset, fig_kwargs: dict = {}, trim=None
):
    fig, ax = plt.subplots(
        1, 1, **fig_kwargs, subplot_kw={"projection": ccrs.PlateCarree()}
    )
    fig.suptitle("CALIPSO-LIVAS Trajectory")
    ax.coastlines()
    ax.set_global()

    # Time info in title
    time = nc["Profile_Time_Parsed"][:]
    first_day, first_time = time[0][0:10], time[0][11:16]
    last_day, last_time = time[-1][0:10], time[-1][11:16]
    ax.set_title(f"{first_day} {first_time} → {last_time} UTC")

    # Plot trajectory
    latitude, longitude = nc["Latitude"][:, 1], nc["Longitude"][:, 1]
    ax.scatter(
        longitude,
        latitude,
        label="Trajectory",
        color="r",
        s=1,
        transform=ccrs.PlateCarree(),
    )
    ax.scatter(
        longitude[0],
        latitude[0],
        label="Start",
        color="g",
        s=15,
        transform=ccrs.PlateCarree(),
    )

    # Plot trim, if used
    if trim != None:
        ax.scatter(
            longitude[trim[0] : trim[1]],
            latitude[trim[0] : trim[1]],
            label="Visible",
            color="b",
            s=1,
            transform=ccrs.PlateCarree(),
        )

    # Add ticks
    ax.yaxis.tick_right()
    ax.set_xticks([-180, -120, -60, 0, 60, 120, 180], crs=ccrs.PlateCarree())
    ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    ax.legend()

    filename = output_directory / "trajectory.png"
    fig.savefig(filename, dpi=300)
