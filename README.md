# LIVAS-plots

This is a utility for plotting LIVAS files, currently it supports only per-orbit
files but we would like to extend it to support the per-grid files as well.

## Usage

The script is called from the command line and takes two arguments, the file to plot
and where to write the output PNG files:

```sh
livas_plots LIVAS_CALIPSO_L2_Orbit_2015-09-23T22-26-37ZN.nc ./plots
```

## Supported plots

### Per-grid

| Name                                                       | Variable path                                                                                                 | Notes                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Feature type                                               | `CALIPSO_Flags_and_Auxiliary/Flags/AVD_Feature_Type`                                                          |                                                                      |
| Aerosol subtype                                            | `CALIPSO_Flags_and_Auxiliary/Flags/AVD_Aerosol_Subtype`                                                       | Will also show Cloud/Totally attenuated bins from Feature Type array |
| Raw Backscatter Coefficient 532nm                          | `CALIPSO_Optical_Products/Total_Backscatter_Coefficient_532`                                                  |                                                                      |
| Backscatter Coefficient 532nm, smoothed ±1 bin             | `LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Backscatter_Coefficient_532`          |
| Backscatter Coefficient 532nm, smoothed ±2 bin             | `LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Backscatter_Coefficient_532`          |
| Raw Particulate Depolarization Ratio 532 nm                | `CALIPSO_Optical_Products/Particulate_Depolarization_Ratio_Profile_532`                                       | Will have the same filtered bins as the smoothed version.            |
| Particulate Depolarization Ratio 532 nm, , smoothed ±1 bin | `LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_180m/Particulate_Depolarization_Ratio_532` |                                                                      |
| Particulate Depolarization Ratio 532 nm, , smoothed ±2 bin | `LIVAS/CALIPSO_Optical_Products_Smoothed/Altitudinally_Smoothed_by_420m/Particulate_Depolarization_Ratio_532` |                                                                      |
| Pure dust Backscatter Coefficient 532nm                    | `LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Backscatter_Coefficient_532`           |                                                                      |
| Pure Dust Coarse Backscatter 532 nm                        | `LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Coarse_Backscatter_Coefficient_532`    |                                                                      |
| Pure Dust Fine Backscatter 532 nm                          | `LIVAS/Cloud_Free/Pure_Dust_and_Fine_Coarse/Optical_Products/Pure_Dust_Fine_Backscatter_Coefficient_532`      |                                                                      |

## Blame

Written by Thanasis Georgiou <ageorgiou@noa.gr>
