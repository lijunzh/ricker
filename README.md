# Ricker Wavelet Generator

[![PyPI version](https://img.shields.io/pypi/v/ricker)](https://pypi.org/project/ricker/)
![License](https://img.shields.io/pypi/l/ricker)
![Python versions](https://img.shields.io/pypi/pyversions/ricker)
[![CI/CD](https://github.com/lijunzh/ricker/actions/workflows/cicd.yml/badge.svg)](https://github.com/lijunzh/ricker/actions/workflows/cicd.yml)

## Introduction

The [Ricker wavelet](http://wiki.seg.org/wiki/Dictionary:Ricker_wavelet)
(Mexican hat) is widely used in synthetic seismic simulation. While
[SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.ricker.html)
offers a basic generator, this package provides a shifted, causal Ricker
wavelet with configurable peak location — ready for seismic modelling.

## Project status: maintenance mode

ricker is feature-complete, and no new features are planned. It stays
maintained so that it keeps installing and working. What to expect:

- **Compatibility fixes** ship as patch releases when a new Python or NumPy
  version breaks something. CI tests Python 3.10–3.14.
- **Dependencies:** ricker sets no upper version limits, so NumPy fixes
  reach you through your own `pip` or `uv` upgrade, without a new ricker
  release. Dependabot keeps the CI and development tools current.
- **Bug reports and pull requests** are welcome. Review may be slow, and
  new features are unlikely to be merged.

The PyPI release (0.1.2, 2017) names the length parameter `len`; the
code here and the examples below call it `duration`.

## Installation

### From PyPI

```bash
pip install ricker
```

### From source (development)

```bash
git clone https://github.com/lijunzh/ricker.git
cd ricker
uv sync --all-extras --dev
```

## Quick Start

```python
import matplotlib.pyplot as plt
from ricker import ricker

wavelet = ricker(f=25, duration=0.2, dt=0.001, peak_loc=0.1)
plt.plot(wavelet)
plt.title("25 Hz Ricker Wavelet")
plt.show()
```

## API

```python
ricker(f=10, duration=0.5, dt=0.002, peak_loc=0.25)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `f` | float | 10 | Centre frequency (Hz) |
| `duration` | float | 0.5 | Signal length (seconds) |
| `dt` | float | 0.002 | Sampling interval (seconds) |
| `peak_loc` | float | 0.25 | Peak location (seconds) |

## Dependencies

- [NumPy](https://numpy.org/)

## Development

```bash
uv run ruff check src tests   # lint
uv run ruff format src tests  # format
uv run pytest                 # test
uv run pre-commit install     # set up git hooks
```

## Contact

For issues, please open a
[GitHub issue](https://github.com/lijunzh/ricker/issues) or contact
*gatechzhu@gmail.com*.
