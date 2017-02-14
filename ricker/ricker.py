import warnings

import numpy as np


def ricker(f: float = 10, len: float = 0.5, dt: float = 0.002,
           peak_loc: float = 0.25) -> np.ndarray:
    """ricker creates a shifted causal ricker wavelet (Maxican hat).

    :param f: center frequency of Ricker wavelet (default 10)
    :param len: float
    :type len: signal length in unit of second (default 0.5 sec)
    :param dt: float
    :type dt: time sampling interval in unit of second (default 0.002 sec)
    :param peak_loc: float
    :type peak_loc: location of wavelet peak in unit of second (default 0.25
    sec)
    :return: shifted Ricker wavelet starting from t=0.
    :rtype: np.ndarray

    Note that the returned signal always starts at t=0. For a different
    starting point, it can be achieved by shifting the time vector instead.


    """
    # Import check
    if f <= 0:
        raise ValueError("Center frequency (f) needs to be positive.")

    if len <= 0:
        raise ValueError("Signal length (len) needs to be positive.")

    if dt <= 0:
        raise ValueError("Time interval (dt) needs to be positive.")

    if len < peak_loc:
        warnings.warn("The peak location is outside the signal range. All "
                      "zero output will be provided.")
        return np.zeros(int(len / dt))
    else:
        # Generate time sequence based on sample frequency/period, signal length
        # and peak location
        t = np.linspace(-peak_loc, len - peak_loc - dt, int(len / dt))

        # Shift time to the correct location
        # t_out = t + peak_loc  # time shift Ricker wavelet based on peak_loc

        # Generate Ricker wavelet signal based on reference
        y = (1 - 2 * np.pi ** 2 * f ** 2 * t ** 2) * np.exp(
            -np.pi ** 2 * f ** 2 * t ** 2)

        return y


if __name__ == '__main__':
    pass
