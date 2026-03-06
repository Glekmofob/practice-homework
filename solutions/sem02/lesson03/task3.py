import numpy as np


def get_extremum_indices(
    ordinates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if (np.size(ordinates)) < 3:
        raise ValueError
    moved_left = ordinates[:-2]
    moved_right = ordinates[2:]
    check_area = ordinates[1:-1]
    max_mask = (check_area > moved_left) & (check_area > moved_right)
    min_mask = (check_area < moved_left) & (check_area < moved_right)
    return (
        np.where(min_mask)[0] + 1,
        np.where(max_mask)[0] + 1,
    )  # where return tuple of arrays of indexes for each axis, sooo need[0] to work, source: google
