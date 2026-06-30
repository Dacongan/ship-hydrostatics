import numpy as np


def simpson_rule(values, spacing):
    """Integrate equally spaced values using Simpson's first rule."""
    if len(values) % 2 == 0:
        raise ValueError("Simpson's first rule needs an odd number of points")
    n = len(values)
    multipliers = np.zeros(n)
    multipliers[0], multipliers[-1] = 1, 1
    for i in range(1, n - 1):
        multipliers[i] = 2 if i % 2 == 0 else 4
    return spacing / 3 * np.dot(values, multipliers)


def waterplane_area(half_breadths, spacing):
    """Waterplane area from a table of half-breadths (both sides)."""
    return 2 * simpson_rule(half_breadths, spacing)


def waterplane_coefficient(waterplane_area, length, beam):
    """Cw = Aw / (L * B)."""
    return waterplane_area / (length * beam)


def volume_of_displacement(sectional_areas, spacing):
    """Volume of displacement from sectional areas along the length."""
    return simpson_rule(sectional_areas, spacing)


def block_coefficient(volume, length, beam, draft):
    """Cb = V / (L * B * T)."""
    return volume / (length * beam * draft)