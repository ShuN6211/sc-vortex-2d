import pytest
from src.sc_vortex_2d.vortex import VortexInstanceT03
from scipy import interpolate


@pytest.fixture
def make_instance() -> VortexInstanceT03:
    instance = VortexInstanceT03()
    instance.construct()
    return VortexInstanceT03()


def test_get_pair_potential(make_instance):
    instance: VortexInstanceT03 = make_instance
    assert isinstance(instance.get_pair_potential(), interpolate.CubicSpline)
