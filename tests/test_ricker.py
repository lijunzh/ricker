"""Tests for the ricker wavelet generator."""

import numpy as np
import pytest

from ricker import ricker


class TestInputValidation:
    """Ensure invalid inputs are rejected."""

    def test_rejects_zero_frequency(self):
        with pytest.raises(ValueError, match="frequency"):
            ricker(f=0)

    def test_rejects_negative_frequency(self):
        with pytest.raises(ValueError, match="frequency"):
            ricker(f=-5)

    def test_rejects_zero_duration(self):
        with pytest.raises(ValueError, match="duration"):
            ricker(duration=0)

    def test_rejects_zero_dt(self):
        with pytest.raises(ValueError, match="dt"):
            ricker(dt=0)

    def test_warns_peak_outside_range(self):
        with pytest.warns(UserWarning, match="outside"):
            result = ricker(duration=1, peak_loc=2)
        assert np.all(result == 0)


class TestWavelet:
    """Verify correct wavelet generation."""

    def test_output_length(self):
        dt = 0.002
        duration = 1.0
        result = ricker(duration=duration, dt=dt)
        assert len(result) == int(duration / dt)

    def test_peak_at_expected_location(self):
        result = ricker(f=10, duration=0.5, dt=0.001, peak_loc=0.25)
        peak_idx = np.argmax(result)
        peak_time = peak_idx * 0.001
        assert peak_time == pytest.approx(0.25, abs=0.002)

    def test_peak_value_is_one(self):
        # At t=0 (peak_loc), the Ricker wavelet equals 1.0
        result = ricker(f=10, duration=0.5, dt=0.001, peak_loc=0.25)
        assert np.max(result) == pytest.approx(1.0, abs=0.01)

    def test_returns_numpy_array(self):
        assert isinstance(ricker(), np.ndarray)

    def test_default_params_produce_nonzero(self):
        result = ricker()
        assert np.any(result != 0)

    def test_higher_frequency_narrower_wavelet(self):
        low_f = ricker(f=5, duration=1, dt=0.001, peak_loc=0.5)
        high_f = ricker(f=20, duration=1, dt=0.001, peak_loc=0.5)
        # Higher freq wavelet should have fewer samples above half-max
        low_width = np.sum(low_f > 0.5 * np.max(low_f))
        high_width = np.sum(high_f > 0.5 * np.max(high_f))
        assert high_width < low_width
