import numpy as np

from matplotlib.ticker import FuncFormatter

from livas_plots import colors
from livas_plots.common import Plot


def copy_filter(nc, source_var, target_var):
    arr = nc[target_var][:]
    mask = np.isnan(nc[source_var][:])

    arr[mask] = np.nan
    return arr


def aerosol_subtype_variable(nc):
    subtype = nc["CALIPSO_Flags_and_Auxiliary/Flags/AVD_Aerosol_Subtype"][:]
    ftype = nc["CALIPSO_Flags_and_Auxiliary/Flags/AVD_Feature_Type"][:]

    subtype[ftype == 2] = 11
    subtype[ftype == 9] = 12

    return subtype


PER_ORBIT_PLOTS = [
    ## AVD-related arrays
    Plot(
        title="Feature Type",
        variable="CALIPSO_Flags_and_Auxiliary/Flags/AVD_Feature_Type",
        colorbar=colors.feature_type_cbar,
        colorbar_kwargs={
            "ticks": np.arange(0, 11, 1) - 0.5,
            "format": FuncFormatter(colors.feature_type_cbar_tick_formatter),
        },
        norm=colors.feature_type_norm,
    ),
    Plot(
        title="Aerosol Subtype",
        # variable="CALIPSO_Flags_and_Auxiliary/Flags/AVD_Aerosol_Subtype",
        variable=aerosol_subtype_variable,
        colorbar=colors.aerosol_subtype_cbar,
        colorbar_kwargs={
            "ticks": np.arange(0, 14, 1) - 0.5,
            "format": FuncFormatter(colors.aerosol_subtype_cbar_tick_formatter),
        },
        norm=colors.aerosol_subtype_norm,
    ),
    ## Backscatter vs Smoothing
    Plot(
        title="Raw Total Backscatter 532 nm",
        variable="CALIPSO_Optical_Products/Total_Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Total Backscatter 532 nm, smoothed ±1 bin",
        variable="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Total Backscatter 532 nm, smoothed ±2 bins",
        variable="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    ## Depol vs smoothing
    Plot(
        title="Particulate Depolarization Ratio 532 nm",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Particulate_Depolarization_Ratio_532",
            target_var="CALIPSO_Optical_Products/Particulate_Depolarization_Ratio_Profile_532",
        ),
        # variable="CALIPSO_Optical_Products/Particulate_Depolarization_Ratio_Profile_532",
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    Plot(
        title="Particulate Depolarization Ratio 532 nm, smoothed ±1 bin",
        variable="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Particulate_Depolarization_Ratio_532",
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    Plot(
        title="Particulate Depolarization Ratio 532 nm, smoothed ±2 bin",
        variable="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Particulate_Depolarization_Ratio_532",
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    # Cloud free backscatter vs smoothing
    Plot(
        title="Raw Total Backscatter 532 nm (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="CALIPSO_Optical_Products/Total_Backscatter_Coefficient_532",
        ),
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Total Backscatter 532 nm, smoothed ±1 bin (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Backscatter_Coefficient_532",
        ),
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Total Backscatter 532 nm, smoothed ±2 bins (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Backscatter_Coefficient_532",
        ),
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    # Cloud free backscatter vs smoothing
    Plot(
        title="Particulate Depolarization Ratio 532 nm (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="CALIPSO_Optical_Products/Particulate_Depolarization_Ratio_Profile_532",
        ),
        # variable="CALIPSO_Optical_Products/Particulate_Depolarization_Ratio_Profile_532",
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    Plot(
        title="Particulate Depolarization Ratio 532 nm, smoothed ±1 bin (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Particulate_Depolarization_Ratio_532",
        ),
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    Plot(
        title="Particulate Depolarization Ratio 532 nm, smoothed ±2 bin (Cloud-free)",
        variable=lambda nc: copy_filter(
            nc,
            source_var="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
            target_var="LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Particulate_Depolarization_Ratio_532",
        ),
        colorbar=colors.depol_cbar,
        colorbar_kwargs={
            "ticks": colors.depol_bins,
        },
        norm=colors.depol_norm,
    ),
    ## Pure dust, fine/coarse mode arrays
    Plot(
        title="Pure Dust Backscatter 532 nm",
        variable="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Pure Dust Coarse Backscatter 532 nm",
        variable="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Coarse_Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
    Plot(
        title="Pure Dust Fine Backscatter 532 nm",
        variable="LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Fine_Backscatter_Coefficient_532",
        colorbar=colors.backscatter_cbar,
        colorbar_kwargs={
            "ticks": colors.backscatter_bins,
            "format": FuncFormatter(colors.backscatter_cbar_tick_formatter),
        },
        norm=colors.backscatter_norm,
    ),
]
