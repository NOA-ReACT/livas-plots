import numpy as np


def check_coordinates(loc: tuple[float, float]):
    """
    Checks that the given coordinates are valid.
    The first value should be the Latitude, the second the Longtitude.
    """

    assert len(loc) == 2
    assert -90 <= loc[0] <= 90
    assert -180 <= loc[1] <= 180


def find_nearest_location(l: float, latitude: np.ndarray) -> tuple[float, int]:
    """
    Returns the nearest latitude in the given array, as well as its index.

    Args:
        l: The location to search for (latitude
        latitude: The Latitude array from the LIVAS file.

    Returns:
        A tuple containing the nearest latitude and its index.
    """
    latitude = latitude[:, 1]

    lat_i = np.argmin(np.abs(latitude - l))

    return latitude[lat_i], lat_i
