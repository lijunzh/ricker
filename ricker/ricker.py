import numpy as np


def ricker(f=10, len=0.5, dt=0.002, peak_loc=0.25):
    """
    ------------------------------------------------------------
    Generate ricker wavelet signal for seismic simulation
    ------------------------------------------------------------

    Input and output:
        :param f: (float) peak frequency in Hz (default 10)
        :param len: (float) length of signal in sec (default 0.5)
        :param dt: (float) time resolution in sec (default 0.002)
        :param peak_loc: (float) peak location in sec (default 0.25)

        :return:
        t (nparray): time sequence
        y (nparray): ricker signal sequence

    Examples:
        This function can be called directly with no argument as following::

            $ ricker_signal = seispy.ricker()

        which returns a 10 Hz Ricker wavelet that peaked at 0.25 sec,  0.5
        sec long and sampled at 500 Hz.

        Users can generate different Ricker wavelet by tweaking the input
        argument

    References:
        http://subsurfwiki.org/wiki/Ricker_wavelet
    """

    # Import check
    if f <= 0:
        raise ValueError("Center frequency (f) needs to be positive.")

    if len <= 0:
        raise ValueError("Signal length (len) needs to be positive.")

    if dt <= 0:
        raise ValueError("Time interval (dt) needs to be positive.")

    # Generate time sequence based on sample frequency/period, signal length
    # and peak location
    t = np.linspace(-peak_loc, len - peak_loc - dt, int(len / dt))

    # Shift signal to the correct location
    t_out = t + peak_loc  # time shift Ricker wavelet based on peak_loc

    # Generate Ricker wavelet signal based on reference
    y = (1 - 2 * np.pi ** 2 * f ** 2 * t ** 2) * np.exp(
        -np.pi ** 2 * f ** 2 * t ** 2)

    return t_out, y

if __name__ == '__main__':
    pass
