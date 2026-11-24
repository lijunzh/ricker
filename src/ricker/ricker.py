"""Ricker (Mexican hat) wavelet generator for seismic simulation."""

from __future__ import annotations

import warnings

import numpy as np
from numpy.typing import NDArray


def ricker(
    f: float = 10,
    duration: float = 0.5,
    dt: float = 0.002,
    peak_loc: float = 0.25,
    *,
    len: float | None = None,
) -> NDArray[np.floating]:
    """Generate a shifted causal Ricker wavelet (Mexican hat).

    Parameters
    ----------
    f : float
        Centre frequency in Hz (default ``10``).
    duration : float
        Signal length in seconds (default ``0.5``).
    dt : float
        Time sampling interval in seconds (default ``0.002``).
    peak_loc : float
        Location of the wavelet peak in seconds (default ``0.25``).
    len : float, optional
        Deprecated alias for *duration*, the name used up to 0.1.2. Passing
        it emits a ``DeprecationWarning``.

    Returns
    -------
    NDArray[np.floating]
        Shifted Ricker wavelet starting at *t = 0*.

    Raises
    ------
    ValueError
        If *f*, *duration*, or *dt* are not positive.
    TypeError
        If both *len* and a non-default *duration* are given.

    Notes
    -----
    The returned signal always starts at *t = 0*.  For a different starting
    point, shift the corresponding time vector instead.
    """
    if len is not None:
        if duration != 0.5:
            raise TypeError("Pass duration or the deprecated len, not both.")
        warnings.warn(
            "ricker(len=...) is deprecated; use duration=... instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        duration = len

    if f <= 0:
        raise ValueError("Centre frequency (f) must be positive.")
    if duration <= 0:
        raise ValueError("Signal duration must be positive.")
    if dt <= 0:
        raise ValueError("Time interval (dt) must be positive.")

    n_samples = int(duration / dt)

    if duration < peak_loc:
        warnings.warn(
            "Peak location is outside the signal range. Returning all-zero output.",
            stacklevel=2,
        )
        return np.zeros(n_samples)

    t = np.linspace(-peak_loc, duration - peak_loc - dt, n_samples)
    pf2t2 = np.pi**2 * f**2 * t**2
    return (1 - 2 * pf2t2) * np.exp(-pf2t2)
