# Ship Hydrostatics

A small Python module to compute basic hydrostatic properties of a ship
hull from a table of offsets, using Simpson's rule.

## What it computes

- **Waterplane area** (`Aw`)
- **Waterplane area coefficient** (`Cw`)
- **Volume of displacement** (`∇`)
- **Block coefficient** (`Cb`)

All areas and volumes are integrated with Simpson's first rule.

## The math

Simpson's first rule (for an even number of intervals):

$$\int_0^L f(x)\,dx \approx \frac{h}{3}\left(f_0 + 4f_1 + 2f_2 + \cdots + 4f_{n-1} + f_n\right)$$

Form coefficients:

$$C_w = \frac{A_w}{L \cdot B} \qquad C_b = \frac{\nabla}{L \cdot B \cdot T}$$

## How to use

```python
import numpy as np
from hydrostatics import waterplane_area, waterplane_coefficient

half_breadths = np.array([0.2, 1.8, 3.1, 3.6, 3.2, 2.0, 0.4])
spacing = 5  # distance between stations (m)

area = waterplane_area(half_breadths, spacing)
print(area)  # 142.67
```

See `hydrostatics_demo.ipynb` for a full example with a plot.

## Functions

| Function | Returns |
| --- | --- |
| `simpson_rule(values, spacing)` | Integral by Simpson's first rule |
| `waterplane_area(half_breadths, spacing)` | Waterplane area `Aw` |
| `waterplane_coefficient(area, length, beam)` | Coefficient `Cw` |
| `volume_of_displacement(sectional_areas, spacing)` | Volume `∇` |
| `block_coefficient(volume, length, beam, draft)` | Coefficient `Cb` |

## Run the tests

```bash
pip install -r requirements.txt
pytest
```

All four results are checked against known values.

## Note

`simpson_rule` needs an even number of intervals (an odd number of
points). Other cases (Simpson's 3/8 rule, combined rules) are planned.

## License

MIT — see `LICENSE`.
