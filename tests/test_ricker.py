import pytest

from ricker.ricker import ricker


class TestRicker:
    def test_output_number(self):
        assert len(ricker()) == 2

    def test_default_output(self):
        t, s = ricker()
        assert len(t) == len(s)

    def test_error(self):
        with pytest.raises(ValueError):
            ricker(f=0)
