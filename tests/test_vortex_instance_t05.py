import pytest
from scipy import interpolate

from src.sc_vortex_2d.vortex import VortexInstanceT05


@pytest.fixture
def make_instance() -> VortexInstanceT05:
    instance = VortexInstanceT05()
    instance._construct()
    return instance


def test_instance(make_instance):
    instance: VortexInstanceT05 = make_instance
    assert len(instance.spectra_dict) == 200
    assert len(instance.u_dict) == 200
    assert len(instance.v_dict) == 200


def test_get_pair_potential(make_instance):
    instance: VortexInstanceT05 = make_instance
    assert isinstance(instance.get_pair_potential(), interpolate.CubicSpline)


def test_get_ith_eigen_energy(make_instance):
    instance: VortexInstanceT05 = make_instance
    assert instance.get_ith_eigen_energy(0) == 0.5
    assert instance.get_ith_eigen_energy(-1) == -0.5

def test_get_ith_eigen_func(make_instance):
    instance: VortexInstanceT05 = make_instance
    target = instance.get_ith_eigen_func(0)
    assert len(target) == 2
    assert isinstance(target[0], interpolate.CubicSpline)
    assert isinstance(target[1], interpolate.CubicSpline)
    
