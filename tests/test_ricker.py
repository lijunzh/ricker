import pytest

from ricker.ricker import ricker


class TestRicker:
    def test_default_output(self):
        dt = 0.002
        length = 1
        s = ricker(len=length, dt=dt)
        assert len(s) == int(length / dt)

    def test_input_check_f(self):
        with pytest.raises(ValueError):
            ricker(f=0)

    def test_input_check_len(self):
        with pytest.raises(ValueError):
            ricker(len=0)

    def test_input_check_dt(self):
        with pytest.raises(ValueError):
            ricker(dt=0)

    def test_input_len_peak_loc(self):
        with pytest.warns(UserWarning):
            ricker(len=1, peak_loc=2)
