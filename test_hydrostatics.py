import numpy as np

from hydrostatics import (
    simpson_rule,
    waterplane_area,
    waterplane_coefficient,
    volume_of_displacement,
    block_coefficient,
)

# Reference data (table of offsets)
HALF_BREADTHS = np.array([0.2, 1.8, 3.1, 3.6, 3.2, 2.0, 0.4])
SECTIONAL_AREAS = np.array([1, 12, 20, 23, 19, 10, 2])
SPACING = 5

LENGTH = 30
BEAM = 7.2
DRAFT = 3


def test_simpson_rule():
    # Simpson is exact for a constant function: integral of 1 over length = L
    values = np.array([1, 1, 1, 1, 1, 1, 1])
    assert np.isclose(simpson_rule(values, SPACING), 30.0)


def test_waterplane_area():
    assert np.isclose(waterplane_area(HALF_BREADTHS, SPACING), 142.6667)


def test_waterplane_coefficient():
    area = waterplane_area(HALF_BREADTHS, SPACING)
    assert np.isclose(waterplane_coefficient(area, LENGTH, BEAM), 0.6605, atol=1e-4)


def test_volume_of_displacement():
    assert np.isclose(volume_of_displacement(SECTIONAL_AREAS, SPACING), 435.0)


def test_block_coefficient():
    volume = volume_of_displacement(SECTIONAL_AREAS, SPACING)
    assert np.isclose(block_coefficient(volume, LENGTH, BEAM, DRAFT), 0.6713, atol=1e-4)
