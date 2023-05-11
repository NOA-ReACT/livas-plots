from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap
import numpy as np

## Backscatter profile colors
backscatter_colors = [
    "#062ea4",
    "#062ea4",
    "#117ef9",
    "#117ef9",
    "#117ef9",
    "#117ef9",
    "#117ef9",
    "#22fead",
    "#107d7d",
    "#16a85b",
    "#fffe45",
    "#fffe45",
    "#fed23b",
    "#fea832",
    "#fd7e29",
    "#fd5723",
    "#fd161d",
    "#fd3157",
    "#fd577e",
    "#fd7fa7",
    "#474747",
    "#636363",
    "#808080",
    "#999999",
    "#b2b2b2",
    "#c6c6c6",
    "#e0e0e0",
    "#eaeaea",
    "#efefef",
    "#f1f1f1",
    "#f4f4f4",
    "#f8f8f8",
    "#fdfcfc",
    "#fffeff",
]
backscatter_bins = [
    1e-4,
    2e-4,
    3e-4,
    4e-4,
    5e-4,
    6e-4,
    7e-4,
    8e-4,
    9e-4,
    1e-3,
    1.5e-3,
    2e-3,
    2.5e-3,
    3e-3,
    3.5e-3,
    4e-3,
    4.5e-3,
    5e-3,
    5.5e-3,
    6e-3,
    6.5e-3,
    7e-3,
    7.5e-3,
    8e-3,
    1e-2,
    2e-2,
    3e-2,
    4e-2,
    5e-2,
    6e-2,
    7e-2,
    8e-2,
    9e-2,
    1e-1,
]

backscatter_norm = BoundaryNorm(backscatter_bins, len(backscatter_colors), clip=True)
backscatter_cbar = LinearSegmentedColormap.from_list(
    "CALIOP_Backscatter", backscatter_colors, len(backscatter_bins)
)


def backscatter_cbar_tick_formatter(x, pos):
    exp = np.floor(np.log10(np.abs(x)))
    x = x / 10**exp
    if x == 1:
        return f"${x:.1f}\\times 10^{{{int(exp)}}}$"
    else:
        return f"${x:.1f}$"


## Depolarization ratio profile colors
depol_colors = [
    "#00aaff",
    "#00d400",
    "#ffff00",
    "#ffaa01",
    "#fe0000",
    "#ff00fe",
    "#ffd4ff",
    "#ab55fe",
    "#646464",
    "#969696",
]
depol_bins = [
    # -3, -2, -1,
    0,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1,
]
depol_labels = [
    # "Clouds",
    # "Attenuated/Surface",
    # "Clear",
    "0.1",
    "0.2",
    "0.3",
    "0.4",
    "0.5",
    "0.6",
    "0.7",
    "0.8",
    "0.9",
    "1",
]
depol_norm = BoundaryNorm(depol_bins, len(depol_colors), clip=True)
depol_cbar = LinearSegmentedColormap.from_list(
    "CALIOP_Depolarization", depol_colors, len(depol_bins)
)


## Feature type profile colors
feature_type_colors = [
    "#1f77b4",
    "#00E5FF",
    "#9932CC",
    "#FFC107",
    "#FF3D00",
    "#C6FF00",
    "#00a600",
    "#9E9E9E",
    "#000000",
]
feature_type_cbar = LinearSegmentedColormap.from_list(
    "CALIOP_FeatureType", feature_type_colors, len(feature_type_colors)
)
feature_type_norm = BoundaryNorm(range(1, 11), 9, clip=True)
feature_type_labels = [
    "Clear Air",
    "Cloud",
    "Low Confidence Cloud",
    "Aerosol",
    "Low Confidence Aerosol",
    "Stratospheric",
    "Surface",
    "Subsurface",
    "Attenuated",
]


def feature_type_cbar_tick_formatter(x, pos):
    i = int(np.floor(x))
    return feature_type_labels[i - 1]


## Feature subtype profile colors
aerosol_subtype_colors = [
    "#ffffff",
    "#0000fe",
    "#ffff01",
    "#ffb300",
    "#00a600",
    "#994c00",
    "#000000",
    "#008ec2",
    "#c6c6c6",
    "#8a8a8a",
    "#515151",
    "#b22222",
    "#ee82ee",
]
aerosol_subtype_cbar = LinearSegmentedColormap.from_list(
    "CALIOP_AerosolSubtype", aerosol_subtype_colors, len(aerosol_subtype_colors)
)
aerosol_subtype_norm = BoundaryNorm(range(0, 14), 13, clip=True)
aerosol_subtype_labels = [
    "N/A",
    "Marine",
    "Dust",
    "Polluted Continetal/Smoke",
    "Clean Continetal",
    "Polluted Dust",
    "Elevated Smoke",
    "Dusty Marine",
    "PSC Aerosol",
    "Volcanic Ash",
    "Sulfate/Other",
    "Cloud",
    "Totally Attenuated",
]


def aerosol_subtype_cbar_tick_formatter(x, pos):
    i = int(np.floor(x))
    return aerosol_subtype_labels[i]
