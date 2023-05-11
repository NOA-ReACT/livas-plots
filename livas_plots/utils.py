import numpy as np


def check_coordinates(loc: tuple[float, float]):
    """
    Checks that the given coordinates are valid.
    The first value should be the Latitude, the second the Longtitude.
    """

    assert len(loc) == 2
    assert -90 <= loc[0] <= 90
    assert -180 <= loc[1] <= 180


def find_nearest_location(
    loc: tuple[float, float], latitude: np.ndarray, longitude: np.ndarray
) -> tuple[tuple[float, float], tuple[int, int]]:
    """
    Given a pair of coordinates and the Latitude, Longitude arrays of a LIVAS file,
    returns the nearest location in the file and its index.

    Args:
        loc: The location to search for (latitude, longitude)
        latitude: The Latitude array from the LIVAS file.
        longitude: The Longitude array from the LIVAS file.

    Returns:
        A tuple containing two tuples: the first tuple contains the nearest location in
        the file (latitude, longitude pair), the second tuple contains the index of the
        nearest location in the file (latitude index, longitude index pair)
    """
    assert latitude.shape == longitude.shape
    check_coordinates(loc)

    latitude = latitude[:, 1]
    longitude = longitude[:, 1]

    lat_i = np.argmin(np.abs(latitude - loc[0]))
    lon_i = np.argmin(np.abs(longitude - loc[1]))

    return (latitude[lat_i], longitude[lon_i]), (lat_i, lon_i)
